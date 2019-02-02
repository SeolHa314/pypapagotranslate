# pypapagotranslate

> 파이썬을 위한 파파고 라이브러리

만든 사람 : [SeolHa314](https://github.com/seolha314)

현재 버전 : 0.0.1

## 이건 무었을 하느냐.

파파고 번역의 api 이용을 편하게 하기 위해서 만든 것이다.

## 설치

**그런 거 없다.**

그냥 프로젝트 폴더에 pypapagotranslate 폴더를 넣어서 쓰도록.

## 쓰는 방법

```python
from pypapagotranslate import PapagoTranslate

papago = PapagoTranslate("파파고_api_clientid", "파파고_api_secret")

print(papago.translate("en", "ko", "Hello world!")) # 출발 언어, 번역 대상 언어, 번역할 내용
# 안녕 세상!

print(papago.source)
# en

print(papago.target)
# ko
```

## 주의점

**언어 감지 기능은 아직 없음**

## 여담

아직 구현 초기니, 기능도 거의 없고 겉면만 만들어져 있음.