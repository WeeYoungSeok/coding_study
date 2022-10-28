# 모든 프로그램은 적절한 입출력 양식을 가지고 있다.
# 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것이다.

# input() 함수는 한 줄의 문자열을 입력 받는 함수
# map() 함수는 리스트의 모든 원소에 각각 특정한 함수를 적용할 떄 사용
# ex) 공백 기준으로 구분된 데이터를 입력 받을때
a = list(map(int, input().split())
# 공백 기준으로 구분된 데이터의 개수가 많지 않다면, 단순히 다음과 같은 방법 이용 가능
a, b, c = map(int, input().split())
     
# 학생 성적 데이터가 주어지고, 이를 내림차순으로 정렬한 결과를 출력하는 프로그램
n = int(input())
data = list(map(int, input().split()))
print(data.sort(reverse = True))

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# sys 라이브러리에 정의되어 있는 sys.stdin.readline() 메서드 이용
# 단, 입력 후 엔터가 줄 바꿈 기호로 입력되므로 rstrip() 메서드를 함께 사용

import sys
data = sys.stdin.readline().rstrip()
print(data)

# 파이썬 띄어쓰기로 구분하여 출력할 경우 ,로 print에서 구분

# print()는 기본적으로 출력 이후 줄 바꿈 수행
# 원치않는 경우 end 속성으로 조정 가능

a = 1
b = 2
print(a, b)
print(7, end=" ")
print(8, end=" ")

answer = 7
# 파이썬은 문자열과 정수형을 같이 쓸 수 없으므로 형변환 필요
print("정답은 " + str(answer) + "입니다.")

# 파이썬 3.6부터 사용 가능
# 형변환 없이 f 스트링 문법 사용 가능
print(f"정답은 {answer}입니다.")