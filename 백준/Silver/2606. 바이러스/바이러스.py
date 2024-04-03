n=int(input())
n_connect=int(input())

graph=[ [] for _ in range(n+1)]
for _ in range(n_connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
visited=[False ] * (n+1)
visited[1]=True 
que=[1]
count=0

while (que):
    v=que.pop(0)
    for target in graph[v]:
        if not visited[target] :
            visited[target]=True
            count+=1
            que.append(target)
print(count)