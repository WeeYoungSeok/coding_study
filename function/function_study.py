# 함수란 특정한 작업을 하나의 단위로 묶어 놓은 것을 의미한다.
# 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있다.

# 내장 함수 : 파이썬이 기본적으로 제공하는 함수
# 사용자 정의 함수 : 개발자가 직접 정의하여 사용할 수 있는 함수

# 프로그램에는 똑같은 코드가 반복적으로 사용되어야 할 때가 많다.
# 함수를 사용하면 소스코드의 길이를 줄일 수 있다.
# 매개 변수 : 함수 내부에서 사용할 변수
# 반환 값 : 함수에서 처리 된 결과를 반환

def test(test):
    # 소스코드
    print("Hello")
    return test

# 더하기 함수
def add(a, b):
    return a + b
print(add(3, 7))

# 더하기 함수 예제 2
def add2(a, b):
    print("함수의 결과 :", a + b)
add2(3, 7)

# 파라미터의 변수 직접 지정
add2(b = 3, a = 7)

# global 키워드
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

# 함수에서 외부 변수명(전역)과 함수 내부 변수명(지역)이 같다면 지역 변수를 우선으로 타겟한다.

# 여러개 값 반환 (패킹)
def operator(a, b):
    add_var = a + b
    subtract_var = a - b
    multiply_var = a * b
    divide_var = a / b
    return add_var, subtract_var, multiply_var, divide_var

# 여러개 값 반환 받기 (언패킹)
a, b, c, d = operator(3, 7)
print(a, b, c, d)

# 람다
# 람다 표현실을 이용하면 함수를 간단하게 작성 가능
print((lambda a, b: a + b)(3, 7))

# 정말 많이 쓰이는 문법
# 리스트 안에 튜플의 두번째 원소를 기준으로 정렬
array = [("홍길동", 50), ("이순신", 32), ("아무개", 74)]

def my_key(x):
    return x[1]

# 함수를 선언하여 정렬
print(sorted(array, key=my_key))
# 람다식으로 함수를 내부에 써서 정령
print(sorted(array, key=lambda x: x[1]))

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# list1, list2의 원소를 같은 번지끼리 더해서 map으로 만듬
result = map(lambda a, b: a + b, list1, list2)

print(list(result))
