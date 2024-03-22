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

def dfs(v):
    if visited[v] == True:  # <-> 미방문으로 한줄처리 체크법이 낫다. ((첫 번짼 어차피 미방문이고, 그후로는 애초에 미방문  조건에서 호출하는 게 나음))
        return 0  # 이 노드 따라 흐르지 않도록.
    print(v, end=' ')
    visited[v] = True
    for d2 in lines[v]:  # <->[1]Good_for w in sorted(adj_list[n]):
        dfs(d2)


# - 조건에서 안 그런다는 말 없으면 해야지 (( X _점선 정보가 중복으로 주어지는 경우, 뒤집어서 주어지는 경우 굳이 안 처리함 -> 해야지 함 이후 문제 중에 있음))

from collections import deque

def bfs(v):
    queue0 = deque([v])  # - 요소 넣고 시작
    visited[v] = True

    while (queue0):
        v = queue0.popleft()
        print(v, end=' ')  # - 출력 : append하는 두곳 보다 pop할 때 한번이 나음 / 큐 선입선출이라 어차피 동일한 순서 & 큐 빌때까지라 어차피 끝까지 뺌
        for a in lines[v]:  # 2 3 4
            if not visited[a]:
                # <-> if visited[a]==True :
                #     continue # 이 노드 따라 흐르지 않도록.
                # print(a, end=' ')
                visited[a] = True  # - ! a로 해야하는데 실수로 복사해온 코드 v로 그대로 해버리네.
                # + 1) 복사해왔을 때 코드 글자 단위체크 2) 변수 이름에 의미 필수 ( 심한 temp 아닌 이상 )
                queue0.append(a)


dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)

# - 1h : 파이썬 기본 사용 체크 조금 / 오랜만에 bfs dfs 의미 떠올리기 조금
# > 1) visited, 0.1) 그래프의 양방향성 저장 0.2) 행 별 sorted (<-디버깅) 등

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

