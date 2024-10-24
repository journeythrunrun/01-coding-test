# 1) 
# 3xN를 2x1, 1x2로 채우는 경우의 수 

# 2) N=30 -> O(n^4)~~O(2^n)
# - 2-2) 특출난 값
# m1) 완전탐색 or backtracking : 0,0부터 시작해서, 방문 안한 곳들끼리에서 우측으로 가거나 아래로 가거나
# m2) &최적해
# -> 3이라 한 행 이상은 무조건 옆임. 
# -> 불가능한 경우 0 출력 : N이 2의 배수가 아님
# -> 세로 : 0개,2,4
## 3행 중에 1행씩 일단 선택 X_ 연달은 가로냐에 따라 상황다름

# 간단한 예시 N=2 -> 4 -> 오 이걸 dp로
# m3) dp
# 0) dp[i]정의 : N=i일 때 최대가질 수 있는 값
# 0) 경로 누적 +가능한 len(가능한경로들)
# for for : for dx dy : if not visited[] and not visited[] : 

 
# - 백트래킹하던거
# answer=0
# def backtrack (forced_index, direction, visited)
#     if forced_index==len(visited[0])*len(visited)-1:
#         answr+=1

# N=int(input())
# if N%2==1:
#     print(0,end='')
# else :  # 백 트래킹
#     for i in range()
#         backtrack(i,1,visited)# 1차원화 인덱스_행인덱스*가로길이+열인덱스,방향_가로0세로1,visited상태 
#         backtrack(i,0,visited)# 1차원화 인덱스_행인덱스*가로길이+열인덱스,방향_가로0세로1,visited상태 
# 4) N=1,
# - 4-2) 다 못하는 경우


# - 40m 초과 : 골드4네
#   > 가장 어려워보이는 문제집의 마지막 문제로 고르긴 했는데 그래도 DP 완벽 체환 안된거네(DP쉬운문제로 나온다긴하지만)

# - 다른 사람 풀이[https://jyeonnyang2.tistory.com/51#google_vignette]
#   + m3) dp 정의까진 맞았음. dp큰 틀은 맞았고 그 세부에서 최적해 구하는 방법을 심도 있게 시간 썼어야함. 큰 틀에서 틀렸거나 큰 틀에서 다른 방법을 찾아야했던 건 아님
#   + 행이 [3으로 매우 작어서], 수기 경우의 수가 매우 제한됨 -> 손으로 그리며 경우의 수 따져봐야 알 수 있는 세부 최적해
#   + [DP] : [점화식_이 가능할 거라 생각하고 전개하기] 수기 초반 케이스부터  전개하며 찾아야할 수도 있음
n = int(input())
dp = [0 for _ in range(31)]
dp[2] = 3
for i in range(4,n+1) :
    if i%2 == 0 :
        dp[i] = dp[i-2] * 3 + sum(dp[:i-2]) * 2 + 2 ##그림 태블릿켈린더 
        # - => i)마지막 두줄 안 가로지르는 경우 dp[i-2]xdp[2] + ii) 가로지른는경우  sum(dp[:i-2])
        #   + [점화식] 2열 잘라서 동일한 문제로 쪼갤 수 있지. 경우의 수 나눠서 동일한 모양꼴 나오게 할 수 있음 
    else :
        dp[i] = 0
print(dp[n])

