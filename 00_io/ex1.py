# 입출력 처리

# 1개 입력
# a = input()
# print(a)
# print(type(a))

# 정수 변환
# a = input()
# a = int(a)  # int("100")
# print(type(a))

# 한 번에 쓰자
a = int(input())
print(a, type(a))

# 실수 입력
b = float(input())
print(b, type(b))  # 10 입력하면 10.0 출력 됨

# 정수 2개 입력
# 100
# 200
a = int(input())
b = int(input())
print(a, b)

# 100 200
a = input().split(" ")  # separator를 생략하면 자동으로 공문자로 설정됨
print(a)

# map 사용하기
# map(함수, 리스트)
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트로 변환
a = list(map(int, input().split()))
print(a)
