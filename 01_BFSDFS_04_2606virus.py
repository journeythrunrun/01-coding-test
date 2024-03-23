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

# - bfs-그래프 생성
# > 0.1) 양방향 그래프 형성폼 0.2)중복(엣지 케이스) 처리한
graph=[ [] for _ in range(n+1)]
for _ in range(n_connect):
    a, b = map(int, input().split())
    if b not in graph[a]: # - 갈 곳에 갈 놈이 이미 있진 않은지 체크
        graph[a].append(b) # - append
    if a not in graph[b]: # 인덱스 에러 안남. -> 모든 행 빈리스트 가지게 만들어둬서 문제없음
        graph[b].append(a)

visited=[False] * (n+1)
que=[1]
visited[1]=True # - 1번컴은 결과에 카운트 안 하더라도(출력) 먹었으면 (방문)visited 처리는 해야 안 틀리지! 1-2) 초기
count=0

while (que):
    v=que.pop(0) # - <-> deque : 데이터 복잡하면 pop del 보다 deque가 빨라지는 거려나. 블로그에 이유도 적어놨으려나
    for target in graph[v]:
        if not visited[target] :
            visited[target]=True
            count+=1 # pop할 때 출력이 나은데 자꾸 append할 때부터 해버리넹
            que.append(target)
print(count)

# - 28 분 : 성공
# > 15분 : 실패 ( 엣지 케이스, 조건 정확히 미충족 )

# - bfs든 dfs든 visit을 카운트


# - 개념 : bfs(더 빠름)/dfs 개념 암기 (( 디버깅으로 찾기보다 애초에 한방해결이 나음))
# > bfs : 조건 2개 & 함수 1+6개
# [조건] 1.1) Graph_양방향성 (행 별 sorted는 문제 조건에 따라 선택) 1.2) 중복 체크**
# [함수] 1) 먹어-v0 & 방문
# [함수] [큐]3.1) While(큐) 3.2) 뱉 v=.pop(0)3.3) 프린트     [그래프]3.4) for 그래프[v_자식들] 3.5) 미방문 _ 3.6) 먹어(.append) & 방문

