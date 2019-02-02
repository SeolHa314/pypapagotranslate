# pypapagotranslate

> 파이썬을 위한 파파고 라이브러리

만든 사람 : [SeolHa314](https://github.com/seolha314)

현재 버전 : 0.1.1.2

## 이건 무었을 하느냐.

파파고 번역의 api 이용을 편하게 하기 위해서 만든 것이다.

## 설치

**그런 거 없다.**

그냥 프로젝트 폴더에 pypapagotranslate 폴더를 넣어서 쓰도록.

## 쓰는 방법

```python
from pypapagotranslate import N2MT, SMT

n2mt = n2mt("n2mt_api_clientid", "n2mt_api_secret")

print(n2mt.translate("en", "ko", "Hello world!")) # 출발 언어, 번역 대상 언어, 번역할 내용
# 안녕 세상!

print(n2mt.source)
# en

print(n2mt.target)
# ko

smt = smt("smt_api_clientid", "smt_api_secret")

print(n2mt.translate("en", "ko", "Just do it!")) # 출발 언어, 번역 대상 언어, 번역할 내용
# 단지 행하라!

print(n2mt.source)
# en

print(n2mt.target)
# ko
```

## 주의점

**언어 감지 기능은 아직 없음**

~~아직 구현된 것은 N2MT 번역 뿐이고, SMT 번역은 구현 예정.~~

SMT 번역을 구현했습니다.

## 여담

아직 구현 초기니, 기능도 거의 없고 겉면만 만들어져 있음.

## TODO

- [x] SMT 번역 구현하기
- [x] setup.py 만들기
- [ ] 버그 찾아보기
- [ ] 코드 가독성 올리기
- [ ] 테스트도 추가하기