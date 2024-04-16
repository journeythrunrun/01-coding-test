# 0) 입출력 예
# s	answer
# "()()"	true

# 2) m1) 스택으로 짝꿍 
# m2) count 
# * 괄호 끝까지 가봐야 True일지 F일지 암 : "(()("


def solution(s):
    answer = True
    count=0
    for a in s :
        if a =='(':
            count+=1
        else:
            count-=1
        if count <0: # 이미 끝까지 안 봐도 어그러짐
            return False
    # 여기까지 온 거 : 항상 (가 더 많았음
    #  -> 그 (가 잘 닫혔는지 확인
    if count!=0:
        return False
    return True
# - 7m / +2점
#  > 근데 어디선가 같은 거 풀어봄. 저 count 해결법이 뇌 어딘가에 있었어서 빨리 풀었을 수 있음