# - 문제집_DFS+BFS 필수 문제_촌수계산_https://www.acmicpc.net/problem/2644



# * 없으면 -1
n_person= int(input())
target=list( map(int, input().split()) )# 촌 수 계산 대상
visited=[False]* (n_person+1)
n_connect=int(input())
# 부모, 자식
# - bfs dfs 케이스
# -> 최단거리/시간 느낌이라 이 문제 상황은 bfs빨라 ( dfs는 최솟값으로 구하려면 min짓해야함 )
# -> 최단 거리 : count 대신 queue에 v넣을 때 거리도 같이 넣어줌 .append( [ new_v,v[1]+1] )
# - 문제 상황_최단 거리 : '노드 당'
# -> 노드 당인 v넣고 빼는 단계에서 결과값 계산
graph=[ [] for _ in range(n_person+1)  ]
for _ in  range(n_connect):
    parent, son= map(int, input().split() )
    if parent not in graph[son] : # - 인덱스 에러 안남. -> 모든 행 빈리스트 가지게 만들어둬서 문제없음
        graph[son].append(parent)
    if son not in graph[parent]:
        graph[parent].append(son)

# - 쓸 때 알고리즘번호 쓰면서 하니까 한 방에 누락실수 없네.
queue=[[target[0],0]] #1 -1
visited[target[0] ]=True#1 -2
result=-1

while(queue):#1
    v=queue.pop(0)# - 모든 사람 거치는 순서 한 번씩 볼 필요 없으므로 3출력 관련 안함 #23

    for side in graph[v[0]]:#1
        if side ==target[1]:# 최종 타겟은 한번만 방문 탈출이라 중복불가여서 미방문체크안해도됨
            result=v[1]+1
            break
        elif not visited[side] : #2
            queue.append([side,v[1]+1])# - 3 'v'를 먹음
            visited[side]=True #3-2

print(result, end='')

# - 33m
#  + 어떤 사람 손에 든 걸 자꾸 던지며 하는 건지( 파열음? 아무튼 소리 중에서도 부조화 소리 나서 집중 흐트러지고(자리 옮김 그래도 쫌 그래서 아예 덜 편한 다른 구역으로 옮겨야 하나 고민 등) 시간 좀 잡아먹음)
#  > 이제 좀 안 던지시는듯 다행쓰 에어팟 노이즈캔슬링 필참
#  + 2)3) 핵심알고리즘 먼저 안 짜서, 매번 똑같은 거 다시 생각해내면서 하느라(문법 언어 등이 익숙한 사용 수준이었다면 입력하면서 흐름 생각만 할 수도 있을듯) 코딩 입력이 좀 더 느렸나.
# - pypy3가 더 빠르댔는데 python이 훨씬 빠르다. 코드마다 다르나. 데이터는 좀 더 모으자

# - 0.2)그래프 형성_중복체크 - 자기자신과의 연결중복은? 같으면 pass하는 걸로 해야하나 근데 그런 연결 있을 문제 설계나 상황이 없을듯(있으면 문제에서 티날 수 있음)
# - 다른 사람 코드 ( mhmh779 )
# > dfs로 푸심 : 최단거리_노드당->v넣고뺄때_v넣을때 결과값계산 / 'visited'에 거리 값 넣어주심
# n = int(input())
# a, b = map(int, input().split())
# m = int(input())
#
# graph = [[] for i in range(n+1)]
# visited = [0] * (n+1)
# for i in range(m):
#   x, y = map(int, input().split())
#   graph[x].append(y)
#   graph[y].append(x)
#
# def dfs(a):
#   for nx in graph[a]:
#     if visited[nx] == 0:
#       visited[nx] = visited[a]+1
#       dfs(nx)
#
# dfs(a)
# print(visited[b] if visited[b] > 0 else -1)

