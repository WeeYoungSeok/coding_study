# 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
# 파이썬 프로그램을 작성할 떄 없어서는 안 되는 필수적인 기능

# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능
# 특히 순열과 조합 라이브러리라는 코딩 테스트(완전 탐색)에서 자주 사용

# heepq : 힙(Heap) 자료구조를 제공
# 일반적으로 우선순위 큐 기능을 구현하기 위해 사용

# bisect : 이진 탐색 기능을 제공

# collections : 덱, 카운터 등의 유용한 자료구조를 포함

# math : 필수적인 수학적 기능을 제공
# 팩토리얼, 제곱근, 최대공약수, 삼각함수 관련 함수부터 파이같은 상수를 포함

# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], resverse = True)
print(result)
print(reverse_result)

# sorted(), with key
array = [("홍길동", 35), ("이순신", 75), ("아무개", 50)]
result = sorted(array, key=lambda x: x[1], reverse = True)
print(result)

# 순열과 조합
# 모든 경우의 수를 고려해야 할 때 어떤 라이브러리를 효과적으로 사용할까?
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
# {'A', 'B', 'C'}에서 세 개를 선택하여 나열 : ABC, ACB, BAC, BCA, CAB, CBA

# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
# {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : AB, BC, AC

# 미리 경우의 수를 파악
# 순열 공식 nPr = n * (n -1) * (n - 2) * ... * (n - r + 1)
# 조합 공식 nCr = n * (n - 1) * (n - 2) * ... * (n - r + 1) / r!

from itertools import permutations

data = ["A", "B", "C"]
result = list(permutations(data, 3))
print(result)

from itertools import combinations
result = list(combinations(data, 2))
print(result)

# 중복 순열, 중복 조합
from itertools import product
result = list(product(data, repeat=2))
print(result)

from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)

# Counter
# 등장 횟수
# 리스트와 같은 반복 가능한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지 알려준다.
from collections import Counter

counter = Counter(["red", "blue", "red", "green", "blue", "blue"])

print(counter["blue"]) # blue 등장 횟수
print(counter["green"])
print(dict(counter)) # 사전 자료형으로 변환

# math
# 최대 공약수, 최소 공배수

import math

# 최소 공배수를 구하는 함수
def lcm(a, b):
    return a * b // math.acd(a, b)

a = 21
b = 14

# 최대 공약수(GCD)
print(math.gcd(a, b))
# 최소 공배수(LCM)
print(lcm(a, b))