# 1벽 -> 로봇의 한칸이라도 N,N 도착하기

# - #$ 병렬실행 보통 dfs때? m1 bfs 병렬 실행 or bfs 같은 자식으로
# - 1> i) 회전함수 
# - 2> ii) 이동함수 현재 두 값에서 상하좌우에 따라 값 검사
# - while

# - 미방문 체크 : 두 칸이라 "두위치같을 때"를 기준으로 visited[왼_r*n+c][오_]


# -> 최소 시간. : bfs

# 2) n=100, N=10,000 O(n**2_프로그래머스에서는됐었음 / 확실힌 NlogN)

# 3) while(q) : 자식에 해당하는 게 저 1>2>
from collections import deque
# def go(r): #$
    
def solution(board):
    answer=0
    n=len(board)
    visited=  [ [0]* (n*n) for _ in range(n*n) ]  #   visited[n*n+c][오_]
    dr,dc=[0,0,-1,1],[1,-1,0,0] # - ! 이거 위/아래/왼/오 중에 어떤 건지 맞추기 ->  오/왼/위/아래 ## r변화기준이니까 위/아래가 i=2,3임. 알고도 앞쪽으로 쏠려있는 값이 봐지네.dr은 앞에 네개에서만 봐야함.   
    
    q=deque([ [0,1, 0 ] ]) 
    
    answer=0# UnboundLocalError: local variable 'answer' referenced before assignment이거 떠서
    visited[0][1]=1
    # 주석시간
    # 다돌기 & 병렬함수여도 빨리탈출도나중에
    while(q):
        v= q.popleft() # [0_r아니고 왼쪽의 rc값 합친거임. ,0,0] # rc1 rc2 distance
        vr1, vc1= v[0]//n ,  v[0]%n #~ , 위치 변경
        vr2, vc2= v[1]//n ,  v[1]%n
        # - ! 두 좌표의 위치가 바뀌어도 같은 놈이어야함. 좌표 기준으로 이동시켜줄 때 회전에서 낮은 값을 기준으로 이용하여 맞는 곳으로 이동시킴. & visited 확인 때 바꾼 값도 같은 걸로 쳐주기.
        #   + 이동 때는 두 점모두에 같은 값 연산해줘서 상관없음 
        #   + -> 그래스 set쓰신
        
        # print(vr1, vc2, vr2, vc2, v[2]) #$
        ## 두 좌표인데 자꾸 실수하네 초기값이랑-> 마지막값도. n-2위치도 있어야.
        if (vr1==n-1 and vc1==n-1) or (vr2==n-1 and vc2==n-1): # 좌표 네개화 귀찮아서 여기서 미리. 어차피 무조건 되는 케이스만 있음 . 이라기엔if 방문 전은 최소로 갔으나 못가는는 경로일수있음 # for 가지마삼 그럼 new r임귀찮
            answer=v[2]    
            # print( ' here' )
            break
            
        # - 2> ii) 이동함수 현재 두 값에서 상하좌우에 따라 값 검사
        for i in range(4):
            r1, c1= v[0]//n + dr[i],  v[0]%n+dc[i] # 여기서 수식보다(무조건 코드 줄 수 줄이는 것보다), 가장 초반에 미리 vr1을 사용하기 편한 2차원으로 나눠준 후, 그 후엔 그 좌표값을 편하게 활용.
            r2, c2= v[1]//n + dr[i],  v[1]%n+dc[i] 
            # X_nr, nc= v[0]+dr[i], v[1]+dc[i]
            
            # - 1> i) 회전함수_가로인 비행체케이스 : 왼쪽 축일 때_위두칸[A_rc2가 rc1의 위칸화]or 아래두칸[ rc2가 rc1의 아래칸화]이 0이어야함, 오른쪽 축일 때_위두칸[A_rc1이 rc2의 위칸화]/아래두칸0[rc1이 rc2의 위칸화]
            # -> 위아래 이동이랑 조건은 겹치네
            

            
            
            
                
            if 0<=r1<n and 0<=c1<n and 0<=r2<n and 0<=c2<n and (visited[n*r1+c1][n*r2+c2]==0 and  visited[n*r2+c2][n*r1+c1]==0  ) : # - 비행체의 L이랑 R의 좌표값이 바뀌어도 같아야하는 상황 : 코드 수정 시:visited 저장 다 바꾸는 것보다는 검사하는 곳 한 곳바꾸는 게 편함 ## 미방문 
                if not board[r1][c1] and not board[r2][c2] : # 둘 다 벽 아님## (2) amap의 값. 벽아니어야하지 
                    # 방문가능. 먹을 때 
                    visited[n*r1+c1][n*r2+c2]=1
                    q.append( [ n*r1+c1, n*r2+c2 ,v[2]+1  ] ) # - ! []
                    # 비행체가 가로인 경우 : 행값같음. 세로인경우 : 열값같음 --> 2케이스밖에 없어서 나머지라 else로 ㄱㄴ
                    width = True if r1==r2 else False
                    
                    # r1,c1는 자식들이고, 지나갈수있는 거 용으로 해당 조건 갈수있는거본거고 기초 (변수명 ㅜ) 값은 vr1,vr2,..
                    if width and i ==2 : ## 위 애들 값비었음 # A
                        # 위아래 -> 행 의미 맞게 
                        ###- 1> i) 회전함수 : 왼쪽 축일 때_위두칸[A_'v'rc2가(원래는 rc2를 nrc로 했어야..) vrc1의 위칸화]or 아래두칸[ vrc2가 vrc1의 아래칸화]이 0이어야함, 오른쪽 축일 때_위두칸[A_vrc1이 vrc2의 위칸화]/아래두칸0[vrc1이 vrc2의 아래칸화]
                        # 다른 부분은 nr nc가 지나가는 값검사도 있어서  최종 위치는 다름 . 위계는 이미 distance로자동임. visite도 최소기준으로 업뎃되있음    앞으로 떙겨주기엔 visit해제 할필요없음
        
                        # - 케이스 미리 나누고 축, 회전방향 으로 회전하는 함수 만들었어도
                        
                        r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                        nnr1,nnc1=r_low,c_low
                        nnr2,nnc2=r_low-1,c_low
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])

                        nnr1,nnc1=r_low,c_low+1
                        nnr2,nnc2=r_low-1,c_low+1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
                        '''
                        visited[n*vr1+vc1][n*(vr1 -1)+vc1]=1
                        q.append( [ n*vr1+vc1, n*(vr1 -1)+vc1 ,v[2]+1 ]) 
                        visited[n*(vr2 -1)+vc2][n*vr2+vc2]=1
                        q.append([n*(vr2 -1)+vc2, n*vr2+vc2 ,v[2]+1 ])
                        '''
                        # print(r1,c1,r2,c2,'->',nnr1,nnc1,nnr2,nnc2)
                        
                    elif width and i==3 : # - 이런 규칙 수식은 종이로 적어야 디버깅이든 뭐든 빠를듯
                        r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                        nnr1,nnc1=r_low,c_low
                        nnr2,nnc2=r_low+1,c_low
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])

                        nnr1,nnc1=r_low,c_low+1
                        nnr2,nnc2=r_low+1,c_low+1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
                        
                        # visited[n*vr1+vc1][ n*(vr1 +1)+vc1 ]=1
                        # q.append([n*vr1+vc1, n*(vr1 +1)+vc1 ,v[2]+1])
                        # visited[n*(vr2 +1)+vc2][n*vr2+vc2]=1
                        # q.append([n*(vr2 +1)+vc2, n*vr2+vc2 ,v[2]+1])   
                        
                    
                    # 1> i) 회전함수_세로인 비행체 
                    # 오른쪽으로 이동하는 좌표로 갈 수 있을 경우i=0 : 아래에 있던 좌표가(행이 더큰 좌표가) 작은행값놈의행값화&열+1화   | 위에있던 좌표가(행이더작은좌표가) 행값높은것과행값동기화& # - 이거 확실한 세부사항은 글로쓰는것보다 머리로 그렸을 때 좌표로 그려버리는 게 나을듯
                    # 왼쪽으로 이동하는 좌표로 갈 수 있는 경우 i=1: 
                    
                    
                    elif not width and i==0: ## 오른
                        r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                        nnr1,nnc1=r_low,c_low
                        nnr2,nnc2=r_low,c_low+1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])

                        nnr1,nnc1=r_low+1,c_low
                        nnr2,nnc2=r_low+1,c_low+1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
                        
                    elif not width and i==1 : 
                        r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                        nnr1,nnc1=r_low,c_low
                        nnr2,nnc2=r_low,c_low-1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2] # - visited & append 케이스에 따라 여러번 쓸거 같으니 -> 함수화하지. 반복사용가능한 코드화.
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])

                        nnr1,nnc1=r_low+1,c_low
                        nnr2,nnc2=r_low+1,c_low-1
                        visited[nnr1*n+nnc1][nnr2*n+nnc2]
                        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
                        # print(r1,c1,r2,c2,'->',nnr1,nnc1,nnr2,nnc2)
                        
    # return 
    # - ! 아 answer+1해뒀으면 #$[표기] 항상 잘 해야지
    return answer
# 4) 보드의 한 변 길이 5,6,..
# - # 도착가능경우만 줌_ 마지막 점이 1일경우

# - (정답보기 전까지)주석 빼면 1h 5m정도? : 시간오버로 효율을 위해 다른 사람 풀이 봄
#   + = 세로로 놓인 상태에서 회전하는 케이스 빠트림 
#     + (1) 이동 (2) 회전에서 이동은 완벽하고 회전은 규칙찾기를 했었다. [규칙찾기]는 예시에서 하는 거라, [모든 경우의 수] 따진다 생각하고 가능한 회전 진짜 [하나하나 스도쿠마냥 다 따져봐야함]

#   + 논리 상 가능한 방법이고 디버깅으로 세부 부분 수정하던 중이었음  


# - 2차원 visited를 위해 한 점의 좌표인 r,c를 한 값화 했었다. 근데 그 거 빼고 나머지에서는 다 r,c로 각각 가지고 있는 게 코드 깔끔하겠다. 여기저기서 계속 <->하면서 수식 더 생김. 굳이 2->1->2차원화 다시 할 필요없음. 
#   + 근데 약간 처음에만 쓰기 불편한거지 4차원/3차원 visited이 오히려 나중에는 <->이거 안 해서 편했을 듯 : 그리고  r1,c1,r2,c2를 인덱스위치 기준으로 안 하고 h로 쌓았다 생각하면 [0/1_h_첫점/두번째점][r][c]로 3차원이면 되서 쉬움. #$ 두 점의 위치가 서로 바뀌는 케이스는
#   + 다른 거 가능하면 수식 지양이 나은 건 : 디버깅 때 엄청 직관적이진 않아서 번거로움.

# - 시간복잡도
#   +  새로 듣기 전에 이코테(책이니 더 전문적일 수도)&경험적인것도 조합해서? 외웠던 시간 복잡도는 다음과 같음. 
#     + 안전빵차이일까, 코테연습문제에서 효율성 부분 없으면 시간복잡도 길이에 비해 초과해도 뻑 안나는 경우도 있나
#   + n**3_500, n**2_만(<-2000), nlogn_백만(<-십만) 이하 

# - 근데 깃허브 검색 기능 되게 좋다. 앞으로 코드 말고도 공부한거 깃허브에 마크다운으로 적을까. & 블로그에 해당 깃허브링크 주소올리기(블로그는 마크다운 깨지니깡. & 블로그의 이득도 같이가질수있겄넹). [-] 물론 검색에 한계가 있는 부분 있으니까 그거 보고 /분량 등에 따라 결정?
#   + 왜냐면 이전에 적었던 거 많은데 깃허브 검색기능 보니까 원하는 내용 바로 찾기에 좋음.


# - 힙큐 시간복잡도 #$
# - 10,000_O(n**2)으로 봐도 되나체크 #$. 생각해보니 O(n**2)은 2000이라는 말이 있긴 했어도 경험적으로 10,000에서 안되는 경우는 없었던 것 같기도 함. 물론 내가 최적화해서 풀려고 해서 애초에 시복 벗어날 일이 적었을 수도 있고 .

# - 다른 사람 풀이 (( 더 효율적인 걸로 투표된 게 있을 수 있는데 넘 길구 특이한 거 사용도 있어서 & 어차피 내 코드로도 효율화할 거라(worst O(n)보다 더 효율적일 순없을 ) 걍 해석하기 쉬운 코드 읽었음 [https://github.com/ndb796] -> 그 특이한 게 다른 곳에도 쓸 수 있을 법한 거면 새로 배우는 게 좋은 건가? 근데 어차피 더 줄일 순 없는 시복이니까 더 줄여지는 케이스에서 특이한 거 있으면 배우지뭐 )) 
#   + 복잡한 3차원 [visited] 대신, [set나 딕셔너리의 키에다 좌표를 튜플형]으로 저장해서 in으로 찾으면 O(1)

# from collections import deque
# - 이 코드가 L,R = R,L 처리한 방법 
#   + #$
def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # - 난 위쪽/아래쪽 칸이 비어있는 조건이 이동 때 따졌던 조건과 부분집합인 부분이 있어서 그 아래에서 코드 작성해서 i==로 검사함. 근데 시복 차이까진 안 날테니 굳이 조건 내부로 최적화하기보다 그냥 아무 곳에 바로 하는 게 속도나 가시성이 나았을 수도 있겠네.  # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면 
                # - 길이2가 [위]로 [90도 회전] = 아래와 같은데, for i in [-1,1] 에서 공통으로 통하는 수식을 만들 기 위해 아주 specific한 좌표 이용함. 걍 규칙찾아서 하는 것도 실수만 안하고 값 체크만 하면 적당한 방법일듯. 굳이 외울정돈? 
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos: # - 비행체의 두 점 중 한 점이라도 도착점 : or보다 (도착점), in 이 코드 짧네
            return cost  
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board): # - 우와 난 append랑 visited 반복 되길래  go를 함수로 만드려고 했었는데, [이 사람은 더 큰 범위의 함수]'v 다음으로 갈 수 있는 위치들'함수화해서 for에서 돌림. (~~ bfs의 for부분이랑 비슷하네. [자식들을] [함수로든 미리 구해서] for에서 돌자.) 그래서 for내에서 append와 visited가 자동으로 반복됨. []
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited: # - in 있는지 | visisted | -> [집합] 검사 ~ 
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0


# - 예전에 40분 풀어서 테스트 케이스만 맞추고 제출은 많이 틀린 본 있는데 좋은 문제니까&그기간사이 bfs/dfs몇문제 풀었으니까 작년 쯤 푼문제 중간부터 하기보다 첨부터 풀어보자
''' 

# 최소시간 / 90도 회전
# bfs 
# 최소시간 dfs

# 방문하지 않은 모든 0 칸 가기.
# 

# 무조건 갈 수 있는 거만 준다고 했으니, 회전한 위치 까지는 몰라도 되겠다.
# 0 길찾고
# 가려는 방향에서 두값 0인지 비교 [a:a+2] / 회전숫자 업하고 비교
dr=[0,0,1,-1,1,1,-1,-1]# 오른 쪽 기준 8가지 방향 
dc=[1,-1,0,0,1,-1,1,-1]# 리스트라서 다른 함수 끼리도 쓸수 있는 거 아니었나..

def dfs(v,distance,board):
    distance+=1 #~최소값 재귀함수속 전달 / 예전파이참 문제 훑
                # 함수 탈출하면서 distance자동으로 1 빠지려나
                
    if v[0] == len(board)-1 and v[1]==len(board[0])-1 :
        return 1 # 재귀 속이어도 동일한 return값으로 계속 탈출# while...

    # 이미 왼쪽이 0이라 오른쪽발 기준으로 주변이 0이면 다 갈 수 있으니, 탐색. 
    for i in range(8):
        newr=v[0]+dr[i]
        newc=v[1]+dc[i]
        
        if newr > -1 and newr< len(board) and newc>-1 and newc<len(board[0]):
            if board[newr][newc]==0:
                if newr == len(board)-1 and newc==len(board[0])-1 :
                    answer[0]=min(answer[0],distance)#~+1? 함수 바로 아래 조건문에 해버리면 탈출때 귀찮아질 수잇음?
                board[newr][newc]=1 #~ 저번 코드들 파이참 보자
                dfs([newr,newc],distance,board)
                
    return 0
        
answer = [1000000]
    
def solution(board):
    
    # visited=[[False]*len(board[0]) for _ in range(len(board)) ]
    board[0][0], board[0][1]=1,1#True, True
    # ㅇ
    dfs([0,1],-1,board)#~첨에 1더해주는것땜시 # 보드 안 넣으면 정의 안됐다고 뜨네
    return answer[0]


# 40분 _틀렸음_디버깅보다 복습하고 오는것도.






# 이것이 코딩테스트다 _ 난이도 3 _ 50분 
'''