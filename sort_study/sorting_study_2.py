# 이진 탐색 알고리즘
# 순차 탐색 : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
# 이진 탐색 : '정렬되어 있는 리스트'에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
# 이진 탐색은 시작점, 끝점, 중간점을 이용하며 탐색 범위를 설정

# 4 찾기
array = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# 시작점 0, 끝점 9, 중간점 4

# 중간점 = (시작점 + 끝점) // 2

# 중간점이 2개 존재할 경우 소수점 이하는 제거해서 작은 인덱스 선택
# 중간점을 기준으로 찾아야하는 값과 비교할 때 중간점이 찾는값보다 크다면 중간점을 기준으로 오른쪽의 데이터는 전부 필요가 없어진다.

# 다시 탐색할떄 시작점은 그대로 끝점은 아까의 중간점 인덱스에서 -1을 한 기준으로 다시 절반을 자른다.
# 시작점 0, 끝점 3, 중간점 1
# 이번에는 중간점값이 찾고자하는 값보다 더 작기떄문에 왼쪽 값들은 필요가 없어진다.
# 시작점은 중간점 인덱스 + 1을 해주고
# 끝점은 그대로 고정한다.

# 시작점 2, 끝점 3, 중간점 2
# 중간점의 값이 찾고자하는 값과 같기 때문에 알고리즘이 종료된다. (찾고자하는 값이 존재하는 지와 인덱스도 알 수 있다.)

# 단계마다 탐색 범위를 2로 나누는 것과 동일하므로 연산 횟수는 log2N에 비례한다 (log의 밑이 2인 로그이다)
# 예를 들어 초기 데이터가 개수가 32개일 떄, 이상적으로 1단계를 거치면 16개가량의 데이터만 남는다.
# 2단계 이후 8개
# 3단계 이후 4개
# 다시 말해 이진 탐색은 탐색 범위를 절반씩 줄이며, 시간 복잡도는 O(logN)을 보장한다.

# 재귀적 구현 (이진탐색)
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# 반복문 구현
def binary_search1(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n(원속의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1) # 몇번째 존재하는지

# 파이썬의 이진 탐색 라이브러리
# biset_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 사입할 가장 왼쪽 인덱스를 반환
# biset_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))

# 라이브러리 활용
# 값이 특정 범위에 속하는 데이터 개수 구하기

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 배열 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # 2 출력 4 4

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3)) # 6 출력 1 2 3 3 3 3 


# 파라메트릭 서치
# 최적화 문제를 결정 문제('예' 혹은 '아니오')로 바꾸어 해결하는 기법
# 최적화 문제 : 어떤 함수의 값을 가능한 낮추거나, 최대한 높이거나 하는 문제
# 예시 : 특정 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
# 일반적으로 코딩 테스트에서 파라메ㅐ트릭 서치 문제는 이진 탐색을 이용하여 해결 가능하다.

# 떡볶이 떡 만들기
# 절단기를 높이면 높일수록 잘린떡의 길이는 줄어들고
# 절단기를 낮추면 낮출수록 잘린떡의 길이는 길어진다.
# 현재 이 높이로 자르면 조건을 만족할 수 있는가?를 확인한 뒤에 조건의 만족 여부('예' 혹은 '아니오')에 따라서 탐색 범위를 좁혀서 해결할 수 있다. (만약 M만큼의 떡을 가질 수 없다면 절단기를 더 줄이면 된다.)
# 절단기의 높이는 0부터 10억까지의 정수 중 하나이다.
# ***이렇게 큰 탐색 범위를 보면 가장 먼저 이진 탐색을 떠올려야한다***

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

# 가장 긴 떡의 길이가 끝점이 된다
# 시작점 0, 끝점 가장 긴 떡의 길이, 중간점 두개 더해서 나눈것
# 중간점이 높이에 해당됨
# 그 높이로 잘랐을 때 원하는 떡의 길이보다 크면 저장하고 시작점을 중간점의 + 1로 바꾸어준다.
# 만약 원하는 떡의 길이보다 작다면 저장하지 않고 시작점은 그대로 끝점은 중간점의 -1로 바꾸어준다.
start = 0
end = max(array)
result = 0
while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in array:
        # 잘랐을 때의 떡의 양 계싼
        if i > mid:
            count += (i - mid) 
    # 떡의 양이 부족한 경우 더 많이 잘랴아하므로 저장 안하고 왼쪽 부분 탐색
    if count < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기 오른쪽 부분 탐색
    else:
        start = mid + 1
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
print(result)

# 정렬된 배열에서 특정 수의 개수 구하기
n, x = map(int, input().split())
array = list(map(int, input().split()))

from bisect import bisect_left, bisect_right
count = bisect_right(array, x) - bisect_left(array, x)
if count == 0:
    print(-1)
else:
    print(count)

# 이진 탐색으로 풀기
# 이코테에 나와있음 찾아보고 구현해보자.
