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

# + 첫Pi를 dp값초기화로?
#~ 미리 0으로 하면 중간인 케이스에서도 안되긴 하는데, 애초에 마지막도 안되는 경우면 중간도 안되는 거라 그게 맞음
# 그 값을 array로는 더해도 되는 건지
# <->걍!! 나중에 뺴기 
dp=[ array[i][1] if n>=i+array[i][0] else 0 for i in range( len(array) )]
# print(dp)
for i in range(1,len(array)): # 첫놈은 앞놈이 없어서, 굳이 dp에 이전꺼 더하는거 할필요 없음 
    if dp[i]==0: # 마지막이 이거인걸로 못끝남
        continue
    for j in range( i): # i-1 # 0은 굳이 안 써도
        if i>=j+array[j][0] :#_3조건만족# 이전꺼 할 수 있는지
            dp[i]= max(dp[i], dp[j]+array[i][1]) 
    # print(dp)
print(max(dp), end='')
# + j<i : dp[i]= max(dp[i]_1일과4일일지 2일과 4일일지 for돌며 누적max검사, dp[j]+array[i][1]) 
# + max(dp)

#~ 키보드 가져와서 무릎위에 두고할까

# 4) N=1,..15
# Ti,Pi 1,..

# - 39m

#~ 0인결과 출력 가능. max가 0이라