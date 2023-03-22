# Proof of concept Kwangwoon Univ library QR check emulator

[광운대학교 중앙도서관 앱](https://play.google.com/store/apps/details?id=idoit.slpck.kwangwoon)의 내부 API를 분석해 QR코드를 생성하는 기능을 파이썬으로 구현한 코드입니다.

### Requirement
* Python
* Pycryptodome
* requests
* qrcode (Python module)

### Usage
```
python poc.py [학번] [비밀번호] [전화번호]
```

### How it works?
광운대학교 중앙도서관 앱을 [jadx](https://github.com/skylot/jadx), [Frida](https://frida.re/), adb, IDA 등의 분석 도구를 이용해 내부 API 및 암/복호화 알고리즘을 분석하고 이를 파이썬 코드로 구현하였습니다.

### Disclaimer
* 이 코드는 광운대학교 중앙도서관 앱을 분석한 결과를 바탕으로 작성되었습니다.
* 해당 코드는 학습적 목적으로 작성되었으며, 광운대학교 중앙도서관 앱의 보안을 해킹하는 목적으로 작성되지 않았습니다.
* 해당 코드를 사용 혹은 참고함으로써 발생하는 모든 책임은 사용자에게 있습니다.

### License
GPLv3

### Special Thanks
* [cloudchamb3r](https://github.com/cloudchamb3r) For helping me how to reverse mobile app and encryption algorithm
