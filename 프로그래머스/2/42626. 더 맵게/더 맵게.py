# 1) 
# 모든 음식의 스코빌 지수를 K이상 될때까지
#  first + second*2
# -> 섞어야 하는 최소 횟수 / 불가능 = -1

# 2) 백만 : O(n) , 운좋으면 O(n log n )

# 계산한값 또 sort 안하려면 우선순위큐. 
import heapq
def solution(scoville, K):
    q=[]
    # - 리스트 요소들 한 번에 heapq에 각 요소로 넣는 법 : heapq.heapify(scoville)
    for one in scoville : 
        heapq.heappush(q, one )
    answer=-1
    old_answer=0
    while ( 1 ):
        if len(q)==1 :
            if heapq.heappop(q) >=K :
                answer=old_answer
            else :
                answer=-1
            break
            
        one=heapq.heappop(q)
        if one >=K :
            answer=old_answer
            break
        two=heapq.heappop(q) # - heapq.heappop(q)
        heapq.heappush(q, one+two*2)
        #print(heapq.heappop(q))
        # if new > = K:
        #     break
        # print(q)
        old_answer+=1

    return answer
# 4) 길이 2, K= 0,1, ..

# - 21m (+4점)


