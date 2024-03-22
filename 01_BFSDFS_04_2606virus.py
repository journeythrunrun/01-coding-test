# - 문제집_DFS+BFS 필수 문제_바이러스_https://www.acmicpc.net/problem/2606

# 1) 1번 컴퓨터 => 1번 제외하고 바이러스 걸리는 총 컴터 수
# * 0말고 1부터임

# 2)
# 행에서의 정렬은 조건에 따라 필요 없기도 함

n=int(input())
n_connect=int(input())

if  n_connect ==0: # - 엣지 케이스 처리
    print(0)
    exit()

graph=[ [] for _ in range(n+1)]
# - 엣지 케이스 처리한 양방향 형성폼으로 숙지 : 중복 처리
for _ in range(n_connect):
    a, b = map(int, input().split())
    if b not in graph[a]: # - 갈 곳에 갈 놈이 이미 있진 않은지 체크
        graph[a].append(b) # - append
    if a not in graph[b]:
        graph[b].append(a)

visited=[False ] * (n+1)
visited[1]=True # - 1번컴 결과 카운트 안 하더라도 visited 처리는 해야 안틀리지! 2.1) 초기값
que=[1]
count=0


while (que):
    v=que.pop(0) # - 데이터 복잡하면 pop del 보다 deque가 빨라지는 거려나. 블로그에 이유도 적어놨으려나
    for target in graph[v]:
        if not visited[target] :
            visited[target]=True
            count+=1
            que.append(target)
print(count)

# - 28 분 : 성공
# > 15분 : 실패 ( 엣지 케이스, 조건 정확히 미충족 )

# - bfs든 dfs든 visit을 카운트


# - 개념 : bfs(더 빠름)/dfs 개념 암기 (( 디버깅으로 찾기보다 애초에 한방해결이 나음))
# > bfs
# 1.1) Graph_양방향성 (행 별 sorted는 문제 조건에 따라 선택) 1.2) 중복 체크
# 2) Visited=, 첫 v
# 3.1) While(큐) 3.2) v=.pop(0) & 나오며 프린트  3.3) for v_자식들 3.4) 미방문 _ 3.5) .append & 방문

