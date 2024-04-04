# - 문제집_DFS+BFS 필수 문제_토마토_https://www.acmicpc.net/problem/7569

# 1)
# 1익음 0안익음 -1 토마토 없음
# 하루 후 , 익은 토마토 인접도 익기화  / 2차원 네방향 + 위아래
# -> 며칠이 지나면 다 익는지 최소값

# O* 결과 모두익어있었 0 모두못익-1


# 2)
# - 그래프 입력 때 익은 것 저장 -> 거기에서 꺼내며, 방문체크하며 -> '하루'(bfs) , 주변 익기화 ->
#   >'며칠 최소값' : 검사 끝난 bfs_단계count값 : v : [ 단계값_v[0]+1, 좌표 ]
#   >
# - 그래프 필요? ->대신 amap

# 3) (이틀, 3일 = bfs 단계진행)
w, n, h = map(int, input().split())
from collections import deque

#amap = [    [ []  for_ in range(n)  ] for _ in range(h)] # amap[i][j].append
amap = [   []  for _ in range(h)]  # append로 한 줄 씩 넣을거니까, 초기화는 한 차원 부족하게.
# - m1) 2차원틀 만든 후 1차원을 요소로 append해서 3차원 만들거 / 아래에서 이미 forfor n 에서 append함.
# <-> m2)1차원에 2차원을 append : 하다가 맘
# print(amap)
# - rc네모[밑상자]에서 한줄씩 append하므로 [h_가장 나중],[r],[c]순서임. append가 리스트의 가장 안 쪽이자 인덱스의 가장 뒤쪽. r,c,h아님
# ones = []
zeros=[]
queue = deque()#1_
for i in range(h):
    for j in range(n): # n이 행 수
        # - 리스트를 '요소'로 빈 2차원 리스트에 append.여러번 = 1차원 추가됨 # amap[i] : 한 층
        amap[i].append(list(map(int, input().split()))) # - 2차원 amap의 []를 가진 '[i]' 행에 append # - 맵에 저장이랑, 특정 값 찾아 저장해주는 건 따로야
        for k, a in enumerate(amap[i][j]):  # - 금방 append한 한 줄도 amap[i][j]임 not amap[i]. amap[i]에는 append된 여러 행이 있음.
            if a == 1:
                queue.append([100,i,j,k]) # - 100_거리값 0을 맵핑시킴
                amap[i][j][k]=100 # - 새로운 의미부여:아예 거리값 0~을 100번대로 맵핑시켜버림 # 원래값 0,1과 안 겹치고 문제없을 논리 생각 귀찮아서.
            elif a==0:
                zeros.append(1)
# print('temp m', temp_map) # print('amap', amap) # print('ones', ones)
# 토마토가 하나 이상이기 때문에, 아래의 각 if가 중복일 순 없음
if len(queue) == 0: # 모두 못익었
    print(-1, end='')
    exit()
if len(zeros )==0 :#  모두익었 # '토마토 없는' 것도 있음.(변수면 골라서 볼수라도 있지) 뒤늦게 알고리즘 반영했을 떄 전체 알고리즘 훑어라.
    print(0, end='')
    exit()

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
visited = [[[False] * w for _ in range(n)] for _ in range(h)]  # - 미방문 amap에였나 넣으려다 엉켜서 쌩쑈. 데이터 한 덩어리 정도는 압축하려다가 엉키지 말자.
# - 노드에 대한 거니까 visited든 amap이든에 저장 가능


# ( 결국 풀어내는 시간 때문에 m1 진행했다가 시간 복잡도 시간 초과 떠서 m2도 해서 바꿈 핳ㅋㅋ)
# - m2 전염 & '각 ones에 대한 확산이 같은 단계씩' 이 동시에 되도록 = 큐 [같은 레벨 순서로 수행완료[자신의 자식 처리(코드거리연산 및 큐에 삽입)및 방문]함~
#    자기의 자식들 삽입은 하지만, 그 자식들의 자식은 그 윗 형제들 다 pop되고 난 후 pop됨]
#   [큐에 먼저 ones 다 넣어 & 큐 논리(선입선출로서, 먼저 들어간 놈들의 1차 자식들만 일단 넣고, 그자식들의 자식들은 추후에 출됨 )]
#   >    & 노드 당 총 한 번만  보는방법
#   > ones만큼 큐에서 빼기=>그니까 그걸 큐에 우선하여 먼저 다 넣어주면 됐음.'선입''<-선출' ( <-> 큐 i화방법/for을 먼저 생각했었음)

# - m1 one마다 미방문 초기화하며 미방문봐 & 각 one에 의한 노드값을 min으로 통합 -> 시간초과
#   > 미방문다보다가 복잡이거나 탈출을 못했거나-> 탈출손봐야
#   > 방문 위치도 다른 one은 초기화해서 보는 이유 : 그래야 더 먼놈에 의한 값으로 높아진 값이 정상적으로 낮아짐
result=0
# for one in ones:  # [
#     # bfs
#     # count =
#     visited = [[[False] * w for _ in range(n)] for _ in range(h)]  #미방문초기화
#     queue = deque( [  [100, one[0], one[1], one[2]] ]  ) # 1
#     #~ visited[queue[0][1]][queue[0][2]][queue[0][3]] = True
#     amap[queue[0][1]][queue[0][2]][queue[0][3]] = 100 # 방문이라서 0이 아니라 첫 시작애들이라. 당사자들이라 0 주변애들부터가 1 -> +100번대로 변경
#     # print(visited)
visited = [[[False] * w for _ in range(n)] for _ in range(h)]

# - 선입선출이라 바로 아랫 줄에서 for에서 ones 한개씩 넣는거랑 미리 다 넣어있는 거랑 달라. 그렇게 넣으면 ones-one에 대해선 dfs처럼 돼버림
if(1):
    while(queue):  # - while(큐) 편한점 2. 종료조건 따로 안 계산해도 됨.
        #for i in range( len(ones)) :
        v = queue.popleft()
        # queue에 들어가있는 첫 형제들 visited미리는 안해줬었네
        # - ( 3_노드 각자의 이름 단독 출력 필요 없음 )
        for i in range(6):  # 4 - 기본폼_인접그래프 ~~ 지도_사방방향
            x, y, z = v[1] + dx[i], v[2] + dy[i], v[3] + dz[i] # 걍 x,y,z를 dimension순서로 사용했음
            # X_인덱스 결과시 인덱스로 말고 숫자로 계산한부분도 있음주의

            if -1 < x and -1 < z and -1 < y and x < h and y < n and z < w and visited[x][y][z] == False and amap[x][y][z] != -1  and amap[x][y][z] != 1  :# 5미방문&& # 지도_주변_인덱스체크 함꼐 # 토마토없는 -1 위치는 미방문이어도 가면 안되니까
                queue.append([  v[0]+1, x, y, z])  # 6
                visited[x][y][z]=True
                amap[x][y][z] = v[0] + 1 #m2써서 min필요없음 #압축때_ visited[x][y][z] = min(   visited[x][y][z]   ,  1 + visited[v[1]][v[2]][v[3]])  # 6미방문만 오니 중복누적될일 없음

# 얘는 그냥 "전염"과 다르고 "구별된 노드"마다의 & "스텝 감염의 정도가 달라"[거리]


# case : 남은 거에 -1이 중간에 껴있으면 다 익기 실패임
for i, a in enumerate(amap) : # - 걍 지도를 업데이트 (할걸. 결국 지도 업데이트로 바꿈)
    for j,  b in enumerate(a):
        for k, c in enumerate(b): # *변수 바꿀 때 이름만 딱 덮어쓰지 말고 아래에 복사후수정해서 똑같이 옮겼나 확인해라

            # if c< 1000000 : # -1인것도 ㄱㅊ해서  / -1인놈은 어차피 1000000이긴하겠다.
            #
            #     update=max(update,c)
            # elif  amap[i][j][k]==-1 : # 1000000이지만 ㄱㅊ 사과없는놈이라
            #     pass
            #else:
            result = max(result, c)
            if amap[i][j][k]==0 : #애초에 100번대 처럼 다른 걸로 맵핑 # 0이 남아있다면. (방문 안해져서 0값)
                print(-1,end='')
                exit()
print(result-100, end='')

# -  4h30정도? : 풀이 및 질문 봄 근데 나랑 알고리즘 똑같은 거 아닌가 엣지 케이스떄문인건가 모르겠어서 그걸로 내거에 적용하여 해결한 부분은 없음.
# > 대신 이 방법이 틀리지 않았다 + 약간의 내재적 기억 힌트로 분석 및 알고리즘 분석 시 영향 있었을 수 있음
# > 3h30: 급하게 풀어서 그런가 잠을 덜 자서 그런가 너무 실수 오만가지했다( 동일한 내 작성 알고리즘 변수이름 바꾸는 거 등등 내가 금방 했던 것도ㅎㅋㅋ오만가지)
# > 1h 33m : first # 틀렸당 엣지케이스 문제인가

# - **수정 후 알고리즘 찬찬히 쭉 훑기/최소한 그 변수 있는 곳 근처는 다보기 ((빨리 풀려고 조금씩 수정하고 후룩 훑다가 그 수정이 다른 곳에 반영 안되고 그럼))  # > 그놈의 내가 문제 풀어내는 시간! 내가 느리긴 하지 ㅎㅋㅋ
# -> **그건 뭐 하다보면 자연스레 빨라질 테니, '풀 시간이 급해서'라는 이유로 알고리즘 설계 95퍼 이하 확률이어도 넘어가지 말자.
# > (( 요새 푸는 시간 줄이려고 (낮은 단계부터 푸니까 시간복잡도 항상 너무 충분히 남고 최적화 하느라 푸는 시간만 더 들어서) ))

# - 2.때 방법 선택 및 설계를 시간 복잡도는 크게는 신경 안쓰고 했었음 ->  시험 땐 어려운 문제인지 아닌지 모르니까 기왕이면 좀 하자.
# - python=시간초과 / 복잡한 거에선 pypy가 훨씬 낫나봄

# - 다른 사람 풀이 : 알고리즘 자체의 큰 차이는 없음. 그거 더 볼 시간에 다른 거 공부가 효율 상승일듯~
