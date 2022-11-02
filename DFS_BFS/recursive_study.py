# 재귀 함수란 자기 자신을 다시 호출하는 함수

# 재귀 함수는 끝내는 조건을 꼭 넣어주어야 한다.

def recursive_function():
    print("재귀 함수를 호출합니다.")
    recursice_function()

recursive_function()

# 종료 조건을 포함한 재귀 함수 예제
def recursive_function(i):
    if i == 100:
        return
    print(1, "번째 재귀함수에서", i + 1, "번째 재귀함수를 호출합니다.")
    recursive_funtion(i + 1)
    print(i, "번째 재귀함수를 종료합니다.")

# 100번째가 되면 함수가 종료되고 가장 마지막에 불렀던 재귀함수부터 종료된다.

# 팩토리얼 구현

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n + 1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1:
        return
    return n * factorial_recursive(n - 1)

print("반복적으로 구현 :", factorial_iterative(5))
print("재귀적으로 구현 :", factorial_recursive(5))

# 유클리드 호재법

# 두 자연수 A, B에 대하여 (A > B) A를 B로 나눈 나머지를 R이라고 하자
# 이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같다

def recursive_gcd(a, b):
    if a % b == 0:
        return b
    return recursive_gcd(b, a % b)
print(recursive_gcd(192, 162))

# 유의 사항
# 재귀 함수를 잘 활용하면 복잡한 알고리즘을 간결하게 작성할 수 있다.
# 단, 오히려 다른 사람이 이해하기 어려운 형태의 코드가 될 수도 있으므로 신중하게 사용해야 한다.
# 모든 재귀 함수는 반복문을 이용하여 동일한 기능을 구현할 수 있다.
# 재귀 함수가 반복문보다 유리한 경우도 있고 불리한 경우도 있다.
# 컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓인다.
# 그래서 스택을 사용해야 할 때 구현상 스택 라이브러리 대신에 재귀 함수를 이용하는 경우가 많다.

