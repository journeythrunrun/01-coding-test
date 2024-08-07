# - 문제집_DFS+BFS 필수 문제_dfsbfs_https://www.acmicpc.net/problem/1260

# 0)
# 1 2 3 4
# 2  4
# 3 4
# 1)
# 탐색 가능 있 : 번호 작은 것부터 / 없 : 종료
# : '양방향'으로 데이터에 넣어놔 & 동일한 노드 출력 안됨


# 2) 조건 알고리즘 생각 및 후처리
n, m, v = map(int, input().split())  # n 노드 수
visited = [False] * (n + 1)
lines = [[] for _ in range(n + 1)]  # - 빈 리스트도 안에 []로 해야 나중에 거기에 이어서 정상 append 가능
# - *노드 1번 부터면 인덱스 자리에 맵핑시킬 땐 n+1개

# X_해당 인덱스로 건너뛰어서 어펜드 해야하기에 X [for a, b in map(int, input().split()) for _ in range(n)]

# - bfsdfs문제에서 양방향 그래프 이용할 때 자주 필요함
for _ in range(m):
    a, b = map(int, input().split())
    lines[a].append(b)
    lines[b].append(a)

for i in range(n + 1):
    lines[i].sort()


# 각 행에 대해서 전부 정렬하는 함수 따로는 없을듯  <-> X_lines.sort(key=lambda x:x[1])# [1:]로 행 빼고 행마다 정렬이 아님 #행인 인덱스는 시작노드로 맵핑했으니 마음대로 정렬하면 안돼

# - dfs : 조건 2개 & 함수 5단계
#   + 조건 : **1.1) Graph_양방향성 (행 별 sorted는 문제 조건에 따라 선택) 1.2) 중복 체크**
def dfs(v): # (함수호출 때)1-1_v먹음
    # - DFS - 미방문 체크로 실행화 ((문제 푼 후 복습용 작성)) : 한줄 줄이는 거긴 해도 직관적)
    visited[v] = True  # 1-2방문처리(먹었으니까)
    print(v, end=' ')  # 2출력 : dfs는 먹을 때 출력     ## dfs라 깊게 갈 때, 다쓰기 전에 닿을 때 먼저 출력

    for d2 in lines[v]: # 3for그래프
        if not visited[d2]: # 4미방문
            dfs(d2) # 5먹어(deep)
    # - 재귀함수 끝날 때  자동 뱉음

    # if visited[v] == True:  # <-> 미방문으로 한줄처리 체크법이 낫다. ((첫 번짼 어차피 미방문이고, 그후로는 애초에 미방문  조건에서 호출하는 게 나음))
    #     return 0  # 이 노드 따라 흐르지 않도록.
    # print(v, end=' ')
    # visited[v] = True
    # for d2 in lines[v]:  # <-> [1]Good_for w in sorted(adj_list[n]):
    #     dfs(d2)


# - 조건에서 안 그런다는 말 없으면 해야지 (( X _점선 정보가 중복으로 주어지는 경우, 뒤집어서 주어지는 경우 굳이 안 처리함 -> 해야지 함 이후 문제 중에 있음))
from collections import deque


# - bfs : 조건 2개 & 함수 1+6단계
''' 04문제
# - bfs_그래프 생성
# > 0.1) 양방향 그래프 형성폼 0.2)중복(엣지 케이스) 처리한
graph=[ [] for _ in range(n+1)]
for _ in range(n_connect):
    a, b = map(int, input().split())
    if b not in graph[a]: # - 갈 곳에 갈 놈이 이미 있진 않은지 체크 
        graph[a].append(b) # - append
    if a not in graph[b]: # 인덱스 에러 안남. -> 모든 행 빈리스트 가지게 만들어둬서 문제없음
        graph[b].append(a)
'''
''' 04문제
# - 개념 : bfs(더 빠름)/dfs 개념 암기 (( 디버깅으로 찾기보다 애초에 한방해결이 나음))
# > bfs : 조건 2개 & 함수 1+6단계
# [조건] 0.1) Graph_양방향성 (행 별 sorted는 문제 조건에 따라 선택) 0.2) 중복 체크**
# [함수] 1) v0먹어 & 방문
# [함수] [큐]3.1) While(큐) 3.2) 뱉 v=.pop(0)3.3) 출력     [그래프]3.4) for 그래프[v_자식들] 3.5) 미방문 _ 3.6) 먹어(.append) & 방문
'''
def bfs(v):
    queue0 = deque([v])  # 1-1) v0먹어 # - 요소 넣고 시작
    visited[v] = True # 1-2) v방문

    while (queue0): # [큐-1] while(큐)
        v = queue0.popleft() # [큐-2] 뱉 v=.pop(0)
        print(v, end=' ')  # [큐-3] 출력 # -bfs : 뱉고 출력 ( append하는 두곳보다 pop할 때 한번이 나음 / 큐 선입선출이라 어차피 동일한 순서 & 큐 빌때까지라 어차피 끝까지 뺌 )

        for a in lines[v]: # [그래프-1] for그래프[v_자식들]  # 2 3 4
            if not visited[a]: # [그래프-2] 미방문
                # <-> if visited[a]==True :
                #     continue # 이 노드 따라 흐르지 않도록.
                # print(a, end=' ')
                queue0.append(a) # [그래프-3]-1먹어   # 주로 [r,c,d거리_dis[a]+1] 같이 저장. # 부모 +1
                visited[a] = True  # [그래프-3]-2방문 # - ! a로 해야하는데 실수로 복사해온 코드 v로 그대로 해버리네.
                # + 1) 복사해왔을 때 코드 글자 단위체크 2) 변수 이름에 의미 필수 ( 심한 temp 아닌 이상 )                
'''
                # - 최단 '경로' 
                # 여기서 a위치의 부모 위치 저장 parent[a[0]][a[1]]=v 
                # & bfs니까 유일한 방문들 중에 최단발자국도 남구나 
                # dfs와달리 거리순으로 가서 어차피 닿는 것도 최단발자취로 닿음(둘다 목표만 다른거지 어차피 미방문노드만 가긴함) 
# v1
path=[]
last=[m,n]
while(1):
    if last=[0,0] : 
        break
    new=parent[last[0]][last[1]]
    print(new)
    last=new # ((합칠 생각은 했었는데 코드가 덜직관적?))

# v2

    # 경로 역추적
    path = [] # 경로 저장을 위함
    step = goal
    while step: # step이 부모 거슬러 올라가는데, 첫위치는 이전부모 없을 거라 자동 탈출
        path.append(step) # 경로 저장 및 출력을 위한 것
        step = parent[step] # 그냥 바로 스텝이 스텝 거슬러 올라가 받는거 

    return path[::-1]  # 경로를 역순으로 반환하여 시작점에서 종료점 순으로 정렬
'''

dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
# - 1h : 파이썬 기본 사용 체크 조금 / 오랜만에 bfs dfs 의미 떠올리기 조금
# > 1) visited, 0.1) 그래프의 양방향성 저장 0.2) 행 별 sorted (<-디버깅) 등

# - **개념 : bfs dfs_코드개념_위 기본 꼴 보라**  / 4번코드도 유사

# - 다른 사람 코드[1] bhjadmb21_실행 속도 3배 이상 빠름
# > 차이 큰 지는 모르겠는데, 행 당 정렬 : 함수 내에서 사용 시 for w in sorted(adj_list[n]):
# > deque의 popleft()대신 일반 리스트의 pop(0)쓰심. 책_deque가 범용성 기반 유용이겄지?

# def dfs(n):
#     visited[n] = True
#     dfs_list.append(n)
#     for w in sorted(adj_list[n]):
#         if not visited[w]:
#             dfs(w)


# def bfs(n):
#     visited[n] = True
#     queue = [n]
#     while queue:
#         v = queue.pop(0)
#         bfs_list.append(v)
#         for w in sorted(adj_list[v]):
#             if not visited[w]:
#                 visited[w] = True
#                 queue.append(w)


# N, M, V = map(int, input().split())
# adj_list = [[] for _ in range(N + 1)]
# visited = [False] * (N + 1)

# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)

# dfs_list = []
# bfs_list = []

# dfs(V)
# visited = [False] * (N + 1)
# bfs(V)

# print(*dfs_list)
# print(*bfs_list)

