# 최소 평균 시간. 소수점 이하 버리기 // 

# 1) 작업 미수행 중일 때, 먼저 요청 들어온 작업 부터
# 2) 힙큐, 완전탐색 
# m3_각 시작 시간에 따라 heap정렬. 그 이후의 값들 사용
# 500이하 : O(n^3), n^2  -> 힙큐시간복잡도를 몰라서 계산하기가 애매하네
# -> 낮은 것부터.
# -> 대신 요청된 시간 이후 여야함. m1 다른힙큐에넣어서 그 이후에서 빼기?. 해당 시간지나면서 못썼던건 다음 큐에 넣어가고
# -> m2 pop하고 요청된 시간 이후아니면 다시 넣어

import heapq
def solution(jobs):
    q=[]
    
    for job in jobs :
        heapq.heappush(q, (job[1], job[0]) )
    total_time=0     
    current_time=0

    while(q):
        used_time, start = heapq.heappop(q)
        q2=[]
        min_start=1001
        time_jump=False
        
        while (start > current_time): #start <= current_time이면 탈출. 아닌 상태에서 돌기
            min_start=min(min_start, start)
            heapq.heappush( q2, (used_time, start) )
            try : # - 에러 안났을 때 try는 실행이 됨
                used_time, start = heapq.heappop(q)
            except :
                # 시간패스
                time_jump=True
                #여기에하기엔  while문 첫줄도 합치기 & 귀찮 #current_time=min_start 
                break
            # else :
            #     #print('에러 안났을 때 try는 실행이 됐나',q)
            #     pass
            #used_time, start = heapq.heappop(q)
        for job in q2 : #~ 여기선 이렇게 빼는 게 시복 더 나으려나 ## 뺀거 넣기
            heapq.heappush(q, job) 
        if time_jump==True :
            current_time=min_start
            continue
            
        # 작업 수행 시
        total_time+=current_time-start+used_time
        current_time+=used_time
        
        
#     while(q):
        
#         used_time, start = heapq.heappop(q)
#         #~ *
#         q2=[]
#         min_start=1001
#         time_jump=False
#         while (start > current_time):
#             min_start=min(min_start, start)
#             heapq.heappush( q2, (used_time, start) )
#             try :
#                 used_time, start = heapq.heappop(q)
#             except :#~ finally
#                 #~ 시간패스
#                 time_jump=True
#                 #current_time=min_start # while문 첫줄도 합치기 & 귀찮
#                 break
#             else :
#                 used_time, start = heapq.heappop(q)
#         for job in q2 : #~ 여기선 이렇게 빼는 게 시복 더 나으려나
#             heapq.heappush(q, job) 
#         if time_jump==True :
#             current_time=min_start
#             continue
            
#         # 작업 수행 시
#         total_time+=current_time-start+used_time
#         current_time+=used_time
    return total_time//len(jobs)
#4) jobs길이 1,2,.. ## [[1, 3]] 3 : 인덱스 초과 | 수행할 작업 없으면 시간 패스#~
# 요청 시각 0이상,. 
# 소요시간 1이상, |스타트시간=현재시간
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리 = min_start 
## <-두번째 요소의 정렬은 어케되지
# [[0, 3], [1, 9], [10, 6]] -> 인덱스 에러 

# - 1h 7m (+4점)_#
#   > 멍4분
#   + 디버깅 : 파이썬 문법 관련해서도 확인할 거 4번에 적어두기! 에러 안났을 때 try는 실행이 됨

# - try
# > 3) else: 쓸 거면  2)except:도 써야함.  
# 1) try : //실행됨
#     4 / 0
# > except  ZeroDivisionError as e[except 오류메시지]  :#~~오류케이스중_elif느낌 #오류이름 알면.
# 2) except : //오류시 # 나머지 오류_마지막에 와야 
# 3) else : // 오류 없을 시
# 4) finally: //무조건 실행 


# - 다른 사람 풀이 [이시윤 , 민재홍 , 조규관 , 양승민 외 10 명]
# -> 아래에 ->와같은 의문이 있어서 엄청 자세히 따지고 보진 않음
# import heapq
# from collections import deque

# def solution(jobs):
#     # - 정렬을 역순으로 해서 리스트에다가 pop해도 되는데 꼭 deque사용한 이유는?
#     tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
#     q = []
#     heapq.heappush(q, tasks.popleft())
#     current_time, total_response_time = 0, 0
#     while len(q) > 0:
#         dur, arr = heapq.heappop(q)
#         current_time = max(current_time + dur, arr + dur) # max : 당장 못쓰는 시각의 애면 arr+dur로 타임점프된 시각이용하여(arr+) 계산됨 
#         # -> 근데 시작 시각 더 빠른애중에 소요시간 좀더 긴 애 있을 수 있잖아. 400,9    1,10_소요
#         # -> 첫 번째 최소 애 무조건 계산? 100시작 1소요면 어케
#         # -> 이런 경우는 첫 프로세스가 엄청 길고 바로 직후에 오는 프로세스가 짧은 경우에, 수행을 안 하고 있을 때는 먼저 온 프로세스 먼저 수행한다는 규칙에 위반되지 않나요?[이유정]
#         total_response_time += current_time - arr # 타임점프한 시간은 뺌
#         while len(tasks) > 0 and tasks[0][1] <= current_time:
#             heapq.heappush(q, tasks.popleft())
#         if len(tasks) > 0 and len(q) == 0:
#             heapq.heappush(q, tasks.popleft())
#     return total_response_time // len(jobs)

# - heapq
#   + 두번째 요소도 같이 정렬됨
#   + 최대힙 : -를 두 번 [값에 -를 붙여서 넣었다가, 꺼낸 다음 다시 -를 붙이는 방식 가능]

#   + [시간복잡도]  < - > sort&pop이 나을 수 있다.  [https://nerdymint.tistory.com/20] 
#   + 그렇다면 heapq는 언제 사용하면 좋을까?
# 코딩테스트 상황처럼 빈 리스트에 새 원소들을 추가하며 최종적으로 정렬된 리스트를 얻어야 하는 상황보다는
# 새로운 데이터가 추가되어도 항상 정렬 상태를 유지해야 하는 상황이거나, 이미 정렬되어있는 리스트에 새 원소를 추가하는 경우에 유용하게 쓰일 수 있을 것 같다
#   + heappush O(logn) & N개_NlogN=Sigma(logN)   [https://math.stackexchange.com/questions/228744/value-of-summation-of-logn/228748#228748]
#   + heappop O(logN) : O(1)이 걸리는 일반 pop보다 훨씬 느리다
#   + heaptify O(N)


# - queue [큐] 
# m1) dequeue : 인덱싱 안쓸거면 리스트보다 디큐가 낫다.
# : 리스트와 달리, 삽입&삭제&앞&뒤 전부 O(1)
# : 인덱싱(,슬라이싱) 불가

# : 스택 / 큐 모두 대용 가능 
# : >  .append() & .pop() / .append() & .popleft()  OR  .appendleft() & .pop()

# > 큐 코드
# : 0) from collections import deque
# : 0) queue=deque() # deque가 한 자료형. set()같은 선언
# : 1)2)) queue.append() / queue.popleft() #  _queue.reverse()

# m2) Priority queue[우선순위 큐] 
# > m1) 리스트로 구현
# : 삽입_O(1), 삭제_O(n)_*그냥 pop()은 O(1). 우선순위 관련해서 구현하고 저렇게 쓰려면 O(n)인가. 
# : 우선순위대로 넣어주는 거 아니면 다시 sort해야함. NlogN
# > m2) heap[힙]으로 구현
# : 삽입_O(log N), 삭제_O(log N) : N개면 N log N

# - 2) (타임패쓰말고) 요청시점도 있는데 낮은것부터가 무조건? (해당 낮은 거로 인한 total_값이 낮. 이미 task들 누적돼있는 상황이면 소요시간 적은 거 부터 해야함.)

