# 문자열 자료형
# 큰, 작은 따옴표 둘개로 초기화 가능
# 전체 문자열이 큰 따옴표로 묶여있다면 내부에서 작은 따옴표 사용가능, 반대도 가능
# 백슬래쉬 두개(이스케이프)로도 가능

data = 'Hello World'
print(data)

# 문자열 연산
# 덧셈과 곱셈 연산을 사용할 수 있다.
# 덧셈은 문자열이 이어지고
# 곱셈은 몬자열이 여러번 더해진다.
# 문자열은 특정 인덱스를 변경 불가능(immutable)

a = "Hello"
b = "World"
print (a + " " + b)

# 에러 발생
# str은 원소 할당 지원 안함 에러
a[2] = 'a'
