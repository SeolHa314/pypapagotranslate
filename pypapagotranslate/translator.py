import requests
from .exceptions import *

class NaverApi():
    
    def __init__(self, clientid : str, clientsecret : str):
        self._clientid = clientid
        self._clientsecret = clientsecret

    def _makeheader(self, clientid : str, clientsecret : str):
        self._headers = {
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Naver-Client-Id" : clientid,
            "X-Naver-Client-Secret" : clientsecret
        }

class Translate(NaverApi):

    #_papagetranslateurl = "https://openapi.naver.com/v1/papago/n2mt"

    def _makecontent(self, source : str, target : str, context : str):
        self._params = {
            "source" : source,
            "target" : target,
            "text" : context
        }

    def translate(self, source : str, target: str, context : str):
        self.source = source
        self.target = target
        self._context = context
        self._makeheader(self._clientid, self._clientsecret)
        self._makecontent(self.source, self.target, self._context)

        try :
            self._response = requests.post(self._papagotranslateurl, \
                headers = self._headers, \
                data = self._params)
            self._response.raise_for_status()

        except requests.exceptions.HTTPError:
            self._errorcode = self._response.json()["errorCode"]
            raise PapagoError(self._errorcode)
            
        except requests.exceptions.ConnectTimeout:
            raise Exception("서버 연결 에러")

        except:
            raise Exception("정의되지 않은 에러")

        else:
            return self._response.json()["message"]["result"]["translatedText"]

class N2MT(Translate):
    _papagotranslateurl = "https://openapi.naver.com/v1/papago/n2mt"

class SMT(Translate):
    _papagotranslateurl = "https://openapi.naver.com/v1/language/translate"


            