# 큐
# 먼저 들어 온 데이터가 먼저 나가는 형식(선입선출)의 자료구조
# 큐는 입구와 출구가 모두 뚫려 있는 터널과 같은 형태

# 파이썬에서 큐 형태의 문제는 deque을 이용하는게 시간 복잡도가 훨씬 좋다.

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 원소부터 출력