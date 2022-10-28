# 시간 복잡도 O(N)
array = [3, 5, 1, 2, 4] # 5개의 데이터 (N = 5)
summary = 0 # 합계를 저장하는 변수

# 모든 데이터를 하나씩 확인하며 합계를 계산
for x in array:
    summary += x

# 결과 출력
print(summary)

# 시간 복잡도 O(N^2)
array = [3, 5, 1, 2, 4]

for i in array:
    for j in array:
        temp = i * j
        print(temp)
# 주의 : 모든 2중 반복문의 시간 복잡도가 O(N^2)인 것은 아니다.
# 소스코드가 내부적으로 다른 함수를 호출한다면 그 함수의 시간 복잡도 까지 고려해야하기 때문이다.

# 소스코드 시간 구하기
import time
start_time = time.time()

# 프로그램 소스코드
end_time = time.time()
print("time : ", end_time - start_time)