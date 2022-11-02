# 구현
# 머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정
# 거의 모든 코딩테스트 문제가 구현이다.
# 구현 문제가 직접적으로 나오는 경우는 구현이 어려운 경우이다.

# 풀이를 떠올리는 것은 쉽지만 소스코드로 옮기기 어려운 문제를 지칭

# 예시
# 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 분제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리를 찾아서 사용해야 하는 문제

# 일반적으로 2차원 배열이 많이 출제된다.
# 행렬의 정의를 알면 유용하다.

# 방향 벡터가 자주 활용된다.

# 동 북 서 남
# x는 행, y는 열
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

# 동 북 서 남 기준으로 다음 위치 출력
for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# 상하 좌우 문제
n = int(input())
v = list(map(str, input().split()))

# 첫 위치
x, y = 1, 1

move_types = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for vector in v:
    for i in range(len(move_types)):
        if vector == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간 벗어나는 경우 무시
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
print(x, y)


# 시각
n = int(input())

count = 0

# for i in range(n + 1):
#     if "3" in str(i):
#         count += 3600
#         continue
#     for j in range(0, 60):
#         if "3" in str(j):
#             count += 60
#             continue
#         for k in range(0, 60):
#             if "3" in str(k):
#                 count += 1
# print(count)

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if "3" in str(i) + str(j) + str(k):
                count+= 1
print(count)


# 왕실의 나이트

# 내 풀이
n = input()

x = int(n[1])
y = ord(n[0]) - 96
print(x, y)

# 2칸씩 이동 상하좌우
two_dx = [-2, 2, 0, 0]
two_dy = [0, 0, -2, 2]

count = 0
# 수평 또는 수직 이동
v = [-1, 1]

for i in range(4):
    nx = x + two_dx[i]
    ny = y + two_dy[i]
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    if two_dx[i] < 0 or two_dx[i] > 0:
        for j in range(2):
            last_y = ny + v[j]
            if last_y < 1 or last_y > 8:
                continue
            count += 1
    else:
        for j in range(2):
            last_x = nx + v[j]
            if last_x < 1 or last_x > 8:
                continue
            count += 1
print(count)


# 이코테
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord("a")) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_x = row + step[0]
    next_y = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_x >= 1 and next_x <= 8 and next_y >= 1 and next_y <= 8:
        result += 1
print(result)

# 문자열 재정렬

# 내 풀이
n = input()
list_n = list(n)
list_n.sort()

sum_value = 0
result = ""

for i in range(len(list_n)):
    if ord(list_n[i]) >= 48 and ord(list_n[i]) <= 57:
        sum_value += int(list_n[i])
    else:
        list_n = list_n[i : len(list_n)]
        break
if sum_value != 0:
    print("".join(list_n) + str(sum_value))
else:
    print("".join(list_n))

# 이코테
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print("".join(result))