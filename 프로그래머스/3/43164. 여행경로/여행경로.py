# 1) 
# - ICN에서 출발
# - 항공권 모두 이용. 
# - 경로 두개 이상이면 알파벳 순서가 앞서는 경로. 방문대상 시 알파벳 앞부터 넣기. 
# -> 경로

#$ 2) n=10,000 : 2000 에 더 가까우니까 ~O(n^2) 될지궁그
# 여러 경우의 수에 대하여 미방문 애들만 진행
# - 모두 이용 : while(left) : 
# - target="ICN" & 업뎃
# - 알파벳순 : m1_ nlogn충분하니까 미리 정렬_코드단순 m2_찾은 애들 알파벳 빠른 순서로 정렬 후 진행. # x[i][1] == x[i+1인 경우중에

#$ mC_걍 남은 거에서만하지 않고 visited으로 체크하며 통째로 n*n = n+ ..+n = n*n # +연결임 # 찾으면 break 라서 다 가지도 않음
# mA_ find 하고 제거하며 찾기 ~~ n+n-1+...1 = n(n+1)/2 
# mOtehr_visited넘겨주기


# 3)
# visited=[]
import copy
def dfs(target, dict1, answer, len_t ): # - N : 중복 출발지인 애 있으면 티켓들의 길이와 dict1길이 다름 #$ 주석 수정
    # (1) 종료조건
    if len(answer)== len_t +1: 
        return answer # 함수 사라지면 변수 사라지기 때문에 bfs 다시 올라갈 때(dfs 함수 구현 자동임.) 변수 계속 건네줘야함. 전역변수는 함수에선 굳이.
    
    # (2) 부모자식
    
    # dict1[target]에 있는 애들에 대해서만 dfs로 함수 쌓음
    ### 난 딕셔너리라 아래를 했어야
    # - 딕셔너리 조회 시 주의!! 붙이기
    # if not dict1.get(target):# 없으면
    #     return None
        
    for index, airport in enumerate( dict1.get(target,[]) ): # 'ICN', 'AAA' # dict1[target]가 list인 거고 그 안 요소 각각은 한 개
        # - !!!! dict1[target] 여러 개중에 airport 1개만 쓴 거지, airport 이전것들까지 다 쓴 거 아님. 해당 티켓은 남아있지. 티켓을 여러개씩쓰진 않지.
        # if index>=1:
        #     print('index 1 >=', dict1)
            # 
        # (3) 사용 
        # - 방문 미방문 검사 없는 이유는 저기 애들 다 쓸거로 넣어놔서
        # - 그 다음 경로 없을 수도 있어서 return은 for문 밖에서 해야함
        
        # - 먹고
        # - 복사는 시복 너무 커짐 new_dict1=dict1[:] #x 사용했으니 빼자 #$ O(  n_ dfs *n) 
        # pop하면 다음 for관련 인덱스에서 인덱스 바뀜 dict1[airport].pop(index) # 요소인 리스트에서의 특정 요소만 빼기.
        # <-> append한거, pop한거 =로 재정의. 어차피 요소수 적어서.
        # save=dict1[airport][:]
        # - ! target의 value를 빼야하는데(이전 방법에서도 그렇게 했는데) 이 방법 코드에선 실수로 airport로 해버림. airport가 너무 범용 단어다. depart arrive
        
        # dict1은 주소 참조로 가져와서, for 내에서는 계속 같은 애
        # [["ICN", "AAA"], ["ICN", "BBB"], ["ICN", "CCC"], ["CCC", "ICN"], ["BBB", "ICN"]]
        # 기댓값 〉 ["ICN", "BBB", "ICN", "CCC", "ICN", "AAA"]
        new_dict1 = copy.deepcopy(dict1) # 딕셔너리가 주소로되진 #$ dfs라 어차피 걍 딕셔너리 업뎃한걸로 
        new_dict1[target].remove(airport)# - remove는 처음 찾은 값 1개만 지워서, # dict1에서 k_target, v에서 airport인거만 뺀 거 # new_dict1[target]=dict1[target][index+1:] # [index]까지 사용완료# 현재 target의 airport 한 개 사용함 # 리스트 건네는 것의 의미 : 사용 가능, 변경은
        ## 처음에 for 관련 코드 작성할 때 [1:]한거는, 이 new_dict 방식 말고 다른 식으로 갱신했을 때임 
        # - 딕셔너리의 한 벨류값 복사하는 거 아니고 deepcopy임. 리(스트)딕(셔너리)셋(트)는 mutable이라 다른 함수에서 
        # - immutable인 튜플로 하면 전체복사 할 필요 없겠다. dfs에선 오히려 건넬 대상이 immutable_tuple인 게 훨씬 나은 경우가 왕왕 있음
        # - 튜플 do
        # print(dict1)
        #$#$
        new_answer = answer[:] # 걍복사 함수간의 전역성떔시
        new_answer.append( airport )# - 얜 new target # - new_answer= answer+airport #append는 반환안하며써 answer.append(airport)
        
        can=dfs(airport, new_dict1 , new_answer, len_t ) # dict1[airport][1:] TypeError: list indices must be integers or slices, not str 
        # - ! len_t는 증가해야하는 거 아님. 변수 이름을 길더라도 len_tickets로 하든 N 으로 하든 의미 명확하게 해야 실수 안 한다.
        # - ! dfs로 모두 돌아야하는데 한번 break하면 계속 break하네#$#$
        # - 뱉
        # for문이라 이 dfs 아직 안끝나서 원상복귀.
        # dict1[airport]=save[:] # dict1[airport].append(airport)
        # - answer는 for문안에서 안써서 원상복귀 안해도됨 answer.pop()
        # print(can)
        if can :
            # - 자식중 빠른 알파벳이 끝까지 도착 성공했으면 더 볼 필요 없어서 for문 내에서 return
            return can# 굳이 if 한 번 더 거쳐야할까
    # print('함수종료', target, dict1, answer, len_t,'dfs 함수 끝까지 갔는데 이번 경로에서 정답 없음.') 

def solution(tickets):
    
    tickets.sort() # - 시복내인데 굳이_최적화하려면 딕셔너리에 겹치는 게 있을 때만 그 리스트에서 sort해주는 게 나음
    visited=[False]*len(tickets)
    target="ICN"

    #시복 줄이기 : 티켓 단순 돌며 딕셔너리에 저장. 딕셔너리 넣은 순
    dict1=dict()
    for i in range( len(tickets ) ): # len..
        if dict1.get(tickets[i][0]) : # 있으면. 문자엻이라 ==0 안되고 몸체그대로 ? # 문자열안됨 #~오륜 없
            renew=dict1[ tickets[i][0] ] [:]
            # 'list' object cannot be interpreted as an integer
            renew.append( tickets[i][1]   )
            dict1[ tickets[i][0] ]=renew # 원래 있던 값에 추가            
        else :  # 수정했을 때 위도 
            dict1.update([ [  tickets[i][0],  [tickets[i][1]]     ]]) # 
            
    answer = []
    answer.append(target)
    
    # m0 시간초과->해설방법
    answer=dfs(target, dict1, answer, len(tickets) )# -dict1 : dfs 노드 가며 사용한 거에 따라 바뀜
    
    # mB 시복 간단 & 오답 케이스 존재
#     while( len(answer)<len(tickets)+1 ) :
#         # 사전에서 앞에있는 거 사용
#         old_target=target
            
#         # 새로운 타겟 찾기 . 
#         target=dict1[target][0] 
#         visited[i]=True
#         answer.append(target)   

#         # 사용된 old_target 리뉴얼
#         if len (  dict1[old_target]  ) >=2 :
#             dict1[ old_target ]=dict1[ old_target] [1:] # 이번꺼 사용후 리뉴얼
#             # 'list' object cannot be interpreted as an integer
            
        # for i in range ( len(  dict1[target] )) :
        #     if
        #     if not  # 딕셔너리 제거 라기보단 리스트 제거 재할당 
    
    # mA : mB와 같은 오답 케이스 & 시복 좀 더 복잡
    # 가능한 여러 가지 경로 중 최소 거리라기보단 가능한 게 한 경로로 정해져있음.
    # while( len(answer)<len(tickets)+1 ) :
    #     for i in range( len(tickets)  ):
    #         if not visited[i] and target == tickets[i][0]: # 타겟 찾았당
    #             target=tickets[i][1]
    #             visited[i]=True
    #             answer.append(target)
    #             break
                # last_index=i
                
                
                # continue # - 이거 #$였으면 라고 
    
    #$ i,f
    # answer.append(target) # i,f : 길이 3이면 출력 길이는 4임   
    # answer.append(target)
    return answer
# 4) 공항 수 3, .
# [["ICN", "JFK"], ["ICN", "JFK"],["JFK","ICN"]] -> ["ICN", "JFK","ICN", "JFK"]

# -  1h 12m 든 34m 순간이었든 34m : 두 케이스 시간초과 
#   > 시간초과로 정답봄

#   + 알파벳순이 전부 정답이 아님. 끝까지 도달 못 하는 것도 있음
#   + 만든 딕셔너리 사진을 기준으로, 그걸 자식 노드로 하는 bfs. bfs~ 연결노드맵생각

# - 다른 사람 코드 [https://school.programmers.co.kr/learn/courses/30/lessons/43164/solution_groups?language=python3]
'''
from collections import defaultdict 

def dfs(graph, N, key, footprint): # - dfs ( [그래프],  _굳이_, v, [최종 정답일] 리스트 변수 # - ~~ bfs의 while
    print(footprint)

    if len(footprint) == N + 1: ## - 탈출조건 
        return footprint

    for idx, country in enumerate(graph[key]): # - v의자식. 
        graph[key].pop(idx) # - (1) 딕셔너리에서 사용한 거 빼기
        tmp = footprint[:] # - (2) 결과에 금방 사용한 게 추가될 리스트 : dfs 의 노드 위치 마다 달라야하기 때문에 리스트 복사한 후 리뉴얼해서 건네
        tmp.append(country)
        
        ret = dfs(graph, N, country, tmp) # 
        
        graph[key].insert(idx, country) #$ - 이거 지우면? # 이 dfs 위치 노드에서는 저거 안 사용했기 떄문에 다시 insert
        
        if ret: # - 끝까지 못 갔으면 dfs함수는 None을 반환했을 것임
            return ret # -  dfs에서 다시 위 노드로 거슬러 올라올 때, 종료케이스로 끝까지 간 애만 None아닌 것 반환하며 올라갈 수 있도록함


def solution(tickets):
    answer = []

    graph = defaultdict(list)
    
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer
'''
