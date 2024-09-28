# 1) 컴0~n-1  => 네트워크의 개수
# 2) 이어서 붙이기 -> set에? 없으면 추가

# n 200이하 -> n^3



def solution(n, computers):
    network_index=[False]*n
    sets_list=[set([0])] # set에 요소 넣을 때 [ ]이든 씌워야.그냥 ( (0)=단순 숫자 )안됨= int not iterable
    # - 초기값, 위치 0,1 주의

    # 4) 연결된 거 하나도 없으면 n개, 반복 시 초기값 첫번 째, n=1
    for i in range(len(computers) ) : # > 얘네 for 2개에서 1인놈들 따로 저장해서 시복 줄이는 방법도 있긴 함
        for j in range( i+1, len(computers) ) :#동일한 거 검사 안 하기 위해, 순서 정렬한 것만 검사
            # - for문 아래에 아무것도 없으면 에러_~expected an indented block 
            
            if computers[i][j]==1 : #1만 
                find=[-1,-1] #검사하려는 컴퓨터가, sets_list에서 몇번째 인덱스에 해당하는 네트워크에 속했는지 저장
                for k in range( len(sets_list) ):
                    if (i in sets_list[k]) : 
                        find[0]=k
                    if (j in sets_list[k]) : 
                        find[1]=k
                        
                if find[0]!=-1 and find[1]!=-1 and find[0]!=find[1] : # 5) 두 컴퓨터가 각각 '다른' 네트워크에 속해 있을 때. 두 값이 초기값아닌 것 뿐만 아니라 다른 것 까지 체크
                    
                    # - set : 합체_union보다 update([1,2])가 나음
                    #   + -> ! 그 결과를 =으로 해당 변수에 다시 저장해야함.
                    sets_list[ find[0] ]=sets_list[ find[0]].union( sets_list[find[1]] ) 
                    sets_list.pop( find[1] )
                    
                # 5) i 랑 j가 서로 다른 네트워크에 있으면 :
                        # X_m1) (검사는 : 이미 둘다 네트워크 있을 때의 케이스임)
                        # -> 몇 번째 네트워크인지 저장해둔 후 , 나머지도 같은번호화 -> 그 변수이용해서 결과. 다른 숫자의 네트워크_ max() 
                        # m2) set합체는 sets_list 다 검사해야. 근데 빨리 탈출하고 있던 것 뿐이지 어차피 해당 for문으로 검사는 하고 있었음. set_list[k]에서 몇 번째((엄밀힌 인덱스 사용함)) 네트워크로 저장돼있는지 저장하고, 그 위치의 sets에 붙이고 나머지 한 네트워크는 제거
                        
                # - ! 0이랑 False랑 똑같이 취급돼서 문제생김. #코딩할 때 첫 번째를 0<->1 바꾸던 것도 영향받음.
                elif find[0]==-1 and find[1]==-1 : # ! 인덱스  둘 다 [0] 아님
                    sets_list.append( set([i,j]) )
                    
                else :  #두 개 중 이미 네트워크에 연결 된 게 '한 쪽'만 있는 경우->나머지 까지 연결되게 넣기. 이미 있는 놈 포함하여 둘 다 거기에 넣어도 됨(set이라 중복 알아서 처리)

                    # if find[0]!=-1:
                    # find가 -1인 곳말고 값있는 놈 위치에.
                    # 네트워크에 이미 자리가 있는 놈을 찾아서 그 위치에 없던 놈도 넣어줘야함.
                    target=max(find)
                    sets_list[target].add(i)
                    # if find[1]!=-1 :
                    sets_list[target].add(j)
                    
                    
                    
                    # 네트워크 합체 케이스 빼진 구코드 및 m1 조금 하던 거 
                    # if (i in sets_list[k]) or (j in sets_list[k]) :
                        # if (network_index[i] !=False) and (network_index[j] !=False) :
                        #     for 
#                                 if v == network_index[j] :
#                                     network_index[]= v
#                         network_index[i]=k
                        
                        
                        # sets_list[k].add(i)
                        # sets_list[k].add(j)
                        # next_turn=True
                        # print(sets_list)
                        # break
                # if next_turn==True: # 여기 아래에 뭘 했었나. 당연히 continue인데 굳이
                #     continue#break # - continue <-> break 쓸 때 주의
            
    
    # n-주의
    connected_computers = 0
    for aset in sets_list : 
        connected_computers+=len(aset)
    
    answer = n  if (len(sets_list)==1 and len(sets_list[0])==1) else  (n-connected_computers)+len(sets_list) 
    return answer

# - 1h 40m(+1점_방법 생각 후 시복 아슬아슬하게 괜찮겠다 싶어서 선정하여 품. 저 점수로 연결되넹) 논리케이스 1개 추가 + 자잘한 디버깅 오류

# - set : |, &, -, ^, update

# > 값 복사 :  b=a.copy()
# > 기본함수 및 시간복잡도
# >> O(1)
# : in 
# : .add() / .update({3}) / |={3}
# : .discard(3)  (없어도 에러 X) / .remove(3)  ( 없으면 에러_예외처리 필요 )
# : .pop()
# : .clear()
# > 집합 연산
# : 축약형 가능  ^=
# : 1) set1.union(a,b) / a | b
# : 2) set1.intersection(a,b) / a & b
# : 3) set1.difference(a,b) / a - b
# : 4) set1.symmetric_difference(a,b) /  a^b (xor. 겹치지 않는 원소)
# >> 집합 비교
# : a >= {1,2} != 



# - 다른 사람 풀이 [최지호 , 조양규 , 하윤아빠 , Junhoe Do 외 102 명]
#   + bfs/dfs 문제인 거 알고 들어왔긴 한데, 풀이법 알고 풀면 의미 없을 까봐 초기화하구 품 -> 다른 방법으로도 풀 수 있는 문제들도 많을 텐데 그럼 bfs/dfs가 연습이 안 되긴 하겠네.  
#     + 아니면, bfs로 푸는 게 더 빠르고 확실한 문제들이 있는데, 좀 더 우선순위에 두고 그 풀이도 가볍게 생각해보는 경험이 부족한가
#     + bfs/dfs : 특정 컴퓨터 위치에서 시작해서 해당 연결 이어서 탐색하기. 마침 연결맵도 있네 | 한 컴퓨터에서 끝까지 먹어서 탐색하기 반복. 한 네트워크 마다 dfs/bfs   

# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer

# - dfs
# def dfs(v) :
#     #1targets=[v] -> deque([v])
#     visited[v]=True
#     print(v)
#     #1bfs가 더 익숙하긴 하지
#     #1while(targets):
#     #1    target=targets.pop() -> popleft()
#     #1    for connected in graph[target]:
#     for connected in graph[v]:
#         if not visited[connected]:
#             dfs(connected)#2
#             #1visited[connected]=True
#             #1targets.append(connected)
    