# 특정한 소스코드를 반복적으로 실행하고자 할 때 사용하는 문법
# 파이썬에서는 while문과 for문이 존재
# 보통 코딩 테스트에서의 실제 사용 예시를 확인해 보면, for문이 더 간결한 경우가 많다.

array = [9, 8, 7, 6, 5]

for x in array:
    print(x)

# range
# 연속적인 값을 차례대로 순회 가능
# range(시작 값, 끝 값 + 1)
# 인자를 하나만 넣으면 자동으로 시작 값은 0
result = 0

# i는 1부터 9까지 모든 값을 순회
for i in range(1, 10):
    result += 1
print(result)

# continue
# 반복문에서 남은 코드의 실행으 ㄹ건너뛰고, 다음 반복을 진행하고자 할 때 사용

# 1부터 9까지 홀수 함
result = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    result += 1
print(result)

scores = [90, 85, 77, 65, 97]

for i in range(5):
    if score[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

cheating_student_list = {2, 4}

for i in range(5):
    if i + 1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)
    print()