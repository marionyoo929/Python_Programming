# 비트 연산자
a = 5 # 0000 0101
b = 3 # 0000 0011

print(a & b)   # 0000 0001   --> and
print(a | b)   # 0000 0111   --> or
print(a ^ b)   # 0000 0110   --> xor
print(a << b)  # 5 -> 10 -> 20 -> 40
print(40 >> b) # 5
print(~a)      # 1111 1010

# 멤버십 연산자
print("a" in "apple")
print(3 in [1, 2, 3])

# 삼항 연산자
# int max = a > b ? a : b;    ->  C 문법 (a, b 비교해서 둘 중에 큰 값이 max로 들어감)
max = a if a > b else b       # a가 b보다 크면 a를 max

# a가 짝수면 "짝수", 홀수면 "홀수"
print("짝수" if a%2 == 0 else "홀수")

# 삼항연산자
# 90점 이상이면 A 출력
# 80점 이상이면 B 출력
# 70점 이상이면 C 출력
# 70점 미만이면 D 출력
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
print(grade)
