# 오른쪽, 아래쪽으로만 움직여서 -> 최단경로의 개수 % 1000000007
# m이 열 n이 행 # N=만 -> O(n log n), n^2아슬

# map만들고  ->
# dp_ 각 map 위치에 최소인 . set
# bfs _ 그 같은 자식들 수 
# (오른쪽이랑 아래쪽으로만 움직여서 가능한 방법)어디서 내려오느냐로 카운팅 & 물웅덩이 개수로 빼서 최적화
from collections import deque
def solution(m, n, puddles):
    if  len(puddles[0])==0:
        return 1
    ##(n-1)*m# 각 행에서 m개의 열 중에 1개. 행은 1개 빼야함(내려가서 도착하는 위치기준으로 카운팅이기에.)
    # & 단순 m곱하기에는 아래층의 왼쪽에 있는건 못골라서 나머지 열개수에서 골라야함 
    # 근데 물웅덩이가 끝에 있느냐에 따라서 
    
    # 2) -1웅덩이 반영된 map저장. values_map거치며 숫자 저장해나가기. 이전값*
    # 2) 걍 빨리 아는 방법 bfs로 map거쳐서 도착할 때마다(dfs방문했던곳도방문하게) 카운팅할래에? 시복 더 안좋 _ dp좀써보자
    # 아래로 갈 수 있을 때 +1한 거 그 위치에 저장 ~~ 아래로 갈때 자신에서 +1하기 . 마지막 위치에 도달했을 때 answer에+=
    
    ## bfs로 미방문만 가면서 저장
    ## 가로 세로 전체로 뒤집어도 결과는 같음.
    # 눈에 보이는 가로 4개를 행이 4개인거라고 치고 하자 (데이터 입력 앞위치가 그거임)
    dr,dc=[1,0],[0,1] # 우측 , 아래
    amap=[ [0]*n for _ in range(m) ]
    visited=[ [False]*n for _ in range(m) ]
    
    dp=[ [0]*n for _ in range(m) ]
    
    for puddle in puddles :
        amap[puddle[0] -1 ][puddle[1] -1 ]=-1 # - 문제 읽을 때 인덱스 -1 미리 적어두자
    
    aque=deque([ [0,0]  ])
    visited[0][0]=True
    dp[0][0]=1
    #~ 방문했던 곳이면 append는 안하고 카운팅만추가..? 그럼 값이 다른데
    
    for r in range(m) :
        for c in range(n ) :
            if amap[r][c]==-1:
                continue
                
            #print(r,c, dp)
            v=[r,c]
            for i in range(2):
                nr, nc = v[0]+dr[i], v[1]+dc[i]
                if 0<=nr<m and 0<=nc<n and amap[nr][nc]!=-1 : # : 코드수정때 그 앞뒤!!꼭123#똑같은 곳 가야하고 뒤로가는거어차피 없어서미방문체크 안해도  visited[nr][nc]==False :
                    if visited[nr][nc]==True : #i==1:## 두번째가 2가아니라 1이지
                        #print( dp[v[0]][v[1]]+1 )
                        dp[nr][nc]+=dp[v[0]][v[1]]#~이상한값을 복사했엇#1# 1이 아니라 현재값.   ##dp[v[0]][v[1]]#+1대신 처음에 초기값이 1인상태로 전파시키는중 # 내려갈 땐 +=는 안해도  
                    else:# 처음방문한 곳이니까! 그래도 이때까지의 값.  
                        dp[nr][nc]+=dp[v[0]][v[1]] # 1이 아니라 현재값. # 꼭 누적
                    visited[nr][nc]=True  
                    # 백트래킹으로 해야하나..
            
    
#     while(aque):
#         #print(dp)
#         v= aque.popleft() 
#         # m 부모의 값을 자식에게 더해줌
#         # 3) x_현재 위치 기준으로 dr의 두방향 다 갈 수 있으면 +1
#         # 라기보다 차라리 방문한곳 또 방문했을 때 거기에 +1 _ 방향특성상돌아가는 건 없다
#         #print(v)
        
#         # 이 방법 조회 순서에 따라#~#~ 중복이 너무 많다. bfs, dfs, 초기에 넣어놓은값 방법 말구 단순 for?
        
#         for i in range(2):
#             nr, nc = v[0]+dr[i], v[1]+dc[i]
#             if 0<=nr<m and 0<=nc<n and amap[nr][nc]!=-1 : # : 코드수정때 그 앞뒤!!꼭123#똑같은 곳 가야하고 뒤로가는거어차피 없어서미방문체크 안해도  visited[nr][nc]==False :
#                 if visited[nr][nc]==True : #i==1:## 두번째가 2가아니라 1이지
#                     #print( dp[v[0]][v[1]]+1 )
#                     dp[nr][nc]+=1##dp[v[0]][v[1]]#+1대신 처음에 초기값이 1인상태로 전파시키는중 # 내려갈 땐 +=는 안해도 
#                 else:
#                     dp[nr][nc]=1#+=dp[v[0]][v[1]] # 꼭 누적
#                 aque.append([nr,nc])
#                 visited[nr][nc]=True                #~ 방문순서와 다르게, 닿는 순서 때문에 여기서 꼭? 
#                 # 기본 pop, append안한거 실화
#     # 22아닌 퍼들값 체크
#     #~aset=set([ [1,2],[1,2],[3,4] ])# 튜플 ㄱㄴ 리스트 ㅂㄱㄴunhashable
#     ##print(aset)
    return dp[-1][-1]% 1000000007
# 4) m, n 1,1아닌 1,k,2
# 물에 잠긴지역 0개일 때 /결과0일떄 완료_중복 물 -> set
#~ 저 값 연산 범위 이려나

# - 59m (생각난 여러 방법 중, 빠르게 한 개 픽하지 않고 여러 방법 이어서 생각하다가 시간 들여진듯. 빨리 확실히 픽하지 못할 각 방법이었을 수도 있긴 함.)

#   + 1h 제한 문제 풀기로 해서(수학문제 처럼 끊는 거 잘 못했는데 보상 거니까 잘되네.), 4) 체크 안하고 제출함
#   + 시간초과 ( 뭔가 잘못된게 있나)
