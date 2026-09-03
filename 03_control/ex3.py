# for문

# for x in iterable 객체:

for i in range(5):
    print(i, end=" ")

print()
a = range(5)
print(a.start, a.stop, a.step)

# 1 ~ 5
for i in range(1, 6, 1): # step은 생략 가능
    print(i, end=" ")
print()

for i in range(1, 10, 2):
    print(i, end=" ")
print()

# 5 ~ 1 거꾸로
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(1, 11):
    tot += i
else:
    print(f"tot: {tot}")
    
# for else도 됨

print(f"sum: {sum(range(1, 11))}")
# sum은 Python에서 제공하는 함수이기 때문에 변수명으로 사용할 수 없음

s = "hi한국어家📖😒"

for c in s:
    print(c, end=" ")
print()
print(len(s)) # Python은 글자 수 문자마다 하나로 샘 - C 같은 경우에 한글은 3으로 셈 <-- Python은 유니코드 기반이기 때문

# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j :< 5d}", end = " ")
    print()