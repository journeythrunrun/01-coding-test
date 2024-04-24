# 1) n번째 피보나치 수 % 1234567
# n : 100,000 이하인


def solution(n):
    if n==2:
        return 1
    cnt=2
    old1,old2=1,1
    while(1):
        cnt+=1 # cnt 번째 피보나치 / 3, 
        old1,old2=old2,old1+old2
        if cnt==n:
            break
    return old2% 1234567
# 반정도 맞은게 신기
# 4) 
# n=2