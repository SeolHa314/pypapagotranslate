class PapagoError(Exception):
    def __init__(self, code, *args) :
        self.errorcode = code

        if(self.errorcode in ["N2MT01", "TR01"]):
            self.message = "source 파라미터가 필요합니다."
        elif(self.errorcode in ["N2MT02", "TR02"]):
            self.message = "지원하지 않는 source 언어입니다."
        elif(self.errorcode in ["N2MT03", "TR03"]):
            self.message = "target 파라미터가 필요합니다."
        elif(self.errorcode in ["N2MT04", "TR04"]):
            self.message = "지원하지 않는 target 언어입니다."
        elif(self.errorcode in ["N2MT05", "TR05"]):
            self.message = "target 언어와 source 언어가 같습니다."
        elif(self.errorcode in ["N2MT06", "TR06"]):
            self.message = "source->target 번역기가 없습니다."
        elif(self.errorcode in ["N2MT07", "TR07"]):
            self.message = "text 파라미터가 필요합니다."
        elif(self.errorcode in ["N2MT08", "TR08"]):
            self.message = "text 파라미터가 최대 용량을 초과했습니다."
        elif(self.errorcode in ["N2MT99", "TR99", "LD99"]):
            self.message = "내부 서버 에러"
        elif(self.errorcode == "LD01"):
            self.message = "입력된 text가 없습니다"
        elif(self.errorcode == "400"):
            self.message = "잘못된 쿼리요청입니다"
        elif(self.errorcode == "024"):
            self.message = "인증에 실패하였습니다"
        elif(self.errorcode == "072"):
            self.message = "지원하지 않는 프로토콜입니다. HTTPS를 사용해 주세요."
        else:
            self.message = "정의되지 않은 에러입니다."

        super(PapagoError, self).__init__(self.message, *args)