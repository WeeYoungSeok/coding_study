# 리스트와 유사
# 튜플은 한 번 선언된 값을 변경할 수 없다.
# 리스트는 대괄호를 이용하지만, 튜플은 소괄호를 이용한다.
# 튜플은 리스트에 비해 상대적으로 공간 효율적이다.

# 튜플 초기화는 소괄호로
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 네 번쨰 원소만 출력
print(a[3])

# 두 번째 원소부터 네 번째 원소까지
print(a[1 : 4])

# 튜플은 원소 할당 에러 발생
a[2] = 7

# 튜플을 사용하면 좋은 경우

# 서로 다른 성질의 데이터를 묶어서 관리해야 할 때
# 최단 경로 알고리즘에서는 (비용을 실수값으로, 노드번호를 정수로 저장할때)의 형태로 튜플 자료형을 자주 사용한다.
# 데이터의 나열을 해싱의 키 값으로 사용해야 할 때
# 튜플은 변경이 불가능하므로 리스트와 다르게 키 값으로 사용될 수 있습니다.
# 리스트보다 메모리를 효율적으로 사용해야 할 떄