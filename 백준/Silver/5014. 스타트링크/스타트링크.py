# 1) 총 F층. 강호S층  -> G층

#  그 이동 층이 있는 층이면 : 위로 U층 / 아래로 D층_ 

# -> 버튼 최소 수 . 없으면 "use the stairs"

# 2) 백만. O(n), O(nlogn)


from collections import deque
n, initial, goal, u, d = map(int, input().split())
# - 백만 nlogn
answer="use the stairs"
visited=[0]*(n+1)

visited[initial]=1
q=deque([ [initial,0]]) # - => [[로 생각하자.
while(q):
    v, distance= q.popleft()
    # print(v,distance)
    if v== goal :
        answer=distance 
        break
    for child in [v+u, v-d]:
        if 1<=child<=n and visited[child]==0 :
            q.append([ child, distance+1] )
            visited[child]=1
            
print(answer, end='')            


# 4) s, g, =1, =f
# 대소관계
# u,d=0

# 5) #$
# - 6) 시간 남으면 2~3개*3단계

# - A) 인덱스 -1 =>  + 다 땡겨서 하면 실수하니까 초기화+1개

# - 23m (제출하고 틀림) / 20m_(인덱스바로 쓰기 위해 초기화 +1개)
#   + d 변수이름 겹침. d 특히 주의하고. 변수 작성할 때 겹치는 거 없는지 생각. 특히 문제에서 주어진 변수 이름 같은 경우는 내가 지정하면서 의식하지 못하니까 내가 평소에 쓰는 거랑 안겹치는지 더 주의.
#   + 중요한 변수 겹쳤는데도, 테스트케이스에서 중간 중요출력 다 동일할 수 있음 : 이번 상황. 어차피 위로 가는 게 minimum이라 진짜 d가 q에 안쓰인 상황. | 다른 테스트케이스의 중간출력을 통해 알 수 있음.
#     + 무조건 맞다고 생각한 경우도 틀릴 수 있다? >  물론 코테 어차피 핵심 알고리즘 풀어도 시간 안남고 실제 코테면 남은 시간 확인할 거긴함.