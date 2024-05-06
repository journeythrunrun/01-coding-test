# 0) 3 10(최대 1000), 
# 1) N+1퇴사
# ti-1개를 못하게됨
# [] 구간
# -> 최대수익
# 2) 시간복잡도 널널
# 완전탐색 -> [ti일 후:]부터 상담_ 가능한 세트->
# ! 각 상담 일 선택시 그 후 가능한 바로 다음 타겟 따로 저장 & 그거 이후 for 이용

# dp bfs로도

# - dp 빠르게 학습할 생각으로 19m풀다가 정답봄[이것이 코딩테스트다 깃허브]
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i ## time : 상담이 끝나는
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value
print(max_value)

# 이전 다른 방법
# import sys
# input=sys.stdin.readline

# n=int(input())
# data=[list(map(int,input().split())) for _ in range(n)]
# after_target=[ i+data[i][0] for i in range(n)] # <->이후들도 다 저장할까

# print(after_target)
# answer=0
# for i in range(n): # 첫 시작 대상
#     first=after_target[i]  # after_target에서 가져온 한 리스트의 순서대로 빼면서 쓰기 bfs유사
#     asum=first[1]
    
#     # 재귀 대신 for : 저장
#     while(1) :# 다음타겟인덱스가 n 이상이면 탈출 
#         for _ in af

#     for 








