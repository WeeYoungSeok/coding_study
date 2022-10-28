# 사전 자료형

# 키와 값의 쌍을 데이터로 가지는 자료형
# 앞숴 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과는 대비된다.

# 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 '변경 불가능한 자료형'을 키로 사용할 수 있습니다.

# 파이썬의 사전 자료형은 해시 테이블을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있습니다.

data = dict()
data['사과'] = "Apple"
data['바나나'] = "Banana"
data['코코넛'] = "Coconut"

print(data)

# 사과라는 키 존재 여부 확인
# print구문 실행됨
if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 키 데이터만 뽑고자 한다면 keys() 함수 사용 가능
# 값 데이터만 뽑고자 한다면 values() 함수 사용 가능
key_list = data.keys()
value_list = data.values()

print(key_list)
print(value_list)

for key in key_list:
    print(data[key])

