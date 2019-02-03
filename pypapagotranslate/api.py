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