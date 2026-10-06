# 사용자 정의 모듈
print("start:", __name__)     # 모듈의 이름을 가져오는 내장 변수
# 내가 모듈을 직접 실행할 때는 __main__ 이라고 나옴
# 다른 곳에서 호출했을 때는 다름
PI = 3.14

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(PI)
    print(add(10, 20))
