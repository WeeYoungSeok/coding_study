# data = dict()
# data['사과'] = "Apple"
# data['바나나'] = "Banana"
# data['코코넛'] = "Coconut"

# print(data)

# 사과라는 키 존재 여부 확인
# print구문 실행됨
# if '사과' in data:
#     print("'사과'를 키로 가지는 데이터가 존재합니다.")

# key_list = data.keys()
# value_list = data.values()

# print(key_list)
# print(value_list)

# for key in key_list:
#     print(data[key])

# n = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse = True)
# print(data)

# a = 0

# def func():
#     global a
#     a += 1

# for i in range(10):
#     func()

# print(a)

# N = 1260
# array = [500, 100, 50, 10]
# result = 0

# for i in array:
#     result += N // i
#     N = N % i
# print(result)

# n, k = map(int, input().split())
# result = 0

# while True:
#     target = (n % k)
#     result += target
#     n -= target
#     # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
#     if n < k:
#         break
#     # k로 나누기
#     result += 1
#     n //= k
  
# print(result + (n - 1))

# def solution(x, y, z):
#     # Write your code here
#     k = [x]
#     for i in range(z, 0, - 1):
#         if x - i < y:
#             x += 1
#         else:
#             x -= 1
#         k.append(x)
#     if x != y:
#         return  -1
#     return max(k)
# def solution(box):
#     # Write your code here
#     if box[0] > max(box[1:len(box) - 1]):
#         return box[0]
#     else:
    
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



# import re

# # 앉을 수 있는 자리인지 체크
# def family_check(array, start, end):
#     for i in range(start, end + 1):
#         if array[i] == 1:
#             return False
#     return True

# def solution(N, S):
#     # 앉은 자리는 1
#     # 빈 자리는 0
#     labels = []
#     answer = 0
#     for i in range(0, N):
#         labels.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#     if S != "":
#         for i in S.split(" "):
#             # 숫자만 분리
#             numbers = re.findall('\d', i)
#             labels[int(numbers[0]) - 1][ord(i[-1]) - 65] = 1
          
#     for label in labels:
#         # 왼쪽에 통로를 끼고 앉을 수 있는 경우
#         left = family_check(label, 1, 4)
#         # 가운데 앉을 수 있는 경우
#         middle = family_check(label, 3, 6)
#         # 오른쪽에 앉을 수 있는 경우
#         right = family_check(label,5, 8)
#         family_check_array = [left, middle, right]
#         # 만약 전부 앉을 수 있다면 2가지가 최대의 경우
#         if False not in family_check_array:
#             answer += 2
#         # 만약 한자리라도 앉을 수 있다면 최대의 경우
#         elif family_check_array.count(False) != 3:
#             answer += 1
#     return answer

# print(solution(22, "1A 3C 2B 20G 5A"))

# a = [[1, 2], [2, 3], [4, 1], [4, 3], [3, 1]]
# if [1, 2] in a:
#     print("gd")

# def solution(N, A, B):
#     # write your code in Python 3.8.10
#     routes = []
#     for i in range(0, len(A)):
#         routes.append([A[i], B[i]])
#     for i in range(1, N):
#         if [i, i + 1] not in routes and [i + 1, i] not in routes:
#             return False
#     return True
        

# print(solution(3, [2,4,5,3], [3,5,6,4]))

# # 방향 바꾸기
# def vector_change(s, vector_index):
#     # 방향에 따른 vector_index 회전
#     if s == "right":
#         vector_index += 1
#     else:
#         vector_index -= 1

#     # 회전 후 배열 범위 벗어나면 초기화
#     if vector_index < 0:
#         vector_index = 3
#     elif vector_index > 3:
#         vector_index = 0
#     # 방향 리턴
#     return vector_index

# def solution(office, r, c, move):
#     dx = [-1, 0, 1, 0]
#     dy = [0, 1, 0, -1]
#     vector_index = 0
#     # 시작 지점의 먼지의 갯수를 미리 더함
#     answer = office[r][c]
#     office[r][c] = 0
#     for m in move:
#         if m != "go":
#             vector_index = vector_change(m, vector_index)
#         else:
#             dr = r + dx[vector_index]
#             dc = c + dy[vector_index]
#             if dr < 0 or dr > len(office) or dc < 0 or dc > len(office[0]) or office[dr][dc] == -1:
#                 continue
#             answer += office[dr][dc]
#             office[dr][dc] = 0
#             r = dr
#             c = dc
#     return answer
        

# print(solution([[5,-1,3], [6, 4, -1], [3, -1, 3]], 1, 0, ["go", "go", "right", "go", "right", "go", "left", "go"]))

def solution(survey, choices):
    answer = ''
    arr = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            arr[survey[i][1]] += (choices[i] - 4)
        else:
            arr[survey[i][0]] += (4 - choices[i])
    li = list(arr.items())
    for i in range(0, 8, 2):
        if li[i][1] > li[i + 1][1]:
            answer += li[i][0]
        elif li[i][1] < li[i + 1][1]:
            answer += li[i + 1][0]
        else:
            answer += li[i][0]
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
