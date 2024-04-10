# 1개 or 2개 오름
# 연속 3개 못 밟음
# 마지막 밟기

# 맨뒤에서부터 or 완전 탐색
# 2) 완전탐색 bfs나 dfs로 1이나 2칸씩 넣기
# <-> 작은 문제로 나눠서 해당지점까지 최대값인 걸로 하기에는 해당 지점을 안 밟을 수 있음-> 모든 지점마다 업데이트? 이전 두칸 ,1칸값 이용?
#     : 경우의 수 다 저장보다는 각 지점까지의 max값을 이용해서 다음 값 구하는 게 낫겠다.
# import sys
# n=int(input())
# amap=[int(sys.stdin.readline()) for _ in range(n)]
# print(amap)

# if n<=2: 
#     print(sum(amap))
#     exit()

# max_list=[0 for _ in range(n)]
# max_list[0]=amap[0]
# max_list[1]=sum(amap[0:2])

# for i in range(3,n):
#     # 나를 밟는다는 가정에서의 max_list
#     # i) 안밟는 애가 -2전 ii) -1전 #어차피 최대 2개오름 <---#X_ 어차피 나는 밟는 거면 그 이전 두개는
#     max_list[i]=max(max_list[i-2]+amap[i],max_list[i-1]+amap[i]) 
    
# print(max_list[-1])

#from collections import deque
#if 1:
#    max=0
#    queue=deque([v])# 1
#    # visited은 뒤로만 가니까 필요없음
#
#    while(1):
#    for i in range(2):
#        v=queue.popleft()#
#        nv=v+
#        while(queue):
#            #3

# bfs([0])
# 가장 적은점수의 계단을 안밟는 걸로고르기
# - 35m -> 다른사람 코드 
#   + 35m : 중간에 다른 방법으로 풀었을 때 연속 3개 빼먹은 상태
#   + 시간 효율을 위해 난이도 낮은 건 일정 시간 경과 후 답보기 
# 

# - 파이썬_재귀 함수의 개수 제한은? [Chat GPT : 약 1000번]

### 2.6 다이나믹 프로그래밍[https://www.youtube.com/watch?v=rWbjQphRE9A&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=28]
# - 사용 조건 ~~ 점화식
#   + (1)  최적 부분 구조 : 큰 문제를 작은 문제로 나눠서 해결할 수 있음
#   + (2) '중복되는 부분' 문제 : 동일한 작은 문제를 반복적으로 해결해야 함 / Ex. 피보나치에서 2번째 값 계속 쓰이기 
#   +  DP VS 퀵정렬_분할정복
#     - 분할정복 : 조건 (2) 없음 : 피봇 5가 분리 되면 그 5는 더이상 안쓰임

# - 다이나믹 프로그래밍 문제에 접근하는 방법
#   + 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요합니다.
#   + ***가장 먼저 그리디, 구현, 완전 탐색*** 등으로 해결 가능 한지
#     -> **다른 알고리즘 풀이 방법이 떠오르지 않으면*** ->  다이나믹 프로그래밍을 고려
#   + 음 :  일단 ***재귀 함수로 비효율적인 완전 탐색*** 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이 큰
# 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있습니다.
#   + 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제되는 경우가 많습니다.

# - 여러번 호출(비효율) -> DP조건 만족

# - (M1) 상향식 : DP보통.   |  for
#   > 결과 저장용 리스트 : DP테이블

# - (M2) 하향식 : 메모이제이션, 캐싱 | 재귀 함수 내 메모이제이션


# - 다른 사람 코드[https://v3.leedo.me/devs/64]

import sys
input = sys.stdin.readline
n = int(input())

# 계단의 숫자를 초기화 합니다. 1층은 1번째(not 0번째) 인덱스에 저장합니다.
stairs = [0] * 301
for i in range(1, n + 1):
    stairs[i] = int(input())

# dp 배열을 초기화합니다.
dp = [0] * 301
dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]
dp[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

# 점화식을 계산합니다.
for i in range(4, n + 1):
    # - i-1만 안하고 i-3도 하는 이유 : "안 밟는 것"이 [3개 연속을 피하기위해] 각 경우의 수에서 무조건 포함된 식이어야함.  # X_dp[i] = max(dp[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])
    
print(dp[n])

 
