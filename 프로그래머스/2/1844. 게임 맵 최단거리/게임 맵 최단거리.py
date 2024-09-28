# 1) 도착까지 최소 횟수 상대 팀에 도착 못하면 -1 
# 1자리 : 이동가능

# 2) bfs
# n=100 -> n^4 
from collections import deque
def bfs(v, visited,maps): # maps도 넣어야함
    dr=[0,0,1,-1]
    dc=[1,-1,0,0]   
    # global

    visited[v[0]][v[1]]=True
    aque=deque([v])
    
    while(aque):
        # print(aque)

        target=aque.popleft() # +1같이 저장
        for i in range(4):
            nr=target[0]+dr[i]
            nc=target[1]+dc[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) :
                if visited[nr][nc]==False and maps[nr][nc] > 0:# 최소값을 map에 저장? -> bfs로 하면 그냥 먼저 턴에서 닿았을 때 멈추면 최소임
                    if nr==len(maps)-1 and nc==len(maps[0])-1 : # nr(0) target[0](X)
                        return target[2]+1
                        
                    else : 
                        aque.append([nr,nc,target[2]+1])
                        visited[nr][nc]=True
                        ##maps[nr][nc]=min(maps[])
    return -1

def solution(maps):
    n,m= len(maps), len(maps[0])
    visited=[ [False]*m  for _ in range(n)]

    return bfs([0,0,1], visited,maps)
    
    # 4) 도착 못할 경우, n m 중 한 개가 1
#     answer = -1

#     return answer
# 멍 때림 5분