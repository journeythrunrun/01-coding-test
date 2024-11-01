# 1벽 -> 로봇의 한칸이라도 N,N 도착하기

# - m1 bfs에서 append를 병렬 실행 
# - 1> i) 회전함수 
# - 2> ii) 이동함수 현재 두 값에서 상하좌우에 따라 값 검사
# - while

# - 미방문 체크 : 두 칸이라 "두위치같을 때"를 기준으로 visited[왼_r*n+c][오_]
# -> 최소 시간. : bfs

# 2) n=100, N=10,000 O(n**2_프로그래머스에서는됐었음 / 확실힌 NlogN)

# 3) while(q) : 자식에 해당하는 게 저 1>2>

from collections import deque
def check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited) :  
    if (visited[ nnr1*n+nnc1][nnr2*n+nnc2]==0 and  visited[nnr2*n+nnc2][nnr1*n+nnc1]==0  ) :  
        visited[nnr1*n+nnc1][nnr2*n+nnc2]=1
        q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
    
def solution(board):
    # - m1 bfs한 번 쓰는데 'append를 병렬 실행'. bfs 함수 자체를 병렬로 실행하진 않음. 
    # - ! 런타임 에러 : 엣지 케이스 말고 논리에서 문제가 있어서 그러기도 함
    #   + 심지어 이런 상황에서도 : 여기서 answer=0을 안하면 테스트케이스 6에서만 (break에해당하는 if문 내부를 못 가고 )런타임 에러가 남. 하면 오답.## 보드의 길이는 5이상이고 항상 목적지에 도착할 수 있는 경우만 있는데 왜 특정케이스에서만 저런 에러가 나지 ?
    
    n=len(board)
    visited=  [ [0]* (n*n) for _ in range(n*n) ] 
    dr,dc=[0,0,-1,1],[1,-1,0,0] # - ! 이거 위/아래/왼/오 중에 어떤 건지 맞추기 ->  오/왼/위/아래 ## r변화기준이니까 위/아래가 i=2,3임. 알고도 앞쪽으로 쏠려있는 값이 봐지네.dr은 앞에 네개에서만 봐야함.   
    
    q=deque([ [0,1, 0 ] ]) 
    visited[0][1]=1
    
    while(q):
        v= q.popleft() # [ 0_r아니고 왼쪽의 rc값 합친거임. ,0,0] # rc1, rc2, distance
        
        vr1, vc1= v[0]//n ,  v[0]%n # - r이랑 c가 가운데에 있으면 다른 변수인지 너무 티가 안나. [의미가 다른 부분]이니 [변수이름]에 [위계] 
        vr2, vc2= v[1]//n ,  v[1]%n
        
        # - ! LR=RL # 두 점의 위치가 바뀌어도 같은 놈이어야함
        #   + 회전된 이동 위치좌표 값 구하기 : (회전) 두 점에서 낮은 값을 기준으로 활용하여 맞는 곳으로 이동시킴 # (이동) 이동 함수 때는 두 점 모두에 같은 값 연산해줘서 상관없음 
        #   + 미방문 검사 시 :  visited 확인 때 L,R 위치 바꾼 값도 같은 걸로 쳐주기.
        
        # - ! 디버깅하며 다시 읽었는데도 vc1이 vc2로 돼있는 거 못본 거 실화냐. 변수명 한글자한글자 맞나 체크하자 ## print(vr1, vc1, vr2, vc2, v[2])

        # - !! 디버깅_정확한 케이스와 엄밀한 상황적기_그게 어디가 문젠지 다양하게 시도해볼 수 있음 ## 방문했던 곳 뒤 자식이 또 가네. visted 체크가 잘 안됐나  # 0 1 1 1    1, 2
        
        if (vr1==n-1 and vc1==n-1) or (vr2==n-1 and vc2==n-1):
            answer=v[2]  
            break
            
        # - 2> ii) 이동함수. 
        for i in range(4):
            r1, c1= v[0]//n + dr[i],  v[0]%n+dc[i] # - 여기서 수식보다(무조건 코드 줄 수 줄이는 것보다), vr1+dr[i] 처럼 가장 초반에 미리 좌표를 사용하기 편한 2차원으로 만들어준 후, 그 후엔 그 좌표값을 편하게 활용.
            r2, c2= v[1]//n + dr[i],  v[1]%n+dc[i] 
            
            
            # - 1> i) 회전함수_가로인 비행체케이스 : 왼쪽 축일 때_위두칸[A_rc2가 rc1의 위칸화]or 아래두칸[ rc2가 rc1의 아래칸화]이 0이어야함, 오른쪽 축일 때_위두칸[A_rc1이 rc2의 위칸화]/아래두칸0[rc1이 rc2의 위칸화]
            # - ! -> 위아래 이동이랑 조건은 겹치네 : 놉. 꽤 겹치는 부분 있는데 완벽히 겹치는 조건은 아니었었음. 엄밀히 if문의 한 요소요소 보며 체크
            if 0<=r1<n and 0<=c1<n and 0<=r2<n and 0<=c2<n and not board[r1][c1] and not board[r2][c2] : 
                if (visited[n*r1+c1][n*r2+c2]==0 and  visited[n*r2+c2][n*r1+c1]==0  ) : ## 둘 다 벽 아님## (2) amap의 값. 벽아니어야하지 
                    ## 비행체의 L이랑 R의 좌표값이 바뀌어도 같아야하는 상황 :  ## 미방문 
                    # - LR RL을 위한코드 수정 시:visited 저장 다 바꾸는 것보다는 검사하는 곳 한 곳바꾸는 게 편함
                    
                    ## 방문가능. 먹을 때 
                    visited[n*r1+c1][n*r2+c2]=1
                    q.append( [ n*r1+c1, n*r2+c2 ,v[2]+1  ] ) # - !  q.append([ r,c,d ]  : [ ] 씌워야.  q에 append할 때 요소도 리스트임! 
                    
                    # - 같은 자식층인 이동함수애들이 수정한 visited을 계승받는 상황   : 계승 받는 거 맞음.  ## 최소값 값인 놈이 가면 어떤 자식이 가든 똑같아서, 같은 자식 층에서 앞자식이 먹으면 visited갱신되는 거 거 맞음
                    
                    # - !!!! 이동함수와 회전함수가 조건 겹치는 부분은 회전할 때 거쳐가는 부분이 '벽없는지'임  
                    
                    # - 코딩 연습 시
                    #   + [정답 봤는데도 내 풀이 어디서 틀린지 모르겠다] => 내 답과 정답의 핵심값 출력값 비교. 테케 1개 틀리길래 엣지 케이스 같은 건줄 알았는데 알고리즘적으로 그냥 틀린 거일 수 있음. 예시에서 우연하게 희귀하게 발생했을 뿐이지 알고리즘적으로 논리 구조에 문제가 있던 거임.
                    
                    
                    # - !!!! 미방문이어야하는 거 != 벽이 아니어야하는 거 다름. 이동 땐 미방문이든 벽이 아니어야하는 거든 대상이 똑같은데 회전 땐 대상이다름.! 
                    #   + ii) 이동_ 새로운 점 두 곳이 미방문이어야함( 두 점 다 옮기니까.) & 그 두 점 다  벽이 아니어야함.
                    #   + ii) 회전_새로운 두 점 중 한 곳만 미방문인 곳으로 이동  & 그 두 점 다 벽이 아니어야함
                    #   + i) 디버깅_[회전 땐 스치는 곳이 이미 방문했던 곳이어도 괜찮음 & 이동함수와 동일하게 새로운 두점값이 벽은 아니어야함] ### 여기 조건문 위치에선 새로운 두 점 모두 미방문일 때만 실행돼버렸었음
                # 비행체가 가로인 경우 ## 행값같음. 세로인경우 : 열값같음 --> 2케이스밖에 없어서 나머지라 else로 ㄱㄴ
                width = True if r1==r2 else False

                # - BFS 변수이름 ㅣ 앞으론 경험적인 거 따르자. 자식은 n_r n_c . 부모가 v/r/c
                
                if width and i ==2 : ## 위 애들 값비었음 # A
                    # 위아래 -> 행 의미 맞게 
                    ###- 1> i) 회전함수 : 왼쪽 축일 때_위두칸[A_'v'rc2가(원래는 rc2를 nrc로 했어야..) vrc1의 위칸화]or 아래두칸[ vrc2가 vrc1의 아래칸화]이 0이어야함, 오른쪽 축일 때_위두칸[A_vrc1이 vrc2의 위칸화]/아래두칸0[vrc1이 vrc2의 아래칸화]
                    # - m_other : 케이스 미리 나누고 축지정한 후, 회전방향 으로 회전하는 함수 ? 더복잡할 수 있음. 축말고 나머지인 애 값의 대각선 움직임 열행증감처리 귀찮을듯. 축과의 상대적인 위치에 의한 거라 귀찮_설령 수식으로 한방 대신 if문으로 네가지 케이스에서 값지정해줘도.
                    r_low,c_low=min(vr1,vr2),min(vc1,vc2) # - 네 개의 좌표에서 min값 기준으로 새 좌표값 할당
                    nnr1,nnc1=r_low,c_low
                    nnr2,nnc2=r_low-1,c_low

                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited) # - deque : mutable. # - ! 첨에 저 좌표 네값만 건넬뻔. 한 요소 한요소 살펴라. visited도 건네야함.##  그래서 다른 분은solution함수에서 for문과 함께 visited 검사/수정/ q 수정하고, 추가 함수에선 이동 대상인 좌표를 가져옮 : 근데 일단 미방문 등의 체크로 필요한 것만 이동회전함수 돌리기보다, 이동함수, 회전함수 돌려서 후보군인 애들을 다 먼저 계산함. 시복 차이는 안나긴함. 
                    
                    # - 코드 복사 얼마나 대충한거지. 다른 걸로 너무 빠르게 전환하지말기? [L][R]위치 바꿔야지.. 의미생각하며 복사?
                    # if (visited[ nnr1*n+nnc1][nnr2*n+nnc2]==0 and  visited[nnr2*n+nnc2][nnr1*n+nnc1]==0  ) :  
                    #     visited[nnr1*n+nnc1][nnr2*n+nnc2] =1 # visited[nnr1*n+nnc1][nnr2*n+nnc2]  
                    # - ! 실환가. 이런저런 방법으로 수정 시도 해도 하나는 다끝내라. 애초에 적질 말던가. 빠르게 떠오른 아이디어들이 많아서 놓치기 전에 우선 이것저것 적은 거면, 주석으로 적어놓기
                    #     q.append([nnr1*n+nnc1, nnr2*n+nnc2,v[2]+1])
                    
                    
                    
                    # - visited & append 케이스에 따라 여러번 쓸거 같으니 -> 함수화하지. 반복사용가능한 코드화.
                    #   + visited 건네기 크다고 생각했는데, 리스트라 주소참조라 ㄱㅊ 
                    nnr1,nnc1=r_low,c_low+1
                    nnr2,nnc2=r_low-1,c_low+1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)
                    
                    
                    '''
                    visited[n*vr1+vc1][n*(vr1 -1)+vc1]=1
                    q.append( [ n*vr1+vc1, n*(vr1 -1)+vc1 ,v[2]+1 ]) 
                    visited[n*(vr2 -1)+vc2][n*vr2+vc2]=1
                    q.append([n*(vr2 -1)+vc2, n*vr2+vc2 ,v[2]+1 ])
                    '''
                    # - 첨에 회전함수마다 도착할 곳 커스터마징한 좌표값을 썼는데 복붙할 곳 너무 많음. 차라리 새좌표 = x1,y1 x2,y2로 설정 후 다른 곳에서 설정만 바꾸며 그 아래 중복 코드(visit,append. 근데 보통 bfs에선 for로 반복하지. 그걸 생각하기. append하고 for문 돌려도 됐음) 활용

                elif width and i==3 : # - 이런 규칙 수식은 종이로 적어야 디버깅이든 뭐든 빠를듯
                    r_low,c_low=min(vr1,vr2),min(vc1,vc2) 
                    nnr1,nnc1=r_low,c_low
                    nnr2,nnc2=r_low+1,c_low
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)

                    nnr1,nnc1=r_low,c_low+1
                    nnr2,nnc2=r_low+1,c_low+1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)


                # 1> i) 회전함수_세로인 비행체 
                ## 오른쪽으로 이동하는 좌표로 갈 수 있을 경우i=0 : 아래에 있던 좌표가(행이 더큰 좌표가) 작은행값놈의행값화&열+1화   | 위에있던 좌표가(행이더작은좌표가) 행값높은것과행값동기화& # - 이거 확실한 세부사항은 글로쓰는것보다 머리로 그렸을 때 좌표로 그려버리는 게 나을듯
                ## 왼쪽으로 이동하는 좌표로 갈 수 있는 경우 i=1: 


                elif not width and i==0: ## 오른
                    r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                    nnr1,nnc1=r_low,c_low
                    nnr2,nnc2=r_low,c_low+1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)

                    nnr1,nnc1=r_low+1,c_low
                    nnr2,nnc2=r_low+1,c_low+1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)

                elif not width and i==1 : 
                    r_low,c_low=min(vr1,vr2),min(vc1,vc2)
                    nnr1,nnc1=r_low,c_low
                    nnr2,nnc2=r_low,c_low-1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)
                    
                    nnr1,nnc1=r_low+1,c_low
                    nnr2,nnc2=r_low+1,c_low-1
                    check_and_go(nnr1,nnc1,nnr2,nnc2 ,n,v,q,visited)
                    
    
    # - ! 아 잠시든 시간 오버돼서 일단 제출하려고든 answer+1해뒀으면 #$[표기] 항상 잘 해야지
    return answer

# 4) 보드의 한 변 길이 5,6,..
# - # 도착가능경우만 줌_ 마지막 점이 1일경우

# - 6) 논리 틀려도 많은 테스트 케이스 맞추기도 함. 꼭 테스트 케이스의 중간값 출력하여 나와야하는 것과 다 맞는지. 앞 2~3회전만이라도 봐.

# -  1h 5m정도? : 시간오버로 효율을 위해 다른 사람 풀이 봄
#   + 내 께 책 관련된 풀이보다 n 줄였당! 
#   >  (정답보기 전까지.)(주석 시간 5m정도 뺌)
#   + = 세로로 놓인 상태에서 회전하는 케이스 빠트림 
#     + (1) 이동 (2) 회전에서 이동은 완벽하고 회전은 규칙찾기를 했었다. [규칙찾기]는 예시에서 하는 거라, [모든 경우의 수] 따진다 생각하고 가능한 회전 진짜 [하나하나 스도쿠마냥 다 따져봐야함]

#   > 논리 상 가능한 방법이고 디버깅으로 세부 부분 수정하던 중이었음  


# - 2차원 visited를 위해 한 점의 좌표인 r,c를 한 값화 했었다. 근데 그 거 빼고 나머지에서는 다 r,c로 각각 가지고 있는 게 코드 깔끔하겠다. 여기저기서 계속 <->하면서 수식 더 생김. 굳이 2->1->2차원화 다시 할 필요없음. 
#   + 근데 약간 처음에만 쓰기 불편한거지 4차원/3차원 visited이 오히려 나중에는 <->이거 안 해서 편했을 듯 : 그리고  r1,c1,r2,c2를 인덱스위치 기준으로 안 하고 h로 쌓았다 생각하면 [0/1_h_첫점/두번째점][r][c]로 3차원이면 되서 쉬움.
#   + 다른 거 가능하면 수식 지양이 나은 건 : 디버깅 때 엄청 직관적이진 않아서 번거로움.

# - 시간복잡도
#   +  새로 듣기 전에 이코테(책이니 더 전문적일 수도)&경험적인것도 조합해서? 외웠던 시간 복잡도는 다음과 같음. 
#     + n**3_500, n**2_[만]_책피셜(<-2000), nlogn_백만(<-십만) 이하  

#     + 안전빵차이일까, 코테연습문제에서 효율성 부분 없으면 시간복잡도 길이에 비해 초과해도 뻑 안나는 경우도 있나
#     >  생각해보니 O(n**2)은 2000이라는 말이 있긴 했어도 경험적으로 10,000에서 안되는 경우는 없었던 것 같기도 함. 물론 내가 최적화해서 풀려고 해서 애초에 시복 벗어날 일이 적었을 수도 있고 .


# - 근데 깃허브 검색 기능 되게 좋다. 앞으로 코드 말고도 공부한거 깃허브에 마크다운으로 적을까. & 블로그에 해당 깃허브링크 주소올리기(블로그는 마크다운 깨지니깡. & 블로그의 이득도 같이가질수있겄넹). [-] 물론 검색에 한계가 있는 부분 있으니까 그거 보고 /분량 등에 따라 결정?
#   > 왜냐면 이전에 적었던 거 많은데 깃허브 검색기능 보니까 원하는 내용 바로 찾기에 좋음.


# - 미방문 검사용 visisted 만들기 번거로울 때 <->-> if _ in set1  O(1)_[집합/딕셔너리 키]로 방문체크

# - a={} # - 기본 딕셔너리.# - = {'a'}:  키 하나만 넣는다 생각하면 안됨 이건 set.

# - 힙큐, 큐 , 우선순위큐_ 복습/자기퀴즈
#   + 힙큐 사용 함수 | 시간복잡도 
#   + 디큐의 장2/단점 | 사용 함수
#   + 우선순위큐 어떤 거 이용하실
#   + https://github.com/journeythrunrun/01-coding-test/blob/main/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/42627.%E2%80%85%EB%94%94%EC%8A%A4%ED%81%AC%E2%80%85%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC/%EB%94%94%EC%8A%A4%ED%81%AC%E2%80%85%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC.py

# - 다른 사람 풀이 
#   > (( 더 효율적인 걸로 투표된 게 있을 수 있는데 넘 길구 특이한 거 사용도 있어서 & 어차피 내 코드로도 효율화할 거라(worst O(n)보다 더 효율적일 순없을 ) 걍 해석하기 쉬운 코드 읽었음 [https://github.com/ndb796] -> 그 특이한 게 다른 곳에도 쓸 수 있을 법한 거면 새로 배우는 게 좋은 건가? 근데 어차피 더 줄일 순 없는 시복이니까 더 줄여지는 케이스에서 특이한 거 있으면 배우지뭐 )) 

#   + 내께 더 빠르긴 하네  1503.11ms <-> 2415.31ms


# - 이 코드가 L,R = R,L 처리한 방법 
#   + visited : "세트"를 "요소"로 가지는 "리스트" & 리스트 in 에서 검사. 시복은 n더 안좋음
#   + 순서 바꿔도 같은 거 = set. -> set을 가지고 같은 놈인지 검사. set이 요소.
#     > visited의 '요소'가 : 'set'임 {(1, 1), (1, 2)} # 세트는 요소의 순서 바뀌도 같음. 

# - 복잡한 3차원 [visited] 대체법 검사
#   + [set나 딕셔너리의 키에다 좌표를 튜플형]으로 저장해서 in으로 찾으면 O(1)
#     > m_other) set의 요소에 비행체 좌표를한값으로 맵핑 & in :{-R(r1,c1,r2,c2)_사실 맵핑한다고 하면 한 정수로 거리 떨어트려서 맵핑시킬수는 있음. 최대값 넘게 떨어트리기 번거로우면 양수/음수로 R/L방향 편하게 맵핑가능. RL=LR은 방문갱신 하거나 검사할 때 LR바꿔서도 하면 됨.)  } & in 검사  O(1)  - > 에라이 맵핑 설명하다보니 그냥 내 리스트인덱스 조회가 편할수도
#       > ## 두점포함 비행체위치를 한값으로맵핑시: L_*십만?대에서시작((굳이최대값계산안해봤음)) R_일의자리에서 시작.처럼 맵핑 가능. 

#     > m_other) 딕셔너리의 요소인 키가 L,R(튜플) &  딕셔너리 in 검사


# - set [집합]
#   + hashable 자료형[tuple(모든 요소가 hashable인 경우만. ) ,str,  숫자 등]만 set의 요소로 입력 가능. <-> [불변형]. list, dict, set형 요소는 안됨 # ST  style로 암기.ㅎㅋ
# >> 다른 O(1) 
# : .add() / .update( {3} ) / |={3} # 집합끼리의 연산 이용
# : .discard(3)  (없어도 에러 X) / .remove(3)  ( 없으면 에러_예외처리 필요 )
# : .pop()
# : .clear()

# > 집합끼리의 연산. {} 씌워줘서 적용가능.
# : 축약형 가능  ^=
# : 1) set1.union(a,b) / a | b
# : 2) set1.intersection(a,b) / a & b
# : 3) set1.difference(a,b) / a - b
# : 4) set1.symmetric_difference(a,b) /  a^b (xor. 겹치지 않는 원소)
'''
from collections import deque
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
    visited = dict() ### []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.update() ### append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        print( [ [a[0]-1,a[1]-1 ] for a in pos] ,cost)
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos: # - 비행체의 두 점 중 한 점이라도 도착점 : or보다 (도착점), in 이 코드 짧네
            return cost  
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board): # - 우와 난 append랑 visited 반복 되길래  go를 함수로 만드려고 했었는데, [이 사람은 더 큰 범위의 함수]'v 다음으로 갈 수 있는 위치들'함수화해서 for에서 돌림. (~~ bfs의 for부분이랑 비슷하네. [자식들을] [함수로든 미리 구해서] for에서 돌자.) 그래서 for내에서 append와 visited가 자동으로 반복됨. []
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited: # - 여기 O(1)아님 visited의 요소가 딕셔너리지 visited 자체는 리스트라 O(n) # - 10,000(만)도 O(n**2) 된다는 확신 있으셨나봄. 그럼 나도 더 만 믿자  
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0

'''


















# > 예전에 40분 풀어서 테스트 케이스만 맞추고 제출은 많이 틀린 본 있는데 그거 수정하기엔 이거 기출 문제니까&그기간사이 bfs/dfs몇문제 풀었으니까 작년 쯤 푼문제 중간부터 하기보다 첨부터 풀어보자
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