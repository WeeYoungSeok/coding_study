#### 알고리즘 설계 Tip
- C언어를 기준으로 통상 1 ~ 3초 가량의 시간이 소요됩니다.
- pythod을 기준으로 통상 5 ~ 15초 가량의 시간이 소요됩니다.
  - PyPy의 경우 때때로 C언어보다도 빠르게 동작하기도 합니다.
- O(N^3)의 알고리즘을 설계한 경우, N의 값이 5000이 넘는다면 얼마나 걸릴까요?
- 코딩 테스트 문제에서 시간제한은 통상 1 ~ 5초 가량이라는 점에 유의하세요.
  - 혹여 문제에 명시되어 있지 않은 경우 대략 5초 정도라고 생각하고 문제를 푸는 것이 합리적입니다.

- 파이썬이 대략 1초에 2000만번정도 계산한다고 가정하고 문제를 푸는 것을 추천합니다.
  - 5000개의 데이터를 O(N^3)으로 알고리즘을 설계하면 엄청나게 많은 시간이 소요되게 됩니다.
<br/>
#### 요구사항에 따라 적절한 알고리즘 설계하기
- 문제에서 가장 먼저 확인해야 하는 내용은 시간제한(수행시간 요구사항)입니다.
- 시간제한이 1초인 문제를 만났을 때, 일반적인 기준은 다음과 같습니다.
  - N의 범위가 500인 경우 : 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 풀 수 있씁니다.
  - N의 범위가 2000인 경우 : 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 풀 수 있씁니다.
  - N의 범위가 100000인 경우 : 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 풀 수 있씁니다.
  - N의 범위가 10000000인 경우 : 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 풀 수 있씁니다.
<br/>
#### 알고리즘 문제 해결 과정
- 일반적인 알고리즘 문제 해결 과정은 다음과 같습니다.
  1. 지문 읽기 및 컴퓨터적 사고
  2. 요구사항(복잡도) 분석
  3. 문제 해결을 위한 아이디어 찾기
  4. 소스코드 설계 및 코딩
- 일반적으로 대부분의 문제 출제자들은 핵심 아이디어를 캐치한다면, 간결하게 소스코드를 작성할 수 있는 형태로 문제를 출제합니다.