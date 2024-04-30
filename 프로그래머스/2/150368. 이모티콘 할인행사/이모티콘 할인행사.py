## 컨셉잡고 설명해봐야지

# 0)
# users(#100)	emoticons(#7)	result
# [[40비율, 10000맥시멈], [25, 10000]]	[7000, 9000]	[1, 5400]

# 1) 가입자 최대화 , 판매액 최대화
# n 명의 사용자에게 m 개를 할인 판매 (할인율 0.1 , 0.2, 0.3, 0.4)

# 사용자_[비율]이상 할인하는 거 전부 구매-> 합이 일정 [가격] 이상이면, 모든 구매 취소 & 플러스 가입

# 2) 이모티콘 별 할인율 up , down - > 유저 가격계산
# - 이모티콘 짧네 - 유저 더짧
# - m)완전탐색 우선? 
# -> users.sort(key=lambda x:x[0], reverse=True) / per=할인율 product 
# -> for in per # products할인율  -> 할인율에 따른 값 딕셔너리 저장
# & resu=[0,0] & for in users  i) 유저의 할인율보다 낮은 거 있으면 break ii) resu[1]+= / i) total이 일정가격이상: resu[0]+=1, resu[1]=0  ii) 
# ->

# [어려운 문제 위주로 효율적으로 풀자] ( 몇개월간 쉬운 문제로 꽤 푸니까 속도는 좀 올라도, 예전에 어려운 문제 풀던 때 사용했던 기법들 잘 모름(걍 코딩테스트는 너무 바쁘지 않은 방학 때 등 discrete하게 하면 그렇게 되고 특정기간때 continuous하게 끌어올려야하는 거라 그럴 수도 있음) )

# [t] 2)에서 시간 너무 많이 쓴 것 같다. 2)에서는 비세부 비계산 '틀만 설계' 하려하자
from itertools import product
## 100원단위 # 내가 처리하는 단계는 아니네[필요없네]
def solution(users, emoticons):
    answer = []
    answer2=[0,0]
    # 두자리까지 출력법
    dict1={10:0, 20:1, 30:2, 40:3}
    users.sort(key=lambda x:x[0], reverse=True)# [[40, 10000], [25, 10000]]
    for discounts in product([10 , 20, 30, 40],repeat=len(emoticons)): 
        fee=[0,0,0,0] # 할인율에 따른 총합값 딕셔너리 저장
        for i in range(len(emoticons)):
            # 디버깅 : '할인'율-> 100- 40
            # 디버깅 : +=임
            fee[ dict1[ discounts[i]  ] ]+=emoticons[i]*(100-discounts[i])*0.01 # 유저 단계에서 하면 계산 많이 할테니 미리 했음 
        old=0
        for i in range(3,-1,-1):
            fee[i]+=old # 윗단에서 누적하면 안됨. 윗단은 서로 다른 많은 이모티콘에 대한 거임.
            old=fee[i]
        # > 윗값 더하기 ## 유저가 가지는 할인율에 따른 이모티콘값(할인율 이상 전부 구매)
        
        resu=[0,0] 
        for auser in users : # [40, 10000],
            auser[0] = int ( ( (auser[0]-1)//10+1 )* 10 ) # 1~10->10*0.01 / 11~20->20*0.01 # 비율 퀀타이제이션
            if fee[ dict1[auser[0] ] ] >=auser[1]:
                resu[0]=resu[0]+1
            else :
                resu[1]+=fee[ dict1[auser[0]] ] 
        ## sort 압축해도 시간 차이 없음. 이 데이터라 그런가
        # answer2 = [resu[0],max(resu[1],answer2[1])] if resu[0] == answer2[0] else ( [ resu[0],resu[1] ] if resu[0]>=answer2[0] else [ answer2[0],answer2[1]] )
    # return answer2            
        answer.append(resu)
    answer.sort( reverse=True) # nlogn <- 2^8*100 : 충분 # 디버깅 : 2순위도 sort해야지  ## sort 대신 압축화 굳이
    return answer[0]
    
# 1h 23m / +2 
# * 코드 짜면서 모듈씩 출력체크 (디버깅에서 하려면 더 찾기 오래 걸림 & 이것저것 수정)
# - 파이썬 실수 계산 오차 조심
#   + M1) round(number, 2) # 소수점 둘째자리까지 반올림 # O(1)
#   + M2) f'{number:.2f}'

# - 다른 사람 코드 
#   + 시복면에서는 내 께 나음: O(user)+O(emotion)임(* 아님)  
#       + sol) * O(7) 수준이었으면 그냥 연산해라. (물론 7 아닐 땐 worst case에서 좋겠지만)
#   + 난 [코딩 속도가 느려] 
#       + sol) '기출문제'에서 자동으로 섞여있는 코딩구현 연습해 # '쉬운 문제'에서 연습해도 얻는 것 효율 별로임
