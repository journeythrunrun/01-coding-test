# # 1) 도착까지 최소 횟수 상대 팀에 도착 못하면 -1 
# # 1자리 : 이동가능

# # 2) bfs
# # n=100 -> n^4 
# from collections import deque
# def bfs(v, visited,maps): # - 리스트(mutable_set, dict까지.) : 함수 밖에서 선언한 거면(함수 내에서도 전역으로 쓸 수 있음) 모를까, 함수 내에서 시작된 거면 리스트여도 다른 함수에서 사용하려할 때 변수 건네야함

#     #   + 전역 '리스트'면[함수 밖에서 정의된 리스트] 함수 내에서 'global 글자 없이도' '사용하고, 바꿀 수 있'을 뿐, 로컬에서[함수] 선언한 것도 전역인 건 아님 # 함수 내에서 요소값 변경 말고, 재정의(리스트자체 = )를 하면 그 이름의 로컬 리스트가 생기는 것임

#     dr=[0,0,1,-1]
#     dc=[1,-1,0,0]   

#     visited[v[0]][v[1]]=True
#     aque=deque([v])
    
#     while(aque):
#         target=aque.popleft() 
#         for i in range(4):
#             nr=target[0]+dr[i]
#             nc=target[1]+dc[i]
#             if 0<=nr<len(maps) and 0<=nc<len(maps[0]) :
#                 if visited[nr][nc]==False and maps[nr][nc] > 0:# - 최소값 어떻게 가져올래 : m_x 최소값을 map에 저장 -> m_o bfs로 하면 그냥 먼저 턴에서 닿았을 때 멈추면 최소임 -> 계층 거리 이상해지지 않게, 부모인 target변수 이용해서 aque의 노드 저장할 때 맨 뒷 요소로 +1거리씩 저장
#                     if nr==len(maps)-1 and nc==len(maps[0])-1 : # ! nr(O) target[0](X)
#                         return target[2]+1
#                     else : 
#                         aque.append([nr,nc,target[2]+1])
#                         visited[nr][nc]=True
#                         ##maps[nr][nc]=min(maps[])
#     return -1

# def solution(maps):
#     n,m= len(maps), len(maps[0])
#     visited=[ [False]*m  for _ in range(n)]

#     return bfs([0,0,1], visited,maps)
    
#     # 4) 도착 못할 경우, n m 중 한 개가 1

# - 32m(멍 때림 5분), +2점
# - 다른 사람 풀이 [김성기 , 서우석 , keepithunnyt , KSY 외 6 명] | 69.9, 30.1 (내 코드랑 점수같음)
#   + 나 굳이 bfs를 다른 함수로 뺄 필요 없었네. 프로그래머스는 자체 솔루션 계산 하는 곳이 이미 함수 내이니까 지역변수 안 귀찮아 지려면 bfs는 내부에 하는 게 낫다.
#   + 이 분 visited가 없네 ~~ 내 m_x였던 map에 저장 & 조건에서 visited대신 맵값이 0보다 큰 거 . 이분은 0말고 d + 1((갔던 곳은 첫 위치 빼곤 1아닐 거라, 이동 가능한 칸인지 검사하던 1인지 체크가 미방문 체크인 것도 됨. 근데 어차피 맵값이 최종 최소보다 크면 줄여나가네. bfs라 자동으로 미니멈 거리씩 가서 굳이 저렇게 안해도 ㄱㅊ함. -> 조건문 후반부 빼도 정답의 점수들 같음.(값 d+1넣는 건, 처음 방문하는 케이스 포함해서 모든 경우에 해주는 값이라 d+1해야하궁) ) )
from collections import deque
def solution(maps):
    x_move = [1, 0, -1, 0]
    y_move = [0, 1, 0, -1]

    x_h, y_h = (len(maps[0]), len(maps))
    queue = deque([(0, 0, 1)])

    while queue:
        x, y, d = queue.popleft()

        for i in range(4):
            nx = x + x_move[i]
            ny = y + y_move[i]

            if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
                if maps[ny][nx] == 1 : #or maps[ny][nx] > d + 1:
                    maps[ny][nx] = d + 1
                    if nx == x_h - 1 and ny == y_h - 1:
                        return d + 1

                    queue.append((nx, ny, d + 1))

    return -1

