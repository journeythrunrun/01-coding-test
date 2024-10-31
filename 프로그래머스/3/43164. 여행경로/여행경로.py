# 1) 
# - ICN에서 출발
# - 항공권 모두 이용. 
# - 경로 두개 이상이면 알파벳 순서가 앞서는 경로. 방문대상 시 알파벳 앞부터 넣기. 
# -> 경로

# 2) n=10,000 : 2000 에 더 가까우니까 ~O(n^2) 될지궁그
# 여러 경우의 수에 대하여 미방문 애들만 진행
# - 모두 이용 : while(left) : 
# - target="ICN" & 업뎃
# - 알파벳순 : m1_ nlogn충분하니까 미리 정렬_코드단순 m2_찾은 애들 알파벳 빠른 순서로 정렬 후 진행. # x[i][1] == x[i+1인 경우중에

# mC_걍 남은 거에서만하지 않고 visited으로 체크하며 통째로 n*n = n+ ..+n = n*n # +연결임 # 찾으면 break 라서 다 가지도 않음 # - 나중에 보니까 뇌에 스쳤던 저방법이 엄밀히 어떤 거였는지 모르겠네. 그런데 아이디어들 다 구체화해서 적기엔 푸는 시간 오바임. 쓸데없는거 패쓰~ 

# mA_ find 하고 제거하며 찾기 ~~ n+n-1+...1 = n(n+1)/2 
# mOtehr_visited넘겨주기


# 3)
# visited=[]

import copy
# - 어차피 시복 내인데 굳이 *n줄이기 등 여러 방식의 세부 구현에 시간을? 씀
#   + 함수에서의 다양한 변수타입 건네기를 통한 보다 더 깊은 이해 및 다른 변수 타입 사용 더 이해(?)
#   + 성공했던 방법들 따로 아래에 붙여넣을 걸 그랬나. 근데 어차피 그 성공했던 걸 주석으로 이론으로 글자화하긴 했음.
def dfs(target, dict1, answer, len_t , real_answer): # - N : 중복 출발지인 애 있으면 티켓들의 길이와 dict1길이 다름 
    # - (1) 종료조건
    if len(answer)== len_t +1: 
        # - 아래는 =이라 real_answer를 새변수에 재정의한 것이기에 이 dfs 나가면 정보를 잃어버림 -> 리스트인덱스수정법 [0]
        # real_answer = answer[:] # - dfs 끝에 있어서 시복이 곱하기 같지만, 정답 닿은 딱 한번만 복사되는 거임.
        real_answer[0]=answer[:]
        return 1 # - real_answer # - 함수가 사라질 때 그 함수에서 사용된 지역 변수도 사라지기 때문에 bfs 다시 올라갈 때( dfs를 함수로 구현 시 함수 탈출하며 자동으로 올라감.) 변수 계속 건네줘야함. 리스트면 주소참조라 안 건네줘도 되긴함.
    # - answer을 new_answer로 복사 안하고 하나로 쓰는 코드 작성해보기 : 굳이? for 돌 때 하나 붙였다가 뺐다가
    # - 함수에서 푸는데 전역 변수 쓰는 건 굳이.
    
    # - (2) 부모자식 # - dict1[target]에 있는 애들에 대해서만 dfs로 함수 쌓음
    # - ! [딕셔너리 조회] 시 주의!! GET 써라 GET    
    for index, airport in enumerate( dict1.get(target,[]) ): # 'ICN', 'AAA' # dict1[target]가 list인 거고 그 안 요소 각각은 한 개
        # - ! dict1.get(target)의 여러 개중에 airport '1개'만 쓴 거고, for 진행할 수록 airport 이전것들까지 다 쓴 거 아님[내려가는 경로인데 자식한꺼번에 옆층으로 먹는 경로는 아니지]. # - 그 중 한 티켓 쓰는 경우이고 나머지 요소인 티켓은 남아있지
        
        
        # - (3) 사용 
        # - 방문 미방문 검사 없는 이유는 자식들이면 다 쓰는 경우라서임. 
        
        # - 복사해도 시복 O(n^2). 이 문제에선 아슬아슬했는데 되네. (2000아니고 만이어도 됨) O(  n+ n(dfs) *n)
        
        # save=dict1[airport][:]
        # - ! target의 value를 빼야하는데(이전 방법에서도 그렇게 했는데) 이 방법 코드에선 실수로 [airport]로 해버림. airport가 너무 범용 단어다. depart arrive 등으로 하던지.
        
        
        # - 새 데이터로 변경한 이유 : 리딕셋 mutable은 다른 dfs에서 바꿔도 다 동기화 돼버림. -> 새dfs에 넣고 쓴 airport를 다시 append하여 해결
        #   + [단점이 큼]시복 *n [장점] 함수 끝나고 다시 그 요소 추가해줄 필요 없음 
        
        # - ! 딕셔너리 속 리스트 : 이중 뮤터블 -> deepcopy. 리(스트)딕(셔너리)셋(트)는 mutable이라 그냥 copy하면 그 주소를 가져와버려서 동기화돼버림
        #   + ["aa","bb"]는 요소에 길이가 있지만 요소가 뮤터블이 아니기에 단순 copy가능
        # new_dict1 = copy.deepcopy(dict1) 
        # new_dict1[target].remove(airport) 
        # - dict1에서 k_target인 v_리스트에서 airport인거만 뺀 거 # - ! [index]까지 사용완료아님 ## new_dict1[target]=dict1[target][index+1:] # # 현재 target의 airport 한 개 사용함 
        
        #   + 처음엔 맞게 pop 방향으로 했는데 인덱스 처리하기 귀찮아서 다르게 하다가 이상한 방법으로 해버렸네. ## pop하면 다음 for관련 인덱스에서 인덱스 바뀜. 새dfs호출 후 다시 inser로 붙이면 됨 dict1[airport].pop(index)   ## 요소인 리스트에서의 특정 요소만 빼기.
        
        
        # - 퀴즈 '똑같은 알고리즘의 answer 부분을 immutable인 튜플로 하면 전체복사 할 필요 없어서 효율 개선이겠는가?'' : -> 요소 추가하는게 O(n)이라 또이또이함(큰차이없음). 
        
        dict1[target].remove(airport)
        
        # - dict1과 다르게 answer는 복사하셨던 이유   (다른 것들에도 "바로"대답할수 있기== 빠르게 알고있음. 안까먹었음. 체화)-> answer관련 변수를 한 가지만 쓰면, 중간과정을 위한 append pop되는 answer가 정답 닿고 나서 거슬러 올라올 때도 pop되면서 정답을 잃음. 난 항상 복사해서 함수에 건네고 받는 대신 정답에 닿은 최종에만 복사. dict1은 정답을 구하기 위해 필요한 정보라 정답에 닿은 이후로 올라올 때 정보 잃어도 상관없음. 어차피 필요한 정보는 정답관련 변수하나임.
        answer.append(airport)
        # new_answer = answer[:] 
        # new_answer.append( airport )
        
        
        possible=dfs(airport, dict1 , answer, len_t,real_answer ) 
        # - ! len_t는 +1증가해야하는 거 아님. 변수 이름을 길더라도 len_tickets로 하든 N 으로 하든 의미 명확하게 해야 실수 안 한다.
        # - 디버깅하다가 오히려 더 이상하게 수정하기도 하네. 무조건 적인 다른 m으로 구현 보다, 디버깅보며 놓친 부분을 수정. 아니면 이전방법으로 돌아갈 수 있게 하던.
        
        # - dfs에 넣으려고 먹은 거 다시 뱉기 # - for문이라 이 dfs 아직 안끝나서 원상복귀해야함
        dict1[target].insert(index,airport) # -! append로 하면 우선순위가 뒤로 가게 돼서 원상복귀 아닌거임
        answer.pop() 
        # - ! answer 복사 안하기방법
        #   + 첫디버깅 : 모든 답이 	["ICN"] 로 나와서 알고리즘 크게 틀린줄 알았는데, dfs실행 시마다 인자 다 출력해보니 answer에 정답이 다 맞게 닿았었음.  -> dfs에서 최종 출력 답은 엄청 이상해도 안에서는 맞게 돌았을 수 있기에 출력해서 하나하나 보는 게 나음
        #     + 이유 : dfs가 끝까지 가서 answer= 정답에 이르고 다시 위층으로 돌아오면서, pop하기에 찾았던 정답을 반환해가버림. 함수가 반환한 answer를 can(real_answer인 자리에 최종 노드 위치에서의 복사 없이 있던 변수)이 저장하고 있지만 리스트라 주소 참조라서 answer pop할 때 can도 같이 pop돼버림 -> 튜플하면 주소참조는 아니라 ㄱㅊ겠지만 어차피 튜플 추가는 복사하는 O(N)이라 리스트에서 새거에 복사하는 거랑 시복 같음. 
        #     + m_string이용 : 마지막에 list화 해야하긴 하지만 총 O( _ +n )이라 곱하기 아니고 상쇄됨
        #     + m_real_answer 변수 추가.(했음) + return 일부를 answer->1로 변경. 근데 리스트 길어도 어차피 주소 return이라 answer return도 그렇게 안복잡했겠네. 그래도 내 방법에서 불필요한 부분을 1로 바꿈 및 성공=맞게 이해하고 있음. 돌아가는 꼴 쫌 더 자세히 맞게 이해했는지 확인
        #     + m_글로벌변수추가
        # - [튜플] 추가 :  근데 애초에 불변형인데 아래처럼 활용하는 게 덜 적합할 수 있음
        '''tup1=('aa') / tup1+=('bb')
        '''
        
        if possible : # - if 해야하는 이유 : real_answer 안 닿았으면 for의 다음 요소 돌아야하고 닿았으면 탈출해야하기에 여기에 있어야하는 조건임
            # - 자식중 빠른 알파벳이 끝까지 도착 성공했으면 더 볼 필요 없어서 for문 내에서 for문에서 나가야함. break 대신 return한 이유는 아래줄.
            return real_answer[0] # - 아래 말고 여기서 return 이유 : 해당 키가 하나의 value를 가지고 있어도 for문을 돌기에 맞는 답일 땐 항상 for문 실행함. for문 끝까지 돌았는데 정답 길이에 못 닿았다는 것은 틀렸다는 것임. 그래서 for 밖은 정답이 아닌 상황인 거임. 여기 말고 for 밖에서 return하면 None으로 자동 return임. # - ! 처음엔, break해서 for 탈출하면 어차피 함수 마지막라인 이라 자동 return돼서 break라는 코드 한 줄 줄일겸 여기에 리턴한줄 
    ## print('함수종료', target, dict1, answer, len_t,'dfs 함수 끝까지 갔는데 이번 경로에서 정답 없음.') 
    
    # return real_answer[0]  # - return None상황

def solution(tickets):
    
    # tickets.sort() # - 시복내라 굳이 안 한 최적화_딕셔너리에 겹치는 게 있을 때만 그 리스트에서 sort해주는 게 나음
    target="ICN"

    # - dfs/bfs : 연결맵, 맵, 그래프  
    dict1=dict()
    for i in range( len(tickets ) ): #  - ! range, len 차분히.  # - 인덱스 때문에 복잡해보이는데 다른 사람 코드처럼 for ticket in tickets으로 하면 단순해보임
        if dict1.get(tickets[i][0]) : ## get : 이미 해당 키가 있으면. 그 벨류값에 업데이트 해주기
            dict1[ tickets[i][0] ].append( tickets[i][1]   ) # - value를 리스트로 넣어놨음. 재할당 없이 그 위치에 바로 append 가능
            # renew=dict1[ tickets[i][0] ] [:]
            # renew.append( tickets[i][1]   )
            # dict1[ tickets[i][0] ]=renew # 원래 있던 값에 추가
            dict1[ tickets[i][0] ].sort()
        else : 
            dict1.update([ [  tickets[i][0],  [tickets[i][1]]     ]]) # - update(딕셔너리/2차원리스트/zip([],[]))
            
    answer = []
    answer.append(target)
    
    answer=dfs(target, dict1, answer, len(tickets),['Yet'] ) # dict1 : dfs 노드 가며 사용한 거에 따라 바뀜
    
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
                
                
                # continue #
    # answer.append(target) # i,f : 길이 3이면 출력 길이는 4임   
    # answer.append(target)
    return answer
# 4) 공항 수 3, .
# [["ICN", "JFK"], ["ICN", "JFK"],["JFK","ICN"]] -> ["ICN", "JFK","ICN", "JFK"]


# - ! [5) #$, #~]

# - 이런 뇌 속 이해는 시간 오래 지나면 까먹기도 한다. 코드 상 직관적인 돌아가기보다 머리 뇌속 돌아가기인 거는(dfs~)  미래용으로 나에게 설명 영상 찍기? 
#   + 다른 사람들도 코딩테스트는 바짝 끌어올리는 거라하는 거 보면 비슷한듯

# -  1h 12m 든 34m 순간이었든 34m : 두 케이스 시간초과 
#   > 시간초과로 정답봄

#   + 알파벳순이 전부 정답이 아님. 끝까지 도달 못 하는 것도 있음
#   + 만든 딕셔너리 사진을 기준으로, 그걸 자식 노드로 하는 bfs. bfs~ 연결노드맵생각


#   + 공부할겸 다른 사람 코드보다 복사부분 없앤 O(n)화? 코드 만들었댱 : 그런데 전체 sort말고 중복 출발지에 대한 sort 시복은 케이스마다 

# - 퀴즈 _빠른 알고리즘 돌아가는 꼴/시복 계산 촥촥 -> 딕셔너리 복사 시 총 시복 ->     O(n**2 이상인거 맞음) answer에 한 요소 추가할 때마다 티켓 다 담긴 딕셔너리 복사하므로.
#   + answer 복사 시 시복  ->  다른 사람 풀이 실행시간 보니까 나랑 시복 크게 차이 안나네. 테스트 케이스가 4개 밖에 없어서 다른 거에서 시간 절약하신 부분일까 answer복사는  매번 n 까진 아니고 dfs로 1, 2, 3 으로 복사해나가서 worstcase아니고는 시복이 식이 바뀔 정도로 ㄱㅊ한 건가 흐음. 시복은 worst로 인데.. 아 나 어차피 시복 내이라 sort최적화 안했어서 거기가 가장 큰 부분이 됐구나. n**2을 n으로 줄일거면 n**2부분 말고 상쇄 지워진 항도 살펴봐야함. 암튼 다른 사람풀이랑 시간 뭔가 비슷하네. 




# - 다른 사람 코드 [https://school.programmers.co.kr/learn/courses/30/lessons/43164/solution_groups?language=python3]
'''
from collections import defaultdict 

def dfs(graph, N, key, footprint): # - dfs ( [그래프],  _굳이_, v, [최종 정답일] 리스트 변수 # - ~~ bfs의 while
    # print(footprint)

    if len(footprint) == N + 1: ## - 탈출조건 
        return footprint

    for idx, country in enumerate(graph[key]): # - v의자식. 
        graph[key].pop(idx) # - (1) 딕셔너리에서 사용한 거 빼기
        tmp = footprint[:] # - (2) 결과에 금방 사용한 게 추가될 리스트 : dfs 의 노드 위치 마다 달라야하기 때문에 리스트 복사한 후 리뉴얼해서 건네
        tmp.append(country)
        
        ret = dfs(graph, N, country, tmp) # 
        
        graph[key].insert(idx, country) # - 이거 지우면 for 다음 항목 진행했을 때 티켓을 누적해서 빼버림# 이 dfs 위치 노드에서는 저거 안 사용했기 떄문에 다시 insert
        
        if ret: # - 끝까지 못 갔으면 dfs함수는 None을 반환했을 것임
            return ret # -  dfs에서 다시 위 노드로 거슬러 올라올 때, 종료케이스로 끝까지 간 애만 None아닌 것 반환하며 올라갈 수 있도록함


def solution(tickets):
    answer = []

    graph = defaultdict(list) # - collections에 있는 defaultdict(기본값 list로 설정)
    
    N = len(tickets)
    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        graph[ticket[0]].sort()

    answer = dfs(graph, N, "ICN", ["ICN"])

    return answer
'''