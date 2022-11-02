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

# dfs 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 0번지는 비워준다.
# 1번 노드의 인접부터 검사하기 때문
# 1번 노드와 인접한 노드는 2, 3, 8이다.
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
    