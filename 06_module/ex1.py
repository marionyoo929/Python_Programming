# 1. 모듈

# 자주 사용하는 기능을 모아놓은 파이썬 파일 한 개
# 모듈에는 함수, 클래스, 변수를 정의할 수 있다.

# 모듈(패키지)의 종류
# 1. 표준 라이브러리 모듈(패키지): 파이썬 제공
# 2. 써드 파티 모듈(패키지): 외부에서 만들어서 배포
# 3. 사용자 정의 모듈(패키지)

# =====================================================================
# 1. 파이썬 표준 라이브러리 불러오기 (https://docs.python.org/3/library)
#  - import 모듈명
#  - from 모듈명 import 함수명
#  - from 패키지명 import 모듈명 (from 가져올 위치 import 가져올 대상)
# =====================================================================

# math 모듈: 수학 계산에 필요한 함수와 상수를 제공하는 표준 라이브러리

import math

print(dir(math))
print(math.sqrt(16))
print(math.pi)


# 별칭 만들기
import math as m

print(m.sqrt(16))
print(m.pi)

# 모듈명 없이 바로 함수명으로 불러오기
# 가져올 함수가 너무 많으면 *써도 됨
from math import sqrt, pi

print(sqrt(16))
print(pi)


# sys 모듈: 파이썬 인터프리터의 실행 환경과 관련된 정보를 제공하는 표준 라이브러리
import sys

print(sys.version)                  # 현재 실행 중인 파이썬 인터프리터의 버전
print(sys.platform)                 # 현재 실행 중인 운영체제 플랫폼 식별자
print(sys.path)                     # 파이썬 라이브러리 검색 디렉토리 목록

# 표준 라이브러리 설치 경로: C:\Users\<user_name>\AppData\Local\Programs\Python\Python314\Lib
# 써드 파티 설치 경로: C:\Users\<user_name>\AppData\Local\Programs\Python\Python314\Lib\site-packages


# ===========================================================
# 2. 써드 파티 모듈 불러오기 (https://pypi.org/)
#  - 패키지 목록 보기: pip list
#  - 패키지 설치 하기: pip install 패키지명
# ===========================================================

# requests 모듈: HTTP 요청과 응답을 처리하기 위한 써드 파티 모듈
import requests

# url = "https://httpbin.org/get"
url = "https://httpbin.org/get?user_id=crong" # key = value

# 응답코드 200 = okay
# 404 = not found
# 500 = internal server error - 인터널 서버 에러

response = requests.get(url)

print(response.status_code) # 응답 코드 확인
print(response.text)        # 결과 확인
# url 뒤에 ?key=value 쓰면 args에 우리가 입력한 값이 들어감
print(type(response.text))  # <class 'str'>
# 실제 서버에 갔다 오는 것임

# 직렬화와 역직렬화
# - 직렬화 (Serialization) : 메모리 상의 객체를 파일 저장 or 네트워크 전송이 가능한 형태로 변환하는 것
#                           (메모리 상에 있는 객체를 그대로 전송하는 것이 불가능하기 때문)
# - 역직렬화 (Deserialization) : 저장된 or 전송받은 데이터를 원래의 객체로 복원
# - 데이터 직렬화 방식 : XML, JSON, YAML
# XML의 가장 큰 단점 : 전송량 많음
# JSON -> 더 간결해짐
# YAML -> 더더 간결해짐 (아예 들여쓰기로 구분)

d = response.json()     # 서버가 응답한 JSON 형식의 문자열을 Python 객체로 변환 -> 역직렬화

print(type(d))
print(d["args"]["user_id"])
print(d["headers"]["Host"])
# ===========================================================
# 3. 사용자 정의 모듈 만들기
# ===========================================================
import mymath
from mymath import PI, add
# start: mymath
# import만 했는데도 실행이 됨 -> import를 하는 순간 해당되는 모듈의 가장 바깥에 있는 최상위 코드가 실행되기 때문에 실행이 되는 것임
# if문 써서 실행 안되게

# import mymath 했을 때는 start: mypath가 실행됨
# from mymath import PI, add 했을 때는 이미 mymath가 최초 한 번 실행되어 있기 때문에 최상위 코드가 실행되지 않음

print(mymath.PI)
print(mymath.add(20, 30))

print(PI)
print(add(20, 30))

# __pycache__ 디렉토리란?
# Python이 실행 속도를 높이기 위해 컴파일된 바이트코드(.pyc)를 캐시로 저장하는 디렉터리
# 모듈을 import할 때만 생성되고, 직접 실행할 때에는 바이트코드까지만 생성하고 저장하지는 않음
# mymath 안에서 직접 실행할 때는 생성 되지 않고 외부에서 호출했을 때만 생긴다는 뜻

# pycache는 임시파일이기 때문에 github에도 올라가지 않음 (gitignore에 올라가 있음)


# Python 모듈 실행 방식
# 1. CPython에 있는 컴파일러가 Python 소스 코드를 바이트코드(.pyc)로 컴파일 -> 기계어로 변환하는 것 x - 바이트 코드는 중간 코드임
# 2. Python 가상 머신(PVM)이 바이트코드를 실행
# 3. 다음 실행 시에는 .pyc를 바로 읽어 실행
# 4. 모듈이 변경된 경우 .pyc 파일을 재생성하여 실행