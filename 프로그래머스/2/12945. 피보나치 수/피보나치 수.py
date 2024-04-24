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
# 4) 
# n=2

# - 6m / +6점
#  > 피보나치 수 문제 최근에 읽었었음. 동적계획법. m2) 재귀 f()+f()

# - 디버깅
#   + return때 %안했는데 제출 테스트 케이스 반정도 맞은게 신기. 반 밖에에 가까움((보다 작은 값이었어서 가능))


# - 다른 사람 코드 [윤종민 , 문형섭 , 김지혁 , 이석곤 외 67 명]
#   + 첫 old값을 0번째 피보나치수부터 시작함으로써, 베이스케이스(n=2)가 반복문에 포함되게 함
#   + 반복 횟수   
#     while말고 for속에서 n번함 - 연산, 피보나치 번째는 1회씩임 | (old2로 return하면 n-1번만 해도 되긴함 )

# # 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# # 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def fibonacci(num):
#     a, b = 0, 1
#     for i in range(num):
#         a, b = b, a+b
#     return a

# # 아래는 테스트로 출력해 보기 위한 코드입니다.
# print(fibonacci(3))
