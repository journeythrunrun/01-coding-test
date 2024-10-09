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
    #heaptify
    q=[]
    for job in jobs :
        heapq.heappush(q, (job[1], job[0]) )
    total_time=0     
    current_time=0
    # for job in q :
    #     print(job)
    # [[0, 3], [1, 9], [10, 6]]
    while(q):
        used_time, start = heapq.heappop(q)
        #~ *
        q2=[]
        min_start=1001
        time_jump=False
        
        while (start > current_time): # start <= current_time이면 탈출. 아닌 상태에서 돌기
            min_start=min(min_start, start)
            heapq.heappush( q2, (used_time, start) )
            #print(q)
            try : #에러 안났을 때 try는 실행이 됐
                used_time, start = heapq.heappop(q)
            except :#~ finally
                #~ 시간패스
                time_jump=True
                #current_time=min_start # while문 첫줄도 합치기 & 귀찮
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
        
        
        # print(current_time, q)
    # mean = //
    #print(total_time)
    return total_time//len(jobs)
#4) jobs길이 1,2,.. ## [[1, 3]] 3 : 인덱스 초과 | 수행할 작업 없으면 시간 패스#~
# 요청 시각 0이상,. 
# 소요시간 1이상, |스타트시간=현재시간
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리 = min_start 
## <-두번째 요소의 정렬은 어케되지
# [[0, 3], [1, 9], [10, 6]] -> 인덱스 에러 

#   + 멍4분
# 500이하                       
# 힙큐이의 시간복잡도     
# 요청시점도 있는데 낮은것부터가 무조건? ( 평균의 해당 낮은 거의 값이 낮)

