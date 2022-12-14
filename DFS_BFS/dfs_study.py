# DFS
# 깊이 우선 탐색이라고 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
# DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다.

# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
# 2. 스택 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리, 방문하지 않은 인접 노드가 없다면 스택에서 최상단 노드에서 꺼낸다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.

# dfs는 보통 함수를 여러번 호출하는 방식으로 푼다.

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

# 음료수 얼려먹기
def ice_count(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if ice[x][y] == 0:
        ice[x][y] = 1
        ice_count(x - 1, y)
        ice_count(x, y - 1)
        ice_count(x + 1, y)
        ice_count(x, y + 1)
        return True
    return False

n, m = map(int, input().split())
ice = []

result = 0
for i in range(n):
    ice.append(list(map(int, input())))

for i in range(n):
    for j in range(m):
        if ice_count(i, j) == True:
            result += 1

print(result)