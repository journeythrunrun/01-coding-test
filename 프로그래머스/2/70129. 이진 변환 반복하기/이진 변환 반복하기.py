# s	result
# "110010101001"	[3,8]
# 1) 1. 모든 0 제거 
#    2. 길이를 2진법으로 표현한 문자열 # 4 ->100 
#    > s가 '1'이 될 때까지 [변환 횟수, 제거된 0수]

# 2) 

    
def solution(s):
    answer = [0,0]
    # a=''.join(list(reversed('abc'))) # 개수가 필요한거라 reverse 할 필요없음
    # print(a)
    count=0
    while(1):
        
        leng=s.count('0')
        answer[1]+=leng
        target=len(s)-leng
        temp=''
        if target==1:
            temp='1'
        else: 
            while(1):# 2
                temp+=str(target %2) # 0
                if target//2==1: # 1
                    temp+=str(target//2)
                    break
                target=target//2
        count+=1
        if temp=='1':
            answer[0]=count
            break
        s=temp
    
    return answer