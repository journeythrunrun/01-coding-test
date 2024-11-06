#1)
# - 1년마다 그 칸에 동서남북 네 방향으로 붙어 있는 0이 저장된 칸의 개수만큼 줄어듬



# - 0화. max(0,
# -> 0보다 큰거 targets에 저장. targets(미방문)에서 하나로 bfs&bfs돌며 visited화 : bfs돌고 나왔는데 targets에 미방문_0이 아닌거로 하기엔 다음꺼 하기 위해서 이미 처리한 놈들 0으로 하긴X_ 있으면(굳이 최적화 하기엔 이미 시복이내.) : 해당 년도.
# -> 한덩어리씩 사방 검사 진행(0있으면 자신-1, 자연수이면 위치 append. 사방검사 다 한 후 0보다 크면 다음 targets에 append. ). 다음덩어리로 가면 해당 년도. 

# > 동서남북 연결
# -> 한 덩어리 빙산이 두 덩어리 이상으로 분리되는 최초의 시간 / 다 녹았는데 (없는데)도 안됐으면 0

# 2) n*m=90,000 / 빙산은 만개이하있음 : O(nlogn) #~
# 칸에 들어가는 값 10이하이므로 최대 *10


from collections import deque
import sys # - 
n,m = map( int, sys.stdin.readline().split() )
amap=[ list(  map( int, sys.stdin.readline().split() ) ) for _ in range(n) ]

visited=[ [1]*m for _ in range(n)  ] # 벽 미리 1화
answer=0
dr,dc=[0,0,1,-1],[-1,1,0,0]



def bfs(v, visited, amap):
    q=deque([ v ])
    # n,m
    n=len(visited)
    m=len(visited[0])
    visited[v[0]][v[1]]=1 #,v[1] ]=1
    pass_set=set()
    pass_set.add( v[0] *m + v[1] ) # 괄호  #$ set r*n+c 첨꺼 # n 아니고 m이쥬@!!!!!@!@!@!@!@!@!@! 생각하고 하기
    # 다 풀어져서 넣어지는 게 아니었던 변수형은 
    while(q) :
        r, c = q.popleft()
        for i in range(4) :
            nr, nc= r+dr[i], c+dc[i]

            # 에라이 뒤에도 = 추가해야
            if 0<=nr<= n  -1 and 0<=nc<=len(visited[0])-1 : # 어라 아까랑 똑같은, 오히려 마지막줄 바껴서 아까가 맞네check. 근데 첫빵만 마이너스된거 없어서 그럴수있음# 근데 여기에 visited검사하면 물로 0화되는게 안됨. 물은 재 방문해도 된다니까. 첨에 그래서 없앴던.'그냥 0 말고 이번 턴에 0이하가된 방문애가 문제인거임'  and visited[nr][nc]==0: # 조건 뺄때 : 추가하는 거 주의 : # - and visited[nr][nc]==0 :# 벽의 0도 이용되어야함. # 이 미방문처리는 빙하였던 애들ㅇ에 대해서만임. 0짤말고 # and amap[nr][nc]> # 이미 미방문인 애들만 _ 이라기엔 그 주위보는 건데 amap 다르게 이용
                #if amap[r][c]==7:
                    #print('why', nr, nc, pass_set)
                # - 0에서 주변에 하는 게 효율성 나을 수도 있긴함. 시복 이내 글두
                if amap[nr][nc] <=0 and nr*m+nc not in pass_set  : # pass set 여기 ## 0보다 작으면화
                    amap[r][c]-=1 # max 0말고  -로 해둘까 나중에 값이용하게? #$
                elif amap[nr][nc] >0 and visited[nr][nc]==0: # 미방문인 애들로 들어오면 무조건 아닌가  # 미방문했던 놈만! 0은 방문했던놈 방문해도 되지만 빙하는 아님
                    q.append( [nr,nc])
                    pass_set.add(nr*m+nc)
                    visited[nr][nc]=1
        #print('here',r,c)
        #print(amap)
                    

amax=0
# - 10,11번 넘지. 10짜리가 빙하에 둘러쌓여있으면.
for after_year in range(1, 10*29*29+2): #error(max(amap) )+2): # 10까지면 11  / 11 12 #$ max층까지? 
    # 엣지 케이스 
    node=0
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if amap[i][j]>0 : # - 빙하들만 미방문화 . 바다는 어차피 방문할 필요도없어서 방문했다침
                visited[i][j]=0
                node=(i,j)
            amax=max(amax,amap[i][j])
    #print( visited, amap, '-------', sep='\n')
    if node==0: # 1개도 없으면 
        break
    bfs(node, visited, amap)


    for i in range(1,n-1):
        if answer == after_year : # 에라이 이전 년도에서도 이미 누적됐었지
            break
        for j in range(1,m-1):
            if visited[i][j]==0:
                answer=after_year
                break
    # 정답에 너무 무의식적으로 맞추어 생각하지 마삼. 헷갈리지 않고 확실히.answer-1 관련 등
    # 다음 층에 보기엔 한번에 여러겹 된 경우? 
    
    #print( visited, amap, '-------', sep='\n')
    if answer ==after_year :#or answer == amax+1 : #-2머임. +2했던거에 -1이었으면 모랄까 ㅜ  # '정답'이 (0,) 1인케이스 after_year의 첫 값이 잖슴...
        break
    

# - 결과 때의 amap까지는  맞게 형성됐는데 visited가 다 1화돼있네 . 아하 이미 갔을때의 임 아하 -1 #~
# - 저번 문제 리스트
# - 다 사라진 경우?  그래도 visited은 처리하다의 기준인

# - 같은 년도에 0이 된애들(visited 0에서 1화, amap0이하 돼있음. 0인애들은 첨부터 visited 1임. 방문하지 않았던 nr nc를 사방검사하면, amap이 0이 아니라 미방문으로 들어왔던 거라 ㄱㅊ)이 옆에 영향을 줘버림. # 4방향에서도 미방문만 . 왜냐면 다행히 문제에선 미방문은 해당 노드의 값에 영향을 안줌ㅁ
answer=max(0, answer-1) # 이전 year의 끝에서 2조각 이상으로 쪼개졌으면 이번year에서 그것 처리 후  visited부분이 남게되는 거기 때문에. -1. 근데 이러면 10까지 갔을 떄 귀찮아질수있음.
print(answer)
# 4) n,m = 3, 다 0            
