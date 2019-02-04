import requests
import json
from .api import NaverApi
from .exceptions import *

class NameRomanizer(NaverApi):
    
    _NameRomanUrl = u"https://openapi.naver.com/v1/krdict/romanization?query="

    def _makecontent(self):
        self._UrlRequest = self._NameRomanUrl + self.koreanName

    def romanize(self, koreanName):

        self.koreanName = koreanName
        self._makeheader(self._clientid, self._clientsecret)
        self._makecontent()

        try:
            self._response = requests.post(self._UrlRequest, \
                headers = self._headers)
            self._response.raise_for_status()

        except requests.exceptions.HTTPError:
            self._errorcode = json.loads(self._response.text[self._response.text.find("{"):])["errorCode"]
            raise PapagoError(self._errorcode)

        except requests.exceptions.ConnectTimeout:
            raise Exception("서버 연결 에러")
        
        except:
            raise Exception("정의되지 않은 에러입니다")
        
        else:
            return self._response.json()["aResult"][0]["aItems"]