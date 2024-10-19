# 소수 몇 개

# 2) n=7 0번~7번 permutations 
# str -> int
## 3) 
from itertools import permutations#~
def solution(numbers):
    answer=0
    # 중복선택 안됨. 자리구별있음. 중복숫자 안됨 # ㅠ말고 p 
    # 소수 효율 알고리즘 굳이?
    #~permu2
    counted_set=set([0,1]) # set
    for i in range(len(numbers)): 
        for case in permutations(numbers,i+1):# # i개 고르기 #('0', '1')
            
            # 소수인지 검사f
            str_output=''
            for one in case :
                str_output+=one
            output=int(str_output)
            #~print
            #print(output)
            # 소수 검사 : 자기 자신으로만 나눠져야
            is_count=True
            #~ 0과 1은 소수 아님
            for numb in range( 2, round(output**0.5)+1 ):##
                if output%numb==0:
                    # not count
                    is_count=False
                    break
            if is_count==True and output not in counted_set:
                counted_set.add(output)
                print(output)
                answer+=1
            
        
        
        
            
        # print(list(permutations(numbers,2))) #list(permutations(numbers,2))
    return answer
# 4) 길이 1,2 | 숫자 0 | 1050100
# 추가된 최종 시복 __!가능수준이라 ㄱㄴ

# - 19m


## 코테 후기 기록용으로 빨리 풀 수 있는 쉬운 문제로 골라서 품
# - 오늘 본 코테 조졌당! ㅎㅋㅋㅋㅋㅋ
#   + (1) [차근차근 풀기] 코테 풀 때 연습문제 풀 때랑 다르게 해버림. [2) 3) 조건이나 풀이 설계] 적기 거의 안 하고 시복 방법만 생각한 후 [급해서 일단 풀기시작해버림]
#     + 테스트 형/모의고사형으로 봐보자
#   + (2) 면접 준비 있더라도, 직렬로 면접에 너무 몰빵 말고 [코테 전에 '문제 풀'면서 감] 올리기
#   + (3) 코테 전날 잠 충분히 잘 수 있게 많이 처먹든 하기
#     > 문제 난이도 차이도 있겠지만 적게 잔 날 유독 뇌가 느리고 후딱 넘어가려하고(급하고) 쓰잘데기 없는 것까지 디버깅하게 되는 코드로 짜버리게 되 거나 생각 놓치게 되는 것 같음 
#   + (4) 공간 전환 ? 
#   + (5) 속도 느림? -> 그래서 더 급하게 풀려고 하고?