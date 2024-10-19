# 소수 몇 개

# 2) n=7 0번~7번 permutations 
# str -> int
## 3) 
from itertools import permutations
def solution(numbers):
    answer=0
    
    # - itertools 사용 시  
    #   + 시간복잡도 : 생성은 병렬덧셈 & 생성된 길이는 for아래와 곱하기임. for 옆에 있다고 생성도 곱하기로 착각은 놉
    #   + (1) 자리구별  있음. (2) [중복선택]  안됨.
    #   + ㅠ(product)말고 p (combinations_with_replacement도 말고)
    #소수 효율 알고리즘 굳이?
    
    counted_set=set([0,1]) 
    for i in range(len(numbers)): 
        for case in permutations(numbers,i+1):#i개 고르기 #('0', '1')
            
            str_output=''
            for one in case :
                str_output+=one 
                
            # - <-> 숏코딩 저정돈 타이핑과 가시성 둘 다 확보일련지. :a |= set(   map(int, map("".join, permutations(list(n), i + 1))))[1]
            #   + 중복된 숫자에 대해 소수 검사할 일 없도록 애초에 set에 집어 넣음
            #   + 굳이 for 말고 저렇게 저장하는 게 시복 나으련지. map이 훨?. 다른 케이스에 거쳐서 중복된 놈들 계산할 일 없게 되긴 하겠다. 근데 그건 검사했던 놈 set에 넣어서 검사할 수도 있긴 한데 코드 길이?
    
            output=int(str_output) # 앞0도제거됨
            
            # 소수 검사 : (1제외하고) 자기 자신으로만 나눠져야
            is_count=True
            # - 소수 : [0과 1]은 소수에서 빼기
            
            # - <-> 전체 소수 검사 for 한바퀴로만 끝낼 수 있는 방법[1]
            #   + for을 돌며 i에 따른 배수를 max(a)까지 a에서 제거
            # - set : set에 없는 원소 빼기 해도 괜찮음 
            # for i in range(2, int(max(a) ** 0.5) + 1):
            #     a -= set(range(i * 2, max(a) + 1, i))
            # return len(a)

            for numb in range( 2, round(output**0.5)+1 ):
                if output%numb==0:
                    # not count
                    is_count=False
                    break
            if is_count==True and output not in counted_set:
                # - <-> a -= set(range(0, 2)) 굳이
                #   > 0,1 두개 검사라 상수효과로 인해 시복 차이는 크게 없을 듯. 0,1은 어차피 소수검사 for문 안 돌게 되고.
                counted_set.add(output)
                answer+=1
    return answer
# 4) 길이 1,2 | 숫자 0 | 1050100
# 추가된 최종 시복 __!가능수준이라 ㄱㄴ

# - 19m(+1점)
#   > 코테 후기 기록용으로 빨리 풀 수 있는 쉬운 문제로 골라서 품

# - 오늘 본 코테 조졌당! ㅎㅋㅋㅋㅋㅋ
#   > 루피(뽀로로의 루피) 닮으신 연예인 분이 조졌네 이거~~ 하는 대사가 떠올랐었다ㅋㅋㅋㅎ
#   + (1) [차근차근 풀기] 코테 풀 때 연습문제 풀 때랑 다르게 해버림. [2) 3) 조건이나 풀이 설계] 적기 거의 안 하고 시복 충족 방법만 생각한 후 [급해서 일단 코딩해버림]
#     + (sol) 테스트형/모의고사형도 봐보자

#   + (2) 면접 준비 있더라도, 직렬로 면접에 너무 몰빵 말고 [코테 전에 '문제 풀'면서 감] 올리기
#   + (3) 코테 전날 [잠] 충분히 잘 수 있게 많이 처먹든 하기
#     > 문제 난이도 차이도 있겠지만 적게 잔 날 유독 뇌가 느리고 후딱 넘어가려하고(급하고) 쓰잘데기 없는 것까지 디버깅하게 되는 코드로 짜버리게 되 거나 생각 놓치게 되는 것 같음 
#   + (4) [공간 전환] ? 
#   + (5) [속도 제한 5,40m]으로 낮추기? 문제 풀면서 자연스레?
#     > 느려서서 더 급하게 풀려고 했으려나

# - 다른 사람 풀이 [1] 김현우 , 윤수현 , 한동준 , 임재현 외 182 명
#   + [회전마다 최대값까지의 배수제거해서 소수만 남기기법]시복 더 좋음. 내 방법은 시간복잡도 이내길래 그냥 코딩 쉬운 방법으로 풀었음
# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)


