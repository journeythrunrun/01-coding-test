# A	B	answer
# [1, 4, 2]	[5, 4, 4]	29

# 1) a * b +=의 최소값
# 2) 가장 큰 값을 상대의 가장 작은거랑 곱하는 게 좋다 #~
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    
    
    return sum([ A[i]*B[-(i+1)]for i in range(len(A))])