import requests
from .api import NaverApi
from .exceptions import *

class LanguageDetect(NaverApi):

    _languagedetecturl = "https://openapi.naver.com/v1/papago/detectLangs"

    def _makecontext(self):
        self._params = {
            "query" : self.context
        }

    def detect(self, context : str):
        self.context = context
        self._makeheader(self._clientid, self._clientsecret)
        self._makecontext()

        try:
            self._response = requests.post(self._languagedetecturl, \
                data = self._params, \
                headers = self._headers)
            self._response.raise_for_status()

        except requests.exceptions.HTTPError:
            self._errorcode = self._response.json()["errorCode"]
            raise PapagoError(self._errorcode)

        except requests.exceptions.ConnectTimeout:
            raise Exception("서버 연결 에러")
        
        except:
            raise Exception("정의되지 않은 에러입니다")
        
        else:
            return self._response.json()["langCode"]