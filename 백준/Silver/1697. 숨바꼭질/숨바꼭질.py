# 1) 숨바꼭질

# 2) 십만 O(nlogn)
# i. 이동 함수 : x-1 or x+1
# ii. 순간이동 함수: 2*x
# -> 동생을 찾을 수 있는 가장 빠른 시간
# 3) 함수를 bfs로. 병렬은 아니고 distance를 동일하게 주면됨.



from collections import deque
# - from collections
person, item = map(int, input().split() ) # 5, 17
# - int, input.split()
visited=[0]*100001  #m1 
# visited=set()#m2 범위 모르면 애매하므로

q=deque([ [ person ,0] ]) # v,d 
# - 리스트 속 리스트 사용시 =로 가져오면 주소 및 동기화 주의. 가져다만 쓰면 안전
visited[person]=1 #m1
#m2 visited.add(person)# x
while(q):
    v,d=q.popleft()
    #print(v,d)
    if v==item : 
        print(d,end='')
        break
        # - 왜 계속 출력되나 했더니  break안했넿 정답 출력하고 프로그램 종료 시켜야지
    # - 다음 타겟들 for에서 한 번에 돌리도록 변수 targets인 [children] 변수를 만들어줌.(그래프 없으니까 대신) children이 더 직관적.
    # - childrens를 구하는 게 복잡하면 새함수 정의
    
    children=[ v-1,v+1,v*2 ]
    
    for child in children:
        # child에 대해 따져야하는 조건이 같아서 for을 통해(동일한놈들 미리 리스트에 넣어서 만들어 준 후) 동일한놈 child 변수로 뭉침 
        
        # - 리스트_인덱스 범위 &&&& <-미방문 
        #m2 if one not in visited :
        if 0<=child<=100000 and not visited[child] :# 범위 #m1 
            q.append([child,d+1] )
            #visited.add(child)#m2
            visited[child]=1 #m1  
            
        # 문제에서 주어진 N범위 : 현재 저 점에 있다는 거고 저 범위 밖을 중간에 가는ㄱ ㅔ안된다는 말은 없는 거같은뎅. 둘다해보지머

#4) N=0,같은놈, 십만.
# 5)#$ 6) 출력후 앞 2~3줄이라도

# - 약 20m : 주석, 오류수정도 포함
#   > (, 문제에서 구체화 안한부분 가능한 경우인 두 방법 다 풀기?&주석, 쉬운 문제라 굳이 엄청 엄밀한 조건으론 덜 줬을 수도 있나)


