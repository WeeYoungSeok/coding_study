i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1
print(result)

# 홀수만 더하기
i = 1
result = 0

while i <= 9:
    if i % 2 != 0:
        result += 1
    i += 1
print(result)

# break
i = 0

while True:
  print("현재의 값 :", i)
  if i == 5:
      break
  i += 1