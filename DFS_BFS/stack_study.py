# 스택
# 먼저 들어 온 데이터가 나중에 나가는 형식(선입후출)의 자료구조
# 입구와 출구가 동일한 형태로 스택을 시각화할 수 있음

stack = []

# append, pop은 시간 복잡도가 상수시간
stack.appned(5)
stack.appned(2)
stack.appned(3)
stack.appned(7)
stack.pop()
stack.appned(1)
stack.appned(4)
stack.appned(5)
stack.pop()

print(stack[::-1]) # 최상단 원소부터 출력
print(stack) # 최하단 원소부터 출력