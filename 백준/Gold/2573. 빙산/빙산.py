#1)
# - 1년마다 그 칸에 동서남북 네 방향으로 붙어 있는 0이 저장된 칸의 개수만큼 줄어듬



# - 0화. max(0,
# -> 0보다 큰거 targets에 저장. targets(미방문)에서 하나로 bfs&bfs돌며 visited화 : bfs돌고 나왔는데 targets에 미방문_0이 아닌거로 하기엔 다음꺼 하기 위해서 이미 처리한 놈들 0으로 하긴X_ 있으면(굳이 최적화 하기엔 이미 시복이내.) : 해당 년도.
# -> 한덩어리씩 사방 검사 진행(0있으면 자신-1, 자연수이면 위치 append. 사방검사 다 한 후 0보다 크면 다음 targets에 append. ). 다음덩어리로 가면 해당 년도. 

# > 동서남북 연결
# -> 한 덩어리 빙산이 두 덩어리 이상으로 분리되는 최초의 시간 / 다 녹았는데 (없는데)도 안됐으면 0

# 2) 





# - 2) n*m=90,000 / 빙산은 만개이하있음 : O(nlogn) : / worst O : O( 90,000 * #years + 십만_   최대값 * 빙하개수(맵개수가 아닌이유는, 처음에 빙하애들만 체크한 후 걔들로 bfs에 넣으며 돌리기 때문임) : 십만  / 시간은 10 *가 아니긴함. 전체 방문의 시각으로 봐서 *한거고 for문기준으로 *한 거 아님. 첫겉for이10보다 훨씬 크긴 한데, 그 대신 항상 모든빙하 다도는 건 아님.(매 시각 모든 빙하 다돌면 그게 코드상에서도 for_10*가 되는 케이스)   )
# - ! 칸에 들어가는 값 10이하이므로 겉껍질for나 최대 시각이 *10은 아님
from collections import deque
import sys # - !
n,m = map( int, sys.stdin.readline().split() )
amap=[ list(  map( int, sys.stdin.readline().split() ) ) for _ in range(n) ]


# - 근데 이론적으론 *상수 날리는 거이긴 한데 *9 수준이면 거의 *10수준이긴 함 ㅋㅎ. n**2 <<--> 숫자를 기준으로 역으로 가기의 차이도 있음

visited=[ [1]*m for _ in range(n)  ] # 벽 미리 1화
answer=0
dr,dc=[0,0,1,-1],[-1,1,0,0]

def bfs(v, visited, amap):
    q=deque([ v ])
    # - ! 보통 함수 분리를 안 하고 풀었어서 n,m 자동으로 없어서 처리하는 건 뒷박자긴 하네  
    n=len(visited)
    m=len(visited[0])
    visited[v[0]][v[1]]=1 # - ! 급하게 코딩해도 마음 속에서 하나하나하기? 아니면 하다보면 자연스러워지는 건가? ,v[1] ]=1
    pass_set=set( ( v[0] *m + v[1], ) ) # - 2차원의 1차원화_r*n+c에서 n 아니고 m이쥬@!!!!!@!@!@!@!@!@!@! 생각하고 하기. 오히려 쉬운 거라 안다 생각하고 후루룩 쓸 때가 위험할 수도.
    # - set ( (1)은 그냥 숫자의 괄호로 받아버리고 (1,)로해야 튜플로 받음 )
    while(q) :
        r, c = q.popleft()
        for i in range(4) :
            nr, nc= r+dr[i], c+dc[i]

            # - ! nr에서 = 추가했으면 뒤에도 차.근.차.근. 차근차근차근차근차근차근차근차근차근차 근의차이..ㅋ.. 이렇게 생각하면 차근차근하려나
            if 0<=nr<= n  -1 and 0<=nc<=len(visited[0])-1 : # 어라 아까랑 똑같은, 오히려 마지막줄 바껴서 아까가 맞네check. 근데 첫빵만 마이너스된거 없어서 그럴수있음# 근데 여기에 visited검사하면 물로 0화되는게 안됨. 물은 재 방문해도 된다니까. 첨에 그래서 없앴던.'그냥 0 말고 이번 턴에 0이하가된 방문애가 문제인거임'  and visited[nr][nc]==0: # 조건 뺄때 : 추가하는 거 주의 : # - and visited[nr][nc]==0 :# 벽의 0도 이용되어야함. # 이 미방문처리는 빙하였던 애들ㅇ에 대해서만임. 0짤말고 # and amap[nr][nc]> # 이미 미방문인 애들만 _ 이라기엔 그 주위보는 건데 amap 다르게 이용
                # - 바다인 0에서 안쪽의 빙하 녹이는 게 효율성 나을 수 있긴함. 그래두 시복 이내라 빨리 코딩하는 걸로 풀었음 # - 빙하복습?
                # - 조건문 설계 주의해야함. 특히 시간에선 동시에 녹일 때 pass_set중요함
                if amap[nr][nc] <=0 and nr*m+nc not in pass_set  : # - pass_set : 이번 타임에 녹아서 0이하가 된 빙하가, 근처 빙하에 바다처럼 작용하지 않도록 이번 타이밍에 추가된 빙하 pass_set에 넣어둠 
                    amap[r][c]-=1 # - 나중에 혹시 몰라서 0으로만 내리지 않고, -1씩 내려서 정보 쫌 보유 & 대신 조건문을 0이하화
                
                elif amap[nr][nc] >0 and visited[nr][nc]==0:  # - 미방문했던 놈만!  0은 방문했던놈 방문해도 되지만 빙하는 아님 # - 미방문인 애들로 들어오면 무조건 아닌가? 란 생간은 잠깐이어도 안 스치는 게 맞는건가 점검차의 비판적사고인건가.. node가 처음에만 임의의 미방문노드이고 그 후론 일반적인 전체탐색처럼 미방문체크지. 문제가 이것저것 덧붙여있지만 그 부분은 일반적bfs랑 똑같음
                    q.append( [nr,nc])
                    pass_set.add(nr*m+nc)
                    visited[nr][nc]=1
                    
## amax=0
# - ! after_year최대 10,11번 넘지 ! max층까지 아님. 층으로 녹이는 거 아니라 옆에서 녹이는 거라서 다름.
for after_year in range(1, 10*29*29+2): # - 더이상 할 거 없을 때의 탈출 조건 추가했기에 적당히 최대값 잡아줌 # +1은 range, 또 +1은 알고리즘이 다음 after_year에 영역 분리를 체크하기 때문임
    node=0
    
    for i in range(1,n-1):
        for j in range(1,m-1):
            if amap[i][j]>0 : # - 빙하들만 미방문화 . 바다는 어차피 방문할 필요도없어서 방문했다침
                visited[i][j]=0
                node=(i,j)
            ##amax=max(amax,amap[i][j])
            
    if node==0: 
        # - 문제 조건에 의해 무조건 빙하 한 덩어리가 '처음엔' 있는 거 맞음. 나중에 반복문에서 다 없어지면 node가 없을 수 있음.
        #   + 변수 사용하거나 넣을 때 그게 값이 없을 경우 생각해라.  
        break
    bfs(node, visited, amap)


    for i in range(1,n-1):
        if answer == after_year : 
            break
        for j in range(1,m-1):
            if visited[i][j]==0: # 0보다 큰 빙하만 visited을 0으로 해놨고, 한 노드에서 시작해서 사방빙하bfs돌며 visited을1로 해놨기에, 분리돼있으면 visited 0이 남아있을 것임. 
                answer=after_year
                break
    # - 정답에 너무 무의식적으로 맞추어 생각하지 마삼. 정답이 뭐라하든 정답에 생각이 영향받아서가 아니라 이론적으로 A라고 확실히 할 수 있기. answer-1 등
    
    if answer ==after_year :## or answer == amax+1 : ## -2머임. +2했던거에 -1이었으면 모랄까 ㅜ  # '정답'이 (0,) 1인케이스 after_year의 첫 값이 잖슴...
        break
    
# - 디버깅
#    + 정답 때의 amap까지도 맞게 출력됐는데 visited가 다 1화돼있어버리네. -> answer-1
#    + [같은 년도[feat주의] ]에 0이 된 애들(visited 0에서 1화, amap 0이하 돼있음. 0인애들은 첨부터 visited 1임. 방문하지 않았던 nr nc를 사방검사하면, amap이 0이 아니라 미방문으로 들어왔던 거라 ㄱㅊ)이 옆에 영향을 줘버림.(->pass_set) # (당연한걸 굳이 설명?) 4방향에서도 미방문만 . 왜냐면 다행히 문제에선 미방문은 해당 노드의 값에 영향을 안줌
answer=max(0, answer-1) # - answer-1 : 이전 year의 bfs에서 2조각 이상으로 쪼개졌으면 이번year에서 그 한조각을 처리한 후  visited부분이 남게되는 거기 때문임. for에 끝값에서 귀찮아지는 건, 탈출 조건으로 처리. 그리고 answer를0부터 시작하기엔 asnwer관련 탈출조건문이랑 겹쳐서 귀찮음.
print(answer)
# 4) n,m = 3, 다 0            
# 다 사라진 경우?  그래도 visited은 처리하다의 기준임

# - 1h 20m + 왜틀리는지 모르겠어서 디버깅하다가 질문게시판 오류케이스 봄 
#   + [맥시멈 설정 주의~] 최대 겉회전 10,11번 넘지. ((ex. 10짜리가 빙하에 둘러쌓여있으면.))
#   + 시간 초과됐던 건 pypy로 변경하니 해결


# - 예전에 정리했던 거 일부 + ((초반에 낙서장 수준에서 시작했어서 정보 검증덜돼있음))
'''
- Set[셋][세트](해시테이블)
: set1= { (1,2), 4 } 
> set '화'.  : a= set (  variable )  # - 이걸로 튜플을 요소로 만드려면. set ( [ (1,3) ]) 이어야함. 다 (괄호면 안됨
: set ( (1)은 그냥 숫자의 괄호로 받아버리고 (1,)로해야 튜플로 받음 )
: 1) set1 = {hashable 자료형 }  :  입력 한개를 한 개의 요소로 받음. 
:   hashable 자료형[tuple(모든 요소가 hashable인 경우만. ) ,str,  숫자 등]만 set의 요소로 입력 가능. <-> [불변형]. list, dict, set형 요소는 안됨

: 2)        = set ( hashable 자료형  ) : 입력 한개의 각 요소를 집합의 각 요소로, 순서 섞여서 들어감
'''

# - 다른 사람 풀이 : 봤는데, 큰 시복은 같은 것 같고 
#   + 매 year에 모든 행열 다 검사한다기보다, 맨 처음에 저장해뒀던 빙하의 위치를 검사함. 빙하가 만개라 훨씬 나음. 
#   + 바다에서 녹임. 녹인 빙하의 값이 딱 0이면 해당 빙하 위치를 빙하에서 제거하고(리스트형 빙하에서 remove_항상remove하는 건 아니니까 빙하길이*빙하길이도 아니라 생각했었음. 각 빙하마다 한번 완전히 제거되면 n_((문맥상여기선빙하길이로사용중인거알수있음. 어차피 제출용으로 쓰는 거 아니고 내 공부용이라 제대로 원서에 제출한 적도 없는 링크인데 굳이 타인을 위한 것에 해야할 거 많은 내 시간을 써야하나? 나만 알아들을 수 있으면 되는 거 아닌가?_컴공과아니라 이정도 제출하면 오히려 -되는지+되는지도 모르고 오히려 정리도 안돼있음))+...+1 이라 크게는 n*n. 하지만 #years에는 안 곱해지고 여러 years에 거쳐서 n*n이라, 그 for 내에 있어도 시복으로는 바깥으로 나가서 +로 연결됨) 바다에는 추가함
#   + 어라 최적화 부분말고 큰 틀에서, 시복_ worst case에서는 remove보다 내께 나으려나. (( 물론 문제에 의해 빙하길이*빙하길이가 훨씬 작게 saturation될 수 있는지를 깊게 생각해보진 않음))

#   > ttemp등의 [0],[1]인덱스는 바다리스트에서 다음 바다리스트를 만들 때서로를 temp로 번갈아 쓰는 것과 비슷(그래서 %2하며 초기화)  
'''
from collections import deque
input=open(0).readline
def bfs(V,A,N,M,k,sx,sy):
    c=1
    q=deque([(sx,sy)])
    V[sy][sx]=k
    while q:
        x,y=q.popleft()
        for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=dx<M and 0<=dy<N and V[dy][dx]<k and A[dy][dx]:
                q.append((dx,dy))
                V[dy][dx]=k
                c+=1
    return V,c

def main():
    N,M=map(int,input().split())
    V=[[0]*M for _ in range(N)]
    sea=[]
    A=[]
    ice=0
    ices=set()
    ttemp=[[],[]] #녹일수 있는 바다 담는 리스트
    for i in range(N):
        temp=[*map(int,input().split())]
        for j in range(M):
            if temp[j]:
                ice+=1
                ices.add((j,i))
            else:
                ttemp[1].append((j,i))
        A.append(temp)
    k=1
    while 1:
        u=k%2
        D=False #얼음이 녹았는지 체크 하는 변수
        for x,y in ttemp[u]:
            P=False
            for dx,dy in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=dx<M and 0<=dy<N and A[dy][dx]:
                    P=True #네 방향중 하나라도 얼음이 접해있는 바다
                    if A[dy][dx]:
                        A[dy][dx]-=1
                        if A[dy][dx]==0:
                            ttemp[0 if u else 1].append((dx,dy))
                            ices.remove((dx,dy))
                            D=True #녹일수 있으면 true
                            ice-=1
                            if ice==0: #다 녹으면 처리
                                print(0)
                                return 1
            if P:
                ttemp[0 if u else 1].append((x,y))
        ttemp[u]=[]#바다 리스트 갱신
        if D: #얼음이 1개 이상녹았나?
            for i,j in ices:
                V,icek=bfs(V,A,N,M,k,i,j)
                if icek!=ice: #얼음덩어리 나누어짐
                    print(k)
                    return 1
                break
        k+=1
            
main()

'''