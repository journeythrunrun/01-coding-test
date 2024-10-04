# 1) number를 표현할 수 있는 최소 N사용횟수 & 8보다 크면 -1
# -> 1회부터 모든 경우 따지며(기호 permutations/괄호 처리는?->귀찮아서 시간 꽤 걸릴줄 알고 해답으로 넘어갔는데 어차피 최대 8이라 괄호 넣어질 수 있는 위치 그렇게 많지 않았네)하며 쭉해나가
# 나누기 = //

# - 5m째인데 그냥 빨리 배우려고 DP정답봄((프로그래머스 알고리즘분류DP첫문제이기도 하고)) [ https://velog.io/@s2ul2/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level3-N%EC%9C%BC%EB%A1%9C-%ED%91%9C%ED%98%84-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC ]
#   + 최대 8이니까. 1회부터 모든 경우 따지며 '"각 횟수_최종관련"에 따른 만들 수 있는 수들'저장해나가기 & 그 수들 다 이용.  k 번 = ()번((으로 만들 수 있는 수들))  + ()번으로 분해.

#   + 괄호 : 괄호의 수학적 결과가 '먼저 연산되는 것'이라서, '같은 숫자를 사용'하여 연산하면, 앞 순서부터 사칙연산 경우 다 저장해나갔으면 커버됨. (즉 뒤에 괄호가 있던 거였으면 결국 계산이 거기서부터 시작된 거나 마찬가지라 ~~ 앞에서 해당 괄호 안에서의 사칙연산을 했던 경우와 결과 같음. 즉 수식을 앞부터가 아니라 계산 순서대로 생각하면 편함.)
#   + (i+1)-(j+1)번이 횟수이니까 인덱스로 사용할 때는 -1. # op2 : 피연산자2, N을 i-j번 사용하여 만들 수 있는 숫자들
def solution(N, number):
    
    # # s[i] : 주어진 수 N을 i+1번 사용해서 만들 수 있는 수들의 집합
    # s = [set() for x in range(8)] # set 8개 초기화, 왜 8개를 만드냐? N 사용횟수가 8보다 크면 -1을 return하므로 N을 1개부터 8개 까지 사용하여 만든 값들이 number가 안될 경우 -1을 return한다.
    # for i, x in enumerate(s, start = 1): # 보통 첫번째 원소의 idx는 0인데 여기서는 첫번째 원소의 idx를 1로 시작한다.
    #     x.add(int(str(N) * i)) # 8개의 set 각각 초기화, s[0] = {N}, s[1] = {NN ... s[7] = {NNNNNNNN (8개) # 경우의 수 중 ~개를 전부 연산 없이 썼을 때의 값.
    # for i in range(len(s)):  # 1,2, ..., 8 # s[i] 즉 N을 i+1개 사용했을 때 만들 수 있는 숫자 구하기.
    #     for j in range(i): # j < i : i +1개 = j+1번 + k번
    #         for op1 in s[j]: # N, 연산된, NNN # op1 : 피연산자1, N을 j+1번 사용하여 만들 수 있는 숫자들
    #             for op2 in s[i-j-1]: # + (i+1)-(j+1)번이 횟수이니까 인덱스로 사용할 때는 -1. # op2 : 피연산자2, N을 i-j번 사용하여 만들 수 있는 숫자들
    #                 # op1과 op2를 사칙연산 --> 즉 N을 i+1번 사용하여 만들 수 있는 숫자를 구하게 되고 이를 s[i]에 대입
    #                 s[i].add(op1 + op2)
    #                 s[i].add(op1 - op2)
    #                 s[i].add(op1 * op2)
    #                 if op2 != 0:
    #                     s[i].add(op1 // op2)
    #     if number in s[i]: # N을 i+1번 사용했을 때 찾고자하는 값 number가 존재한다면 i+1 return
    #         answer = i + 1
    #         break
    #     else: # N을 8번 사용했는데도 찾고자하는 값 number가 존재하지 않는다면 -1 return
    #         answer = -1
    # return answer
    
    
    
    # - set(int형) 불가. 애초에 형식 갖춘 iterable형만 가능.
    # print(set( int(  str(9)   *4 )  ) )
    cases= [set( [int( str(N)*i )   ] ) for i in range(1, 9)]
    # print(cases)
    for i in range(len(cases)): #i+1개를 사용해서 만들 수 있는지
        # i+1개 = j+1개  + k개 
        for j in range(i) : # i개 다쓰는 건 이미 cases 초기에 넣어놓음.
            
            for op1 in cases[i+1 -(j+1) -1 ] : # - '개수'를 '인덱스'(가장근접)에서 가져오려면 -1 # k개  
                for op2 in cases[j] :
                    
                    cases[i].add(op1+op2)
                    cases[i].add(op1-op2)
                    cases[i].add(op1*op2)
                    if op2!=0:
                        cases[i].add(op1/op2) # 반대 순서 : 반대로 k개 + j+1개 일때. 
                    
        
        if number in cases[i] :
            return i+1
    return -1
        
    