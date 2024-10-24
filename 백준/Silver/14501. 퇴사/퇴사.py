# N+1일째 퇴사
# 최대한 많은 상담
# 하루에 하나씩 다른 상담

# 2) O(2^n)
# - 최대 수익
# + dp[i]:i가 마지막으로 한 것일 경우의 총 수익 
# + 첫Pi를 dp값초기화로?
# + j<i : dp[i]= max(dp[i]_1일과4일일지 2일과 4일일지 for돌며 누적max검사, dp[j]+array[i][1]) if i>=j_0+array[j][0]_3조건만족# 이전꺼 할 수 있는지
# + max(dp)

# - k일동안 못함
# - 마지막 상담의 N일째 이내에 끝나야함
#   + 초기값 저장 시 : dp
import sys
inpu=sys.stdin.readline
n=int(inpu()) 
array= [list(map(int, inpu().split()) ) for _ in range( n) ]

# - [0)dp정의] dp[i]:i가 [마지막으로 한 것일 경우]의 총 수익의 [최대값]
# - dp값초기화 : 첫Pi &
#   + 마지막에 기간 초과로 못 먹는 거 : 미리 0으로 하면 그게 중간인 케이스에서도 다 0화 안되긴 하는데, 그게 맞음. 애초에 마지막도 안되는 경우면 중간도 안되는 거임
# - 그 값을 array로는 더해도 되는 건지 -> 이런 특정 세부는 논리 생각보다 코딩짜고 디버깅이 더 빨랐음
#   + m2) 걍!! 나중에 빼기 -> if문으로 어차피 못먹는 상담은 continue 
#   + 성공 후 수정 m1) array대신 array이용하여 초기값 저장해줬던 dp[i]는 이미 누적 최대값으로 업데이트 돼있음
dp=[ array[i][1] if n>=i+array[i][0] else 0 for i in range( len(array) )]

for i in range(1,len(array)): # - [1)for 1]첫놈은 앞놈이 없어서, 굳이 dp에 이전꺼 더하는거 할필요 없음 
    if dp[i]==0: # - i번째가 먹을 수 없는 소요기간 놈인 경우 
        continue
    for j in range(i): # - [2)for] # ~i-1
        if i>=j+array[j][0] : # - [3)조건만족 체크]  # - i번째를 마지막으로 먹는 값 저장 때, i보다 작은 j꺼를 먹을 수 있는지(j상담이 i초과해서 끝나면 안됨)
            dp[i]= max(dp[i], dp[j]+array[i][1]) # - [4)max누적] max 때는 여러가지 거쳐가며 max인거 찾는 거라 ㅁ=max(ㅁ_자기자신, ~) ## j<i : dp[i]= max(dp[i]_1일과4일일지 2일과 4일일지 for돌며 누적max검사, dp[j]+array[i][1]) 
print(max(dp), end='')


# 4) N=1,..15
# Ti,Pi 1,..

# - 4-2) 모두 못먹을 수 있을 경우 : ## 0인결과 출력 가능. max가 0이라

# - 39m
#   > 어차피 시간복잡도 이내이길래 저번 문제의 알고리즘 사용. 더 간단한 시복법있음

# - 다른 풀이[taktak33]
#   + (1) for 돌며 끝나는 시간 대의 DP에 값 더해줌 & 다음칸으로씩 DP값 max로 건네줌
'''
N = int(input())
dp = [0] * (N+1) # - dp[i] : i-1때까지 얻을 수 있는 max값 저장해나감.

for i in range(N):
    T, P = map(int,input().split())
    dp[i + 1] = max(dp[i+1],dp[i]) # - ㅁ=max(ㅁ_for돌며 누적, 바로 이전 것) 
    if i + T <= N: # - 마지막으로 받는 게 가능한 범위의 상담이면
        dp[i+T] = max(dp[i+T],dp[i]+P) # - 현재 상담받는 거 DP에 먹이기. 현재 상담 안받는게 나은상황이면 위의 max에서 다른 최대값으로 갱신됨# -  = max(for돌며 최대값 누적되도록 =을 통해 넣어지는 대상이랑 같은값,i의 상담받기)
        # - 상담 안 받는 날은?
print(dp[N])
'''