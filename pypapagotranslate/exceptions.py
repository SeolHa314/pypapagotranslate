class PapagoError(Exception):
    def __init__(self, code, *args) :
        self.errorcode = code

        if(self.errorcode == "N2MT01"):
            self.message = "source 파라미터가 필요합니다."
        elif(self.errorcode == "N2MT02"):
            self.message = "지원하지 않는 source 언어입니다."
        elif(self.errorcode == "N2MT03"):
            self.message = "target 파라미터가 필요합니다."
        elif(self.errorcode == "N2MT04"):
            self.message = "지원하지 않는 target 언어입니다."
        elif(self.errorcode == "N2MT05"):
            self.message = "target 언어와 source 언어가 같습니다."
        elif(self.errorcode == "N2MT06"):
            self.message = "source->target 번역기가 없습니다."
        elif(self.errorcode == "N2MT07"):
            self.message = "text 파라미터가 필요합니다."
        elif(self.errorcode == "N2MT08"):
            self.message = "text 파라미터가 최대 용량을 초과했습니다."
        elif(self.errorcode == "N2MT99"):
            self.message = "내부 서버 에러"
        else:
            self.message = "정의되지 않은 에러입니다."

        super(PapagoError, self).__init__(self.message, *args)