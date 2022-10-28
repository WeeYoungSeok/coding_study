# 프로그램의 흐름을 제어하는 문법

# 조건, 반복문을 사용할떄 들여쓰기 주의

x = 15

if x >= 10:
    print("x >= 10")

if x >= 0:
    print("x >= 0")

if x >= 30:
    print("x >= 30")

# elif, else
a = 5

if a >= 0:
    print("a >= 0")
elif a >= -10:
    print("0 > a >- -10")
else:
    print("-10 > a")

score = 85

if score >= 90:
    print("학점 : A")
elif score >= 80:
    print("학점 : B")
elif socre >= 70:
    print("학점 : C")
else:
    print("학점 : F")

# 비교 연산자
# == : 서로 값이 같을 떄
# != : 서로 값이 다를 떄
# >, >=, <, <= : 초과, 이상, 미만, 이하

# 논리 연산자
# X and Y : X와 Y가 모두 참일 떄 참
# X or Y : X와 Y중에 하나만 참이어도 참이다.
# net X : X가 거짓일 떄 참

# Yes 출력됨
if True or False:
    print("Yes")

# Yes 출력 안됨
if True and False:
    print("Yes")

a = 15

# Yes 출력 됨
if a <= 20 and a > 0:
    print("Yes")

# 기타 연산자
# 다수의 데이터를 담는 자료형을 위해 in 연산자와 not in 연산자가 제공된다.
# 리스트, 튜플, 문자열, 딕셔너리 모두에서 사용 가능하다.

# x in 리스트 : 리스트 안에 x가 들어있을 때 참
# x not in 리스트 : 리스트 안에 x가 없을 떄 참

# 파이썬 pass 키워드
# 아무것도 처리하고 싶지 않을 떄 pass 키워드 사용
# 디버깅 과정에서 일단 조건문의 형대만 만들어 놓고 조건문을 처리하는 부분은 비워놓고 싶은 경우
# 파이썬은 조건, 반복문만 선언하고 내부에 코드를 작성하지 않으면 에러 발생

score = 85

if score >= 80:
    pass # 나중에 작성할 소스코드
else:
    print("성적이 80 미만이다.")

# 조건문 간소화
# 조건문에서 실행될 코드가 한 줄인 경우 줄바꿈 하지 않아도 된다.

score = 85
if score >= 80: result = "Success"
else: result = "Fail"

# 조건부 표현식은 if ~ else문을 한 줄에 작성할 수 있도록 해줌
# 참이 왼쪽 거짓이 오른쪽
result = "Success" if score >= 80 else "Fail"

