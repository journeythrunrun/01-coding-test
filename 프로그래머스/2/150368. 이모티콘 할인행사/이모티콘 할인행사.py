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

# 몇개월간 쉬운 문제푸니까 속도는 좀 올라도 좀 더 어려웠던문제 사용했던 기법들 다 까먹었네

from itertools import product
# 100원단위 : # 내가 처리하는 단계는아니네
def solution(users, emoticons):
    answer = []
    # 두자리까지 출력법
    dict1={10:0, 20:1,30:2, 40:3}
    users.sort(key=lambda x:x[0], reverse=True)# [[40, 10000], [25, 10000]]
    for discounts in product([10 , 20, 30, 40],repeat=len(emoticons)): # 영상체크 ## per=할인율 product   # products할인율
        fee=[0,0,0,0]# -> 할인율에 따른 총합값 딕셔너리 저장
        for i in range(len(emoticons)-1,-1,-1): # 모듈씩디버깅
            # 100-40
            # +=임
            fee[ dict1[ discounts[i]  ] ]+=emoticons[i]*(100-discounts[i])*0.01#[i]# 계산 많이 할테니 미리 #+old아님
        old=0
        for i in range(3,-1,-1):
            fee[i]+=old
            old=fee[i]
        # 윗값 더하기
        # print(fee)
        
        resu=[0,0] 

        for auser in users : # [40, 10000],
            #  0.30000000000000004
            # *10 ㅑint?
            auser[0] = int ( ( (auser[0]-1)//10+1 )* 10 ) # 1~10->10*0.01 / 11~20->20*0.01 # 비율 퀀타이제이션
            if fee[ dict1[auser[0] ] ] >=auser[1]: # *0.01이 소수점돼서 안맞고 그러진 않겠지 /는? 그 파이썬체크
                resu[0]=resu[0]+1
            else :
                resu[1]+=fee[ dict1[auser[0]] ] 
                # print('1',resu[1])
        # answer= if answer[0]
        answer.append(resu)
    #sort 대신 압축화 굳이
    answer.sort( reverse=True) # nlogn도 여기 위치는 되려나 2^8 : 충분 # 2순위도 sort해야지 
    
    return answer[0]
# 1h 23m : sort 비압축