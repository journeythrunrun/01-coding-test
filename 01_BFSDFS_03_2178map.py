# - 문제집_DFS+BFS 필수 문제_미로 탐색_https://www.acmicpc.net/problem/2178

# 0)
# (1, 1)에서 출발하여 (N, M)의 위치로

# 1)
# 1 : 이동 가능 / 0 : 불가
# => 지나야하는 최소 칸 수
# ; 항상 도착 가능


# 2) 최소 : bfs _count
# - 한 노드에서 인접 1곳들 넣을때 : 같은 수 어펜드 혹은 카운팅 -> '1'위치당 최소값 저장

# * 3) 인덱스화 -1주의
from collections import deque

def bfs(v):
    track[v[0]][v[1]] = v[2]
    queue0 = deque([v])  # - [ ] 안씌워주면 한 요소 v[0] 만 들어감
    # 똑같은 1들 뺑뺑 반복 도는 거 방지 위해 미방문쳌!!!! <-> [1]은 미방문쳌 안하셨네
    while (queue0):
        v = queue0.popleft()  # - 아래 for의 v 인접 4곳은 v 의거리(v[2]에 저장)에서 1 더해짐
        # <-> count+=1 # 같은 층인 친구들 빼는 순서에 따라 자식들에 다른 count 더해주면면 안됨

        for i in range(4):
            nx = v[0] + dx[i]
            ny = v[1] + dy[i]

            if nx == n - 1 and ny == m - 1:  # - 주의사항 * 해둔 거(인덱스 -1) 라스트 체크해라
                print(v[2] + 1)  # 최소 거리로 도착하면 끝이라서, 그 후의 거리에서 동일한 위치 갈 일 없어서 min 필요 없음
                return 0
            elif nx >= 0 and ny >= 0 and nx < n and ny < m and not visited[nx][ny] and map0[nx][
                ny] == '1':  # - 이 줄 조건문 조율해서 시복+k 효율화 보다, 이것처럼 인덱스 체크 후! 인덱스 사용
                track[nx][ny] = v[2] + 1 # - map0에 저장하는 게 더 좋음. map어차피 0,1 문자열이라 구분됨.  # bfs는 어미노드 거리값+1
                queue0.append([nx, ny, track[nx][ny]])
                visited[nx][ny] = True  # - append할 때 방문처리. : 벽은 visit 체크 안 해도 값에 의해 조건문 불퉁과고 아무 실행없음
                # visitd 체크_good :  돌아서온 먼 경로 무시해줄 수 있음 : 높은 거리값 겹치는 걱정 및 min법 필요 없음

n, m = map(int, input().split())
map0 = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
track = [[n * m + 1000] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

bfs([0, 0, 1])  # 1은 첫 count
# 1시간 20분.
# > 코드 오타가 생각보다 있으니,
# -> 디버깅 시 : 알고리즘 보다도, * 모든 변수 체크도 해보자.

# - 다른 사람 코드 [1]jhw7348 : 나보다 1.5배 속도효율
# > 책에 나온 bfs 시 dequeue의 popleft 사용이 더 빠른 거 맞나 / 빠른 코드들에서 쓰는 거 못봤는뎅 /
# : 전엔 pop 이번엔 del queue[0]

# <-> 정석이어서 꽤 괜찮은 정도와 그냥 더 빠른 거의 차이인가
# > '123'도 map_int->list로 가능 -> [1,2,3] : arr.append(  list(map  (int,input())))
#    1 2 3 에서 map 전에 split한 건 공백 없애려고 했던 거고 분리화는 map으로도 가능 _ 백 없는 것123
# > 부등식 조건 양쪽 동시에 쓰시네. 사람들 왜 안 썻었지 으음 일단 보류   : if 0<=x<n ..

# n,m = map(int,input().split())
# arr = []
# queue=[[0,0]]
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

# for i in range(n):
#     arr.append(list(map(int,input())))

# while queue:
#     a,b = queue[0][0],queue[0][1]
#     del queue[0]
#     for i in range(4):
#         x = a+dx[i]
#         y = b+dy[i]
#         if 0<=x<n and 0<=y<m and arr[x][y] == 1:
#             queue.append([x,y])
#             arr[x][y] = arr[a][b] + 1

# print(arr[n-1][m-1])
