# 1)
# 높이 정보 -> 물에 잠기지 않는 안전한 영역의 최대 개수
# - 안전 영역 : 사방이 물에 안잠김 & 그 크기가 최대
# 2)
# -> 높이 돌

# n=int(input())
# - 이 문제는 문제설명보고 이해하려 하지 말기?

# 4) n 2,...100 / 높이 1,..13
# 0 , n*n 

# - 20m?
# 예시 보니까 해당 층이 전부 여야함? 근데 왜 5
# 789보니까 딱 직직육면체 ? 아 9는 인접한 놈없어서. 혼자 살아남는건 아님. # --> 문제설명과 달리 케이스는 인접한 놈 없어도 됐었음
# 근데 그럼 저게 5네
# 문제이게 맞나. 중의적으로 해석되고 숫자보고 이론 적인 규칙을 뽑아내야하는 수준인데  코딩 알고리즘용이 아니라 규칙찾기 도형놀이?
# 그래도 차후 빠른 문제 이해에 도움이 되려나

# - 문제 이해 안 가서 솔루션 코드 보고 문제 이해함
# - 문제 설명 음. 내가 빠르게 못 포착한 부분도 있는데 다른 게 애매해서 그것도 명확하게 못 봤던 부분도.  애매하게 말해도 예시케이스 보고 문제 파악하기 능력을 키워야하는 거려나
#   > (솔루션이 틀렸다기엔 너무 핵심적인 알고리즘 부분이라 맞다고 체크되면 그문제였던 게 맞을듯). 

#   + 헷갈리게 됐던 부분 : 물에 잠기지 않는 안전한 영역이라 함은 물에 잠기지 않는 지점들이 위, 아래, 오른쪽 혹은 왼쪽으로 인접해 있으며 그 크기가 최대인 영역을 말한다. 
#     + 헷갈린 이유(뭔말이지 부분, 중복적해석 가능 부분(1개가 아니면 경우의 수 엄청나게 늘어남. 대충 알아들으라 하기엔 코딩은 엄밀화되지 않은 부분도 생각하며  그러한 엣지케이스?도 해결하는 코드짜는거 아닌가_해외 특정 코딩사이트와의 차이인가) ) 등등 : 인접한 거 없어도 안전한 영역임(그렇게 따지면 문제 설명의 두 번 째 예시의 독립적으로 하얀 칸7은 카운트 안 돼서 안전영역 3개여야하는 거 아닌가?). 혹은때의 반점도 모두 혹은의 연결임 영어처럼.  위, 아래는 층부분은 아님

#   + 헷갈 부분 : 잠기다_높이가 물보다 높은 곳은 물 이하 부분이 잠긴 게 아니라 아예 안 잠긴 것임/지역은 맵, 지점은 층 통째로 맵에서의 한 지점


#   + -> 물에 잠기지 않는 지점들의 '존재'가 인접해 있는 걸 1개(=그 크기가 최대인 영역)의 안전한 영역으로 따지기


# - 다른 사람 풀이 [https://velog.io/@seungjae/%EB%B0%B1%EC%A4%80-2468%EB%B2%88-%EC%95%88%EC%A0%84-%EC%98%81%EC%97%AD-Python-BFS-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4-Silver1]
#   + 물 높이마다의 안전영역 개수에서 최대를 찾기 위해 각 층마다 : 안잠긴 지점이 있는지를 sink_map에 T/F로 저장 -> 안잠긴 지점을 bfs노드에 넣어서 주변 방문화.(_잠긴지점화)
#   + True, True의 bfs로 풀 수 있는 이유  : True라는 건 물의 높이+1인 칸이 무조건 있다는 것이므로 무조건 연결돼있음.
import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_rain = max(map(max, graph))
# 물의 양 조절하기
# 물에 잠기는 영역 확인하기
# 안전한영역의 개수 체크하기
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def bfs(i,j): # - 안 잠긴 영역만 BFS 노드 시작
    global count # - 다른 함수에서 선언한 변수도 다른 함수에서 global 선언하면 변경 가능
    q = deque()
    q.append((i,j))
    sink[i][j] = True # - 이미 방문한 부모 잠김화
    count += 1 # 안전한 영역 개수 1 추가
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i] # 상하좌우 확인
            ny = y + dy[i]
            if nx<0 or ny < 0 or nx >= N or ny >= N: # 영역 밖으로 나가면 x
                continue
            if sink[nx][ny]==False: # 상하좌우중 잠겨있지 않은 부분이 있다면
                sink[nx][ny] = True # 잠겼다고 가정시킴
                q.append((nx,ny))
count_list = []
for rain in range(max_rain): # 물의 양 조절
    count = 0 # 안전한 영역의 개수 카운트
    sink = [[False for _ in range(N)] for i in range(N)] # 물에 잠긴 부분 초기화
    for i in range(N):
        for j in range(N):
            if graph[i][j]<=rain:
                sink[i][j]=True # 물에 잠기는 영역 확인하기
    for i in range(N):
        for j in range(N):
            if sink[i][j]==False: # 잠기지 않은 영역일 경우에만
                bfs(i,j) # bfs실행하여 영역모두 잠겼다고 가정하면서 안전한 영역 1 추가시키기
    count_list.append(count) # count_list에 추가 

print(max(count_list)) # count_list중에서 최대값을 출력
