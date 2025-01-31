# : 좌표 같은 경우 없음
# : 2개 이상으로 분리/완전포함된 경우 없음
# -> 최소 움직임수
# 2) 좌표 50 -> 맵크기 ~ 250  O(n^3)
# m0_ 시복으로부터 방법추론
# m1_규칙찾기
# (lx, ly, rx, ry) -> 새 사각형 추가될 때마다 꼭짓점 개수 +2개 _는아니네
# 추가된 꼭짓점 -> 내부에 있는 거 제거 & 점점추가 ,... : 알고리즘 배우자는 취지에 좀 벗어남 m2로

# m2_bfs 공간있는맵화&방문
# -> ( )  값 감소하며 가다가 새로 받은 x꼭짓점 좌표 나오면 -> 
# : (1) 사각형 내부 해당위치 값들 1로해버리기. -> 1아닌 곳둘러서 다니기 # m2로 픽하고해서그런지 거의 4분컷?

# 3) amap = [[0]*51 for _ in range(51) ]
#[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
# -> for one_rect in rectangle : lx, ly, rx, ry =map(one_rect)   
# 갈수있는길 모서리1화 __내부 0
# -> 값범위 저장? & if in (l+1,r) 
# -> amap[lx][]~[lx2][] =1 | # 가다가 1인곳만나면 
# => 새로운 4개의 점이 내부에 없는 애는 1만날때까지 다시0화(in 꼭짓점방법) _내부검사 : x==in (lx,rx) and (ly,ry) 
# 모서리 저장 후 모서리에서 제거 방법도 있긴함



# - if in (l+1,r)  -> if__any (  l+1 < x< r   for _ in 사각형) 
# - (꼭짓점 규칙찾기 & 꼭짓점으로부터 값은 너무 specific복잡해짐. 굳이 너무 specific & 최적화 알고리즘 생각하진 말자. 복잡해져서 시간 안에 못 풀게 되기도 함) 
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    amap = [[0]*52 for _ in range(52) ]
    visited = [[0]*52 for _ in range(52) ]
    
#     inner=[[1,1,1,1]]
#     #[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
#     for one_rect in rectangle : 
#         lx, ly, rx, ry =map(one_rect)  
#         for i in range(lx,rx+1): # - : 사각형의 내부 값은 변경 안 하고 모서리 위치만 값 바꾸는 코드라 내부를 돌기 위한 for 한개는 덜 있는 상태
#             amap[i][ly]=1 
#             amap[i][ry]=1
#         for j in range(ly, ry+1):
#             amap[lx][i]=1
#             amap[rx][i]=1
#         # 갈수있는길 모서리1화_갈 수있는 길 아님 튀어나온 1있는 상태임. __내부 0
#         # -> 값범위 저장? & if in (l+1,r) -> 
#         #### -> amap[lx][]~[lx2][] =1 | # 가다가 1인곳만나면 

#         # => [튀어나온 모서리 제거를 꼭짓점으로부터 함. 규칙찾기 번거로움]새로운 4개의 점이 내부에 있는 애는 점으로부터 양방향으로 1만날때까지 모서리부분 다시0화 
#         # _내부검사 : x==in (lx,rx) and (ly,ry) 

#         for a_inner in inner :# [1,1,7,4]
#             for _ in range(4):
#             if lx in set( range( lx,rx+1 )) and ly in set( range( ly,ry+1 )) :
#             if lx ry
#         # 내부범위 리뉴얼

    # 주석은 여러방법 왔다갔다해서 섞여있음
    
    # m_other 기본값 0, 내부 다 1 -> 1위에서 1과0경계선 따라 탐색. # 즉 3영역아니고 2영역
    #[[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    answer=0
    # cnt=0
    for one_rect in rectangle : # - => for lx, ly, rx, ry in 사각형
        lx, ly, rx, ry =one_rect
        
        # - 사각형의 가로나 세로의 길이가 1일 때 (의미를 할당한)amap이 백지화 안되려면 : 모서리도 색칠해줘야함 -> m_A가 안됐던 이유.
        # - m 떠올리고 4)_엣지 케이스 포괄 알고리즘인지 생각
        for i in range(lx,rx+1): # - 실화냐 위의 for만 range안썼었다. 
            for j in range(  ly, ry+1):
                if i == lx or i==rx or j == ly or j== ry :
                    amap[i][j]=2
                else :
                    amap[i][j]=1
    for lx, ly, rx, ry in rectangle : # 후 추가
        for i in range(lx,rx+1):
            for j in range(  ly, ry+1):
                if i == lx or i==rx or j == ly or j== ry :
                    pass 
                else :
                    amap[i][j]=1                
    # - (i_1) 이동 조건 : "본인이 1이면서"(적어놓고 아래코드에선 구현안했을 때도 있었음) '8방중에 0있음[외부값이라고 의미 적어두는 게 나을듯]있음' 
    #   + [단점 ㄷ자에선 8방에 외부값었음. 모서리는 무조건 내부값은 근처에 있을텐데 본인과 같은값이어서 구별더어려움_다시 사각형전부 검사하는 방법은 있는데 저 땐 amap으로만 풀려고 했었음] 디버깅으로 조건추가 :   8방이어도 건너뛰어서가는거안됨. 연결모서리체크 ##예제 1_3,5에서 3,6 으로 가버림.
    ## 단점 원인 : 네곳다 1이라 amap에서 어케 맞는 깊은경로를 알게할까. 애초에 8방향중 n안됨. 
    
    # - > [단점해결하려는 노력][_코드 구현하기 매우 복잡한 구체화조건이었음. 차라리 더 쉬운 방법 생각해서 하는 게 나았을련지]8방에서 되는거 여러놈 있을 때 ## :  두 경로에서 오른쪽이 0/1인거의 지속성 각각 유지. -> _X_ 반시계방향이든 시계방향    
    ## 모서리 값 따로 2로. & 1 방향성일치 # count옆에 추가요소저장 : 현재 진행방향, 진행방의 오른쪽이 0인지(이전 진행방향으로봤을때 우측방향부터 검사(네방향중.네방향만 생각해서 비교해보면 더 쉬움) ) 왼쪽이 0인지  저장 -> 그 방향부터 8방향검사 
    ## -> 그 진행방향의 오른쪽부터 검사. == 이전 진행방향 + 시계방향 으로 다음 네방향검사
    
    # (direction_index + ) %4 # 시계
    # (direction_index - ) %4 # 반시계
    # count가 0,1이면

    # 자신1_좌0우1 or 자신1_좌1우0 # 즉 양쪽이 다른거 #다음 으로 갈 수 있는 네 방향 중 그놈의 상하or(회전이라)좌우값이 다른거 
    dx, dy = [1,0,-1,0] ,[0,-1,0,1]# 그냥 dx~dy아예 전체바꿔도 ㄱㅊ
    check_dx, check_dy = [-1,-1,-1,0,0,1,1,1] ,[-1,0,1,-1,1,-1,0,1]
    # - [bfs 사용 : 미방문 체크~!~!~!~!~!~!] 바로 떠올리기  
    q=deque( [  [characterX, characterY,0, 0,1]  ]  ) # - !초기값 막설정안됨 일단 두지마 코드길면 놓친다 ## 첫 시작점에서는 일단시계방향으로봐도됨
    visited[ characterX][characterY]=1 # - ! 대입할 때 == 머임. = <-> ==주의 사용
    
    while(q): # 두경로 : 양쪽 다른 거 찾으면 처음엔 자동으로 두개로 나옴
        x,y,count,  direction_i,counterwise= q.popleft() # - popleft는 기왕 v로 받자. 알고리즘 설계 상 어디 위치인지 훨씬 명확하게 그려짐
        #! 원래 v 리스트로 쓰던거 풀어쓰다가 그런거긴한데 그래도 여기서 보통 nx는 안썼었다.
        # print(q)
        
        # (direction_index + 1,+2, ) %4 # 시계
        # (direction_index -1,-2, ) %4 # 반시계
        # ->(direction_i +counterwise*( i+1) ) %4  # 현재방향 말고 오른쪽 방향부터라 
        if x == itemX and y == itemY : # - [최소값] 문제 케이스 : [while q & 탈출조건_목표 도달 지점].(첫도달==자동 최소값상태)
            # - & q의 요소에 저장해뒀던 distance를 최소값의 의미로 저장
            answer=count
            break
            
        for i in range(4): # 움직 가능 방향
            # - 디버깅 : 상황_ㄷ자에서 안쪽으로 맞게 먼저 가는데, 건너뛸 위험이 있던 곳의 distance가 그 안쪽으로 맞게 먼저 간거랑 같은 distance를 가지네
            #   + ! 네 방향 중 한 방향으로 이동 가능했으면 break해야함 동시에 두경로로 못가.(처음 제외)
            
            # 부모 방향의 다음 시계/반시계 방향으로 한칸 씩 가기
            i=(direction_i +counterwise*( i+1) ) %4 # - !네 방향에서 부모의 counterwise값을 사용하려고 했는데, 아래에서 첫 출발 땐 두 자식에게 다른 counterwise로 업데이트 하다가 값 순서 섞임. v[]로 사용이 나을듯. 부모노드의 값을 업데이트 하진 않을테니까. q의 요소 많아져서 인덱스가 가진 의미 헷갈리면 : v 리스트, v_info 리스트 두개로 나눠.  # 1, 2, 2, 1 
            nx=x+dx[i]
            ny=y+dy[i]
            # - 출력했을때 bfs순으로 거리 같은애들 먼저 pop돼서 뜨는거 빨리 포착했어야
            
            # 4방면이더라도 검사했던 놈 굳이 다시볼? 8 ? 상수배무시?
            # if x== 3 and y==5 :
                # print('direction_i',direction_i,'i',i) # 0,3  | i는 시계방향이니까 그 다음인 1돼야하는데
                
            # 주변에 0있는 거 말고 2있는지임. 방향은 direction_i로 해줬음
            
            
            # 아 모든 모서리 2로 했었으면 내부에서 튀어나온 모서리 생격버리지. 그래서 내부를 다 통일했던거 <-> 8방검사(들어간모서리 8방검사 불일치. ) & di방향.  완전내부에
            ## <-> x값, y값들 set에 넣고 거기에 잇는지. 
            ## -> 2로 그 시계/의 반대방향으로만 계속 검사하기엔떨어져있는부분 건너뛰어버림. 안쪽으로 돌아야함.
            if 1<=nx<=50 and 1<=ny<=50 and visited[nx][ny]==0 and amap[nx][ny]==2: 
                # ndx,ndy= nx+dx[(i+2)%4] , ny+dy[(i+2)%4] # i가 0,1이면 dx방향으로 움직인거라 dy방향이 다른지 확인
                # if amap[ndx][ndy]!=amap[-ndx][-ndy] : 틀린 규칙. 특정복잡 예제의 모든케이스에서도 안맞음.
                
                # can_go=True
                # can_go=False
                
                
                # - [8방] : [한계] 사각형 한쪽 길이 1일 때 맞는 이동 위치인데도 내부값1근처에 없음  | X_'0'검사는 외부와의 검사라 아님(특별케이스 ㄷ케이스 ). 내부와의가 맞음. 
                # for j in range(8): # 2방에서 -> 8방 중 0 있는지
                #     if amap [ nx+check_dx[j]  ] [ny+check_dy[j]   ] == 1:
                #         can_go=True
                #         break
                
                # - 뇌에 그린 ['규칙'알고리즘] : 가장 복잡한 예시의 모든 선에 따져봤어야함
                
                
                # - 튀어나온 모서리 해결했어도, ㄷ에서 틀린다는 건 모서리를 건너뛴다는 거임. 이동 가능 대상은 알아도, 우선순위를 모르는 상태. -> 저 시계반시계방법
                if 1: # can_go==True:
                    # - 개복잡한 설정해야하는 규칙_기왕 다른 방법 생각해서 구현하자 _ count가 0인 초기값 케이스엔 두 경로가 있어서 counterwise를 부모로 받지 않고 초기화 
                    if count ==0: ## 가는 방향의 왼쪽이 0인지==가는방향에서 시계방향으로 한칸 간곳의 맵값 1임 / 0임 
                        # print("current,",i, " [ & counter]",(i+1)%4,  )
                        # print( '000. 현재방향', i)
                        # - 더러운 수식은 #$로 해놓고 오답나오자마자/제출전에 바로 확인을 해야지. 헷갈이나 확인 필요 정도는 #~
                        # - ㄷ의 해결을 위한 시계/반시계 규칙이 모든 케이스 커버하는 알고리즘인지. [첫 시작이 코너일 때] 못하네.-> 둘다 -1 저장해버림
                        # - [[표기]_나중 #_코드의 큰 의미 ##_세부 코드의 의미 설명 ###_다른곳에서 적었던 내용 가져옴
                        
                        
                        # - 굳이 생각한 모든 m을 구현하려 할 필욘 없지 오답 구체화 패쓰. 부모나 자식이 코너일 때
                        ''' 첫 두 가지 경로에서의 1/-1 지정.  어떤 걸 시계 방향/반시계방향으로 할지
                        # - 코너 개번거롭네 8방에서 시계/반시계하는 방법도 나았겠다 / 부모 자식 중 코너 아닌애로 찾아서 걔의 temp_counter값을 이용할 수도 있음( 코너 판별 = 8방검사 or 근처 2 )
                        
                        # - 4방향중 내부 방향인 곳 먼저 돌아야해서(ㄷ)
                        # - '자식'(이전/현재라는 것보단 부모/자식이 의미 엄밀하고 안헷갈리는듯)의 왼쪽이 0 : 시계(외부가 아닌 내부 방향으로 가야해서) / 자식의 오른쪽이 0 : 시계 ## 길이 1일 수 있어서 외부값 기준으로 해야함 # - 머리에 : 직진하는 부모 왼쪽이 내부일 때 왼쪽이 외부일 때 케이스 포괄하는 거 
                        #   + [한계 : 코너가 부모일 때] : 부모말고 자식에서의 조건 -> [ 자식이 코너일 때도 있음  ]
                        #   + counterwise 계승을 계속 저걸 따지는 방법도 있으련지 
                        ### 현재 진행방향, 진행방의 오른쪽이 0인지(이전 진행방향으로봤을때 우측방향부터 검사(네방향중.네방향만 생각해서 비교해보면 더 쉬움) ) 왼쪽이 0인지  저장 -> 
                        '''
                        
                        temp_counterwise=1 if amap[ nx-1 ][ny]==0 else -1 # - amap의 끝 경계에서 꼬이면 amap 패딩 ## 자식 기준
                        #temp_counterwise= 1 if amap [x +dx [(i+1)%4] ] [ y+ dy[(i+1)%4] ] ==1 else -1   ## 부모 ?
                        q.append( [ nx,ny,count+1, i,temp_counterwise ] )
                        
                    else :
                        q.append( [ nx,ny,count+1, i,counterwise ] )
                    visited[nx][ny]=1 # - [[visited 체크인 위치 & bfs]] : dfs는 넣을 때 해야하지만 bfs는 선입선출이라, 뱉을 때 하든 넣을 때 하든 괜찮음. 코드 한줄 더 유무 고려보다는 둘 다 넣을 때 해야 실수 안 하고 암기 편 함. # 이 코드 상에선 실수로 한 좌표 정도 bfs에 한 번 더 들어간다고 해도 최소값부터 나오면 while탈출이고 선입 선출인거라 결과에 큰 영향 없을 것임(거리 정보를 q에 안 넣고 특정 전역데이터를 갱신하면서 하면 영향감)
                    
                    if count : # count가 0이면 두 경로라 break 하면 안됨 모든 2 가야함
                        break
    
    return answer

# - 세로 길이 1,2, 3, 4
# 좌표값 1~
# 직사각형이 1개 , 2개, 3,4개 -> 4개까지 밖에 없네


# - 3h
#   + 방법 세네가지나 끝까지 구현해버림. 알고리즘 구현했는데 특정 케이스에서 부족한 부분 있었음 
#     + -> 다른 방법으로 전환 or 그 특정케이스 해결하는 규칙 예시 보면서 찾아서 구현하기  그 짓을 반복했는데 전환한 게 될 줄 알고 이전꺼로 돌아가기 어렵게 해둠
''' =>
    + '방법 전환 시' : def 함수 내에서 조금씩 수정하지 말고, 변수 한 두개 바꾸는 거여도 걍 아래에 통째로 복붙해놓고 방법 써놓자.?  <-> or 주석 때 mk로 써둬서 검색함으로써 빠르게 이전 방법으로 수정할 수 있게 해놓든. 디버깅하면서 공통 부분 오류 개선 될 땐 이게 나음
    + '방법 mA, mAA 큰 조건흐름, [장점][단점][한계]'는 'def함수 아래'나 '위'에 쓰자.
      + 이유 : 나중에 알고리즘적으로 부족한 케이스 및 부분 발견했을 때, 다른 방법으로 전환했다가 돌아오기도 하고, 코딩 시 bfs로 빨리 될 거 같은 알고리즘의 부족 부분 해결해나가는데 그 때 뭐였는지 찾을 수 있어야함.
      + 이유 : 함수 내부에선 원하는 내용의 주석 다시 찾기 어려움[코딩 시엔 다른 거 치우고 글자 더 작게?]. 코드 길어지면 코드 사이에 주석도 많음
'''    
#     + 예시만 보며 그 예시에서의 규칙찾기는 후순위인 게 나을듯. 단순 예시에서는 놓치는 게 있을 수 있음
#   + bfs 느림
#   + 알고리즘 적으로 예외있는 거 구현하는 데에 시간 많이 씀. 규칙은 특히 더, 논리나 예제에서 확실히 다 검사후 한 알고리즘 구현


# - 다른 m도 같은 값의 오답이 나올 수 있음. 오류별 원인 아래에 적어두기. 오답 17_정답19 : 처음에 두 경로 중 한 개만 가버림

# - 다른 사람 풀이
    # - 방법 : 문제는 최소 거리 탐색인데 어차피 갈 수 있는 경로의 대상이 '2개'밖에 없음, '두' 경로 밖에 없고 특정화 가능해서 bfs 안쓰고 min 활용 가능
    #   + min ( (모서리 따라서) 한 방향으로 도착점까지 간 거리 , (모서리 따라서) 한 바퀴 돌 때의 거리 -( 모서리 따라서) 한 방향으로 도착점까지 간 거리)
    #   + 난 bfs 구현은 성공했으니 이번 문제는 bfs라기보다 구현? 문제 특정, 이동 관련 구현 부족? & bfs 느림 [문제 상황에서 bfs 쓰일 곳 빠르게 알기, 문제에 맞게 빠르게 구현, 오답 시 출력 보며 (디버깅하며) bfs 맞게 돌아가고 있는지 빨리 알 수 있기]
    
"""Solution code for "Programmers 87694. 아이템 줍기".

- Problem link: https://programmers.co.kr/learn/courses/30/lessons/87694
- Solution link: http://www.teferi.net/ps/problems/programmers/87694
"""
import itertools
def is_movable(cur_x, cur_y, next_x, next_y, rectangles):

    # - 현재 위치와 다음 위치의 평균. .5일텐데 그 값을 이용해서 세밀하게 대소관계(위치관계) 비교
    #   + <-> 내 알고리즘에서 부족했던 부분도 이것처럼 정수가 아닌 세부적 칸화로 했으면 해결할 수 있었겠네. ## ㄷ주의 난 .5대신 모서리값은 업데이트 안하고 내부만 업데이트해서 밖을 옆으로 둔다/모서리 위에서 돈다는 의미로 풀려고 했음
    x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2 # - 중간값 검사 : ㄷ자 에서 건너편 모서리로 건너뛰기 방지됨. ##오 차라리 현재 위치와 다음 위치의 평균값으로 이동가능한 위치인지 검사. 반절의 위치를 다 저장할필요 없이 반절의 위치를 '검사' #   + 모서리 경로로 이동 = 모서리 값을 가지는 꼭짓점을 건너간다기보단 그 사이 값도 모서리 값
    
    
    # - 이동할 좌표인지 검사 : (사각형의 모서리에 있는지 & 사각형의 모서리 '경로'인지(건너뛰기 X) ) : 검사 대상인x 좌표와 y좌표 중 한 좌표는 사각형의 꼭짓점 좌표 중 1개와 같고, 나머지 좌표는 사각형의 해당 좌표 범위 이내
    
    
    #   + O( *N) <-> 알고리즘 부족한_O( +N) 난 모서리 영역 관계 관련 검사할 때마다 좌표마다 모든 사각형 돌기보다, 처음에 사각형 한바퀴만 돌면서 amap에 모서리 좌표 저장해뒀음. 
    
    #   + (m_B)근데 모서리2/내부1로 한번에 저장하면 뒤 사각형의 모서리가 내부값이어야하는데 모서리 값으로 튀어나와있음.  
    #     + [장점] 모서리 위치 정확히 알면 이동 가능한 곳을 알기 위해 개쌩쑈 안해도 됨 . m_A대비 이 장점을, 이 방법 생각했을 때 머리에 스치는 정도가 아니라, 방법 떠올리면 확실히 장점을 바로 인지할 정도로, 알거나 적어두기 [단점] 튀어나온 테두리가 있는 amap -> 대충 떠올린 방법들 중에 in도 적었었는데 in으로 모든 사각형 다시 재검사 해서 해당 좌표가 튀어나온 모서리인지 아닌지 확인할 수 있음. 실제로 제대로 머리에 구체화 및 활용을 안/못했음. 꼭짓점 4개 방법에서만 in을 검사하는 게 아니라 모든 검사 대상 좌표에서 모든 사각형에 대해 in으로 검사해도 됨. 너무 specific 규칙 찾기를 우선적인 방법으로 했나. 시복 내이면 [코드로 구현하기 쉬운방법] 생각하기.  
    
    #   + (m_A) 모서리 말고 내부만 1로 저장하면 가능해지는 게 있는데 그럼 모서리 여부 검사를 따로 추가해야함. ㄷ자일 때 주의. (mAA) 모서리 미업데이트= 경로의 옆이 내부1 & 자기자신 0. 구현하다가 전환 [단점] 사각형 한 쪽 길이가 1일 때 amap이 백지화돼버림 -> 모서리도 색칠해줘야함 -> (mAB) 모서리도 내부처럼 업데이트_ [단점] ㄷ자일 때 평범한 이동알고리즘에선 모서리인지 구별 못함. -> 칸 반절 더 쪼개서 업데이트는 구현안해봄. amap을 두배로 하여 반절의 위치를 다 저장할필요 없이 현재 위치와 다음 탐색 위치의 위치를 '검사'해서 해결가능
    
    #     + [장점]초기에 맵값설정 쉬움 (일단 빠르게 떠올린 방법보다 그 후 코드의 단점도 고려하하고 방법 선택하여 구현) [단점] 이동 알고리즘이 개번거로워짐('내부값 옆, 근처로, 방향성으로 돌기'). 그리고 근처로 돌아도 괜찮은가?는 예외케이스 발생하기도 쉬움. 규칙찾고 괜찮은지 하나하나 점검해봐야해서 구체화할 게 많아짐. m_A는 모서리2/내부1만 잘 설정해놓으면 이동 더 쉬움. 엄밀하고 규칙찾을게 없음. 
    #   + 알고리즘 머리에서 구체화하는 속도도 부족한가. 아이디어들이 난잡하게 흩어져있음. => 문제에서 필요한 요소별 아이디어로 정리?
    
    is_on_any_border = any(
        (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
        for x1, y1, x2, y2 in rectangles) # - : any( _ or _ for  ) # - in은 생각했었구, a< x< b가 in range보다 나음
    
    # - 사각형 내부인지 검사 : 내 m_B의 문제는 내부에서 "튀어나온 모서리" 였음 -> 여기선 탐색 대상 모든 좌표에 대해서, 전체 사각형 다 검사하며 내부인지 검사) | 튀어나온 모서리일지는 2bit로 해결 '모서리값인 순간 있는지' '내부인지'
    #   + 여기선 탐색할 좌표마다 모든 사각형을 검사하긴 했는데. 내 amap에 이 아이디어를 녹이면, m_B[모서리2내부1]에서 amap값 설정 시 모든 사각형을 한 번 더 돌며 이번엔 모서리값은 냅두고 내부만 1화하는 걸로 해결가능
    
    is_inside_any_rect = any(
        x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangles)
    return is_on_any_border and not is_inside_any_rect


def solution(rectangle, characterX, characterY, itemX, itemY):
    
    # - 현재 위치, 이전 위치 저장
    cur_pos = (characterX, characterY)
    prev_pos = None
    

    for dist in itertools.count(): # - 그냥 while로 break만날 때까지 cnt증가하는 거랑 똑같음. 코드 단순화. while (1) & count =~ for _ in itertools.count() 
        
        # 초기값인 경우를 제외하고 자기 자신으로 돌아왔을 때 그 거리를 저장 후 break
        if cur_pos == (characterX, characterY) and prev_pos:
            perimeter = dist
            break
        
        # 목표물을 찾았을 때 아이템까지의 거리 저장
        elif cur_pos == (itemX, itemY):
            dist_to_item = dist
        
        # - 특성화한 방법 상 한 경로만 가면 됨 & movable이 문제에 의해 이동해야하는 유일한 위치만을 알려줌 : 네 방향 중 갈 수 있는 곳 있으면 바로 break.
        # - dx, dy : 아래처럼 쓰는 것도 편하겠다.
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)): 
            next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
            
            # 탐색하는 위치가 이전위치와 다르고 갈 수 있는 곳이면 : 그 위치로 이동하면서, 이전 위치도 업데이트
            if next_pos != prev_pos and is_movable(*cur_pos, *next_pos,
                                                   rectangle):
                prev_pos, cur_pos = cur_pos, next_pos
                break
    return min(dist_to_item, perimeter - dist_to_item)

