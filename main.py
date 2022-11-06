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


# 보텀업
n = int(input())
k = list(map(int, input().split()))

# N은 최대 100이므로 앞서 계산된 결과를 저장하기 위한 DB 테이블 초기화
d = [0] * 100

# 보텀업 진행
d[0] = k[0]
d[1] = max(k[0], k[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])