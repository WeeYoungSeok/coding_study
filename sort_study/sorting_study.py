# 정렬이란 데이터를 특정한 기준에 따라 순서대로 나열하는 것을 말합니다.
# 일반적으로 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됩니다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 선택 정렬
# 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

# 선택 정렬의 시간 복잡도
# N번 만큼 가장 작은 수를 찾아서 맨 앞으로 보내야 한다.
# 구현 방식에 따라서 사소한 오차는 있을 수 있지만, 전체 연산 횟수는 다음과 같다
# N + (N - 1) + (n - 2) + ... + 2
# 이는 등차수열 공식으로 (N^2 + N - 2) / 2 로 표현할 수 있는데, 빅오 표기법에 따라 O(N^2)이라고 작성한다.

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프
print(array)

# 삽입 정렬
# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입합니다.
# 선택 정렬에 비해 구현 난이도가 높은 편이지만, 일반적으로 더 효율적으로 동작한다.

# 삽입 정렬의 시간 복잡도
# O(N^2)이며, 선택 정렬과 마찬가지로 반복문이 두 번 중첩되어 사용된다.
# 삽입 정렬은 현재 리스트의 데이터가 거의 정렬되어 있는 상태라면 매우 빠르게 동작한다.
# 최선의 경우 O(N)의 시간 복잡도를 가진다.
# 이미 정렬되어 있는 상태에서 다시 삽업 정렬을 수행하면 N번만 돌고 만다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)

# 퀵 정렬
# 기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법이다.
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나이다.
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘이다. (파이썬, 자바, c의 기본 정렬 라이브러리도 퀵정렬, 병합정렬의 아이디어를 채택한 하이브리드 정렬 라이브러리이다.)
# 가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)로 설정한다.

# 왼쪽에서는 pivot보다 큰 데이터를 고르고 오른쪽에서는 pivot보다 작은 데이터를 고른다.
# 그리고 큰 데이터와 작은 데이터의 위치를 바꾸어준다.
# 왼쪽에서의 데이터와 오른쪽에서 데이터가 엇갈리는 순간 작은 데이터와 pivot값의 자리를 바꾸어준다.
# 그렇게 되면 pivot 기준으로 왼쪽은 pivot보다 작은 데이터 오른쪽은 큰 데이터다 (분할이라고 한다.)

# 다시 pivot값을 기준으로 왼쪽과 오른쪽을 배열로 판단해서 다시 왼쪽 배열과 오른쪽 배열에서 각 퀵정렬을 수행한다.

# 퀵 정렬의 시간 복잡도는 평균의 경우 O(NlogN)이다.
# 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가진다.
# 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면 N^2이 된다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1 # 왼쪽에서 시작
    right = end # 오른쪽에서 시작
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 떄까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 큰 데이터와 작은 데이터 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

# 파이썬의 장점을 살린 퀵 정렬
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort1(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort1(left_side) + [pivot] + quick_sort1(right_side)

print(quick_sort1(array))

# 계수 정렬
# 특정한 조건이 부합할 떄만 사용할 수 있지만 매우 빠르게 동작한다.
# 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 떄 최악의 경우에도 수행 시간 O(N + K)를 보장한다.

# 데이터의 범위가 정해졌다면
# 가장 작은 데이터부터 가장 큰 데이터까지 모두 담길 수 있도록 리스트를 미리 생선한다. (인덱스가 각 원소(값)을 의미하고 해당 인덱스의 값은 해당 원소가 몇번 나타났는지(count)의 값을 의미한다.)

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

count_array = [0] * (max(array) + 1)

for i in array:
    count_array[i] += 1

for i in range(len(count_array)): # - k만큼
    for j in range(count_array[i]): # - 최대 N개의 만큼
        print(i, end= " ")

# 공간 복잠도 또한 O(N + K)
# 계수 정렬은 떄에 따라서 심각한 비효율성을 초래할 수 있습니다.
# 데이터가 0과 999,999로 단 2개만 존재하는 경우를 생각 해보자 - 이렇게 될 경우 미리 데이터를 0부터 999,999인 100만개의 데이터를 만들어야 한다. 그래서 비효율적이다. (0번지와 999,999번지 제외하고는 필요가 없는 공간)
# 계수 정렬은 동일한 값을 가지는 데이터가 여러 개 등장할떄 효과적으로 사용할 수 있다.
# 설적의 경우 100점을 맞은 학생이 여러 명일 수 있기 때문에 계수 정렬이 효과적이다.

# 정렬 알고리즘 비교하기

# 선택 정렬 
# 시간 복잡도 : O(N^2)
# 공간 복잡도 : O(N)
# 특징 : 아이디어가 매우 간단하다.

# 삽입 정렬
# 시간 복잡도 : O(N^2)
# 공강 복잡도 : O(N)
# 특징 : 데이터가 거의 정렬되어 있을 떄는 가장 빠르다. (O(N)으로 준다.)

# 퀵 정렬
# 시간 복잡도 : O(NlogN)
# 공간 복잡도 : O(N)
# 특징 : 대부분의 경우에 가장 적합하며, 충분히 빠르다. (최악의 경우 O(N^2)으로 시간 복잡도가 는다.)

# 계수 정렬
# 시간 복잡도 : O(N + K)
# 공간 복잡도 : O(N + K)
# 특징 : 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다.

# 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있다.
# 고로 코딩테스트에서 별도의 정렬 알고리즘을 직접 코드로 구현하라고 명시되어있지 않는이상 표준 라이브러리를 사용하는 것을 추천한다.
# 하지만 표준 라이브러리로 시간 초과가 뜨는 문제들은 해당 문제에 맞는 적절한 정렬 알고리즘을 직접 구현해야한다.

# 두 배열의 원소 교체
# 내 풀이
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 바꿔줄 필요가 없음 반복문 탈출
        break

print(sum(a))

# 핵심 아이디어 : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
# 가장 먼저 배열 A와 B가 주어지면 A에 대하여 오름차순 정렬하고, B에 대하여 내림차순 정렬한다.
# 이후에 두 배열의 원소를 첫 번째 인덱스부터 차례대로 확인하면서 A의 원소가 B의 원소보다 작을 때에만 교체 수행
# 이 문제에서는 두 배열의 우너소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 한다.

# 이코테 풀이
# 같음
