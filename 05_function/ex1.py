# 함수 1

# ===========================================================
# 1. 기본 함수
# ===========================================================

# ind add(int a, int b)
# {
#    return a + b;
# }
# -> c


def add(a, b):
    """a + b 결과를 반환한다."""   # docstring
    return a + b  # __add__()   호출


print(add(3, 4))
print(add("hello", "python"))
print(add([1, 2], [3, 4]))  # list o
print(add((1, 2), (3, 4)))  # tuple O
# dictionary X, set? X
print(add.__doc__)          # docstring 출력, 없으면 None

# ===========================================================
# 2. 튜플을 리턴하는 함수
# ===========================================================
def add_sub(a, b):
    return a + b, a - b   # 소괄호 생략하면 tuple로 return 됨. list로도 return 할 수 있음 (return 개수는 한 개 !!)

print(add_sub(5, 3))
print(*add_sub(5, 3))

x, y = add_sub(5, 3)
print(x, y)
# tuple unpacking

# ===========================================================
# 3. 디폴트 매개변수 (Default Parameter)
# ===========================================================
# 매개변수에 기본값을 지정하면, 호출 시 해당 인자를 생략할 수 있다.
# 디폴트 매개변수는 항상 일반 매개변수 뒤에 위치해야 한다.
def add(a, b = 0):   # b가 인자로 들어오지 않을 경우 b의 값을 0으로 지정, a = 0 안됨
    return a + b

print(add(5, 10))
print(add(5))


# ===========================================================
# 4. 키워드 인자 (Keyword Argument)
# ===========================================================
# 인자를 순서가 아니라 "매개변수명=값" 형태로 전달할 수 있다.
# 순서를 바꿔서 호출해도 이름만 맞으면 정확히 전달된다.

print(add(5, 10))            # 순서대로 인자 전달
print(add(b = 10, a = 5))    # 키워드 인자로 매핑

def introduce(name, age, city = "안산"):
    return f"저는 {name}이고, {age}살이며 {city}에 살아요."

print(introduce("뽀로로", 5, "일산"))
print(introduce(age = 5, city = "일산", name = "뽀로로"))
print(introduce("뽀로로", 5))


# ===========================================================
# 5. 가변 인자 (Variable-length Argument, *args)
# ===========================================================
# 몇 개의 인자가 들어올지 모를 때 *args를 사용한다. (관례적으로 사용)
# args라는 이름으로 입력값들을 모아 튜플로 만든다.

def add_all(*args):  # 풀린 걸 다시 묶어줌
    print(args)
    return sum(args)
# 그냥 args로 쓰면 안됨. 매개 변수를 하나로 받아야 된다고 오류 뜸 (아마)
# args는 tuple로 변환 ?
print(add_all(1, 2, 3))
print(add_all(1, 2, 3, 4, 5))
a = [1, 2, 3]
print(add_all(*a))   # 묶은 걸 다시 풀어줌

# ================================================================
# 6. 키워드 가변 인자 (Keyword Variable-length Argument, **kwargs)
# ================================================================
# 이름=값 형태로 몇 개가 들어올지 모를 때 **kwargs를 사용한다.
# kwargs라는 이름으로 입력값들을 모아 딕셔너리로 만든다.

def introduce2(**kwargs):   # 푼 거를 받아서 묶어줌
    print(kwargs)


d = {"name": "크롱", "age": 4, "kind": "공룡"}

introduce2(name = "크롱", age = 4, kind = "공룡")
introduce2(**d) # key, value 모두 언패킹   # 묶인 거를 받아서 풀어줌

# ===========================================================
# 7. *args와 **kwargs를 함께 사용하는 예시
# ===========================================================

# 디미가 현재 가진 돈 구하기
# - 지난 달 남은 돈 : 500원
# - 길 가다가 주운 돈 : 100원, 200원 => 가변인자 (튜플)
# - 아빠한테 받은 돈 : 10000원
# - 엄마한테 받은 돈 : 5000원 => 키워드 가변인자 (딕셔너리)

def pocket_money(last_month, *args, **kwargs):
    tot = last_month
    tot += sum(args)
    tot += sum(kwargs.values())
    return tot

print(pocket_money(500, 100, 200, dad = 10000, mom = 5000, uncle = 50000))