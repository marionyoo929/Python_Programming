# __init__.py 파일 (패키지 초기화 파일)   -  이름 정해져 있음

# 1. 패키지를 import할 때 실행되어야 하는 초기화 코드 (환경 확인, 설정값 로드)
print("__init__")

# 2. 패키지 메타데이터 설정 (버전 정보)
VERSION = "1.0.0"

# 3. 패키지 re-export
# from mypackage.mymath import add    # 절대 import 방식
from .mymath import add               # 상대 import 방식