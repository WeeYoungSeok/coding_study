# BFS
# 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드에부터 우선적으로 탐색하는 알고리즘이다.
# 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같다.
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 규에 삽입하고 방문 처리한다.
# 3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

# BFS는 보통 최단 거리일때 많이 사용하며 queue를 이용하여 while문으로 푼다.

from collections import deque

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 사용
    queue = deque([start])
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end="")
        for i in graph[v]:
            # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 미로 탈출
from collections import deque

n, m = map(int, input().split())

miro_array = []

for _ in range(n):
    miro_array.append(list(map(int, input())))

def miro(x, y):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        # 4가지 뱡향 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if miro_array[nx][ny] == 0:
                continue
            if miro_array[nx][ny] == 1:
                miro_array[nx][ny] = miro_array[x][y] + 1
                queue.append((nx, ny))
    return miro_array[n -1][m -1]
  
# 이동 방향 상, 하, 좌, 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

print(miro(0, 0))