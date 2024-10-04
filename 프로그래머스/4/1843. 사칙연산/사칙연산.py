# 1)
# 숫자, +, - 
# -> 다른 연산순서 결과 중 최대값

# 2) N 201 -> O(N^3).  O(N^4)는 운 좋으면

# '괄호 및 계산'-> '연산 순서'숫자들  -> 연산한 숫자 & 나머지 arr
# = m1)_itertools, p로도 가능? (숫자 인덱스 덩어리들 에서 ) [1],3,5, 해당 앞뒤 숫자 연산 
# = m2_ dp로 풀어보고 싶
# 숫자들 연산 결과 가지고 있. 나머지랑 계산.

# from itertools import permutations

# def solution(arr):
#     targets= range(1,len(arr) , 2)# range (len(arr)//2 )
    

    # print( list( permutations( targets , len(arr)//2  ) ) ) # 0,1,2  2,0,1결과는 겹치는데 이정도야뭐. (dp ㅜ)
    # first=True    
#     # 시복 . ㅠ는 아니어도 조합아니라 높지. 
#     for indexs in permutations( targets , len(arr)//2  ) : # 꼭 연산자가 i,j,k 3개로 고정되는건 아니니까. #	(0, 1, 2)
#         answer=1
#         # print(indexs)
#         try :# 두개 리스트 아니면 리스트화 
#             # 리스트면 못할
#             int( arr[index-1][0] ) 
            
#         else :     
        
#         # 리스트 아니면 str이라 둘다 [0] ㄱㅊ
#         arr2=arr.copy()
#         #~ 미리 리스트화? 
#         for i in range(len(arr2)) :
#             arr2[i]= [arr2[i]]
#         #print(indexs)
#         # - 값 동기화 = 리스트로. ! 새 리스트로 정의 말고, 해당 리스트 = 리스트 하면서 해당 리스트의 값을 바꾸며 반영해야함.
#         for index in indexs:              
#             if arr2[index][0]=='-': ## [0] : arr2 요소 다 리스트화 햇으면  arr2다 체크해야지. 
#                 value =  int( arr2[index-1] [0] )- int( arr2[index+1][0] ) 
#                 arr2[index-1][0]=  value
#                 arr2[index+1]=  arr2[index-1] 

#             else :
#                 value =  int( arr2[index-1] [0] )+ int( arr2[index+1][0] ) 
#                 arr2[index-1][0]=  value
#                 arr2[index+1]=  arr2[index-1] 

#                 # arr2[index-1]=  [ int( arr2[index-1][0] )+int( arr2[index+1][0] ) ]
#                 # arr2[index+1]= arr2[index-1]
#             old_answer=arr2[index+1][0]
#             #print (arr2, old_answer)
#         # else :
#         #     answer = max(answer,  )
#         if first==True:
#             answer=old_answer
#         else :
#             answer=max(answer, old_answer)
#         first=False
        

    # return answer

# - 저번 문제 다시 풀어보기
# 4) arr 길이 3,5,.. = 숫자 개수 2개,3 ..
# 숫자 = 1, ... 
# 결과 음수일 수 있어서 초기값 설정 귀찮 : 초기 임시값 설정 대신 초기인지 조건문으로 체크하고 값 할당

# - 1h : 풀이법 시복초과 ( 초반에 permutations 시복 적당하게 생각하고 풀어버렸었음_(n//2)! ~ . r이 전부라서 시복 큼 )

#  - 다른 사람 풀이 씀 (+6점)[https://www.ai-bio.info/programmers/1843]
#   + DP = 문제 '분할', 점화식

#   + 연산 -> '구간 분할'-> 짧은 구간 부터 DP
#   + 1) 나올 수 있는 연산의 최댓값, 최솟값을 저장해 두어야 한다.
#     + M[(i, j)], m : 'nums[i] 부터 nums[j] 까지 연산했을 때 나올 수 있는 M,m값' 구간 두 개로 나누기
#   + i~j 구간이 i~k-1, k~j 의 두 구간으로 나뉜다고 하자
#   + ops[k-1]의 경우에 따라 나뉜다 ##k-1연산자는 k숫자 k+1숫자를 계산함

# i. ops[k-1] == '-'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] - m[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] - M[(k, j)] 를 기억해둔다.

# ii. ops[k-1] == '+'인 경우,
# 최댓값을 위해서는 M[(i, k-1)] + M[(k, j)] 를 기억해둔다.
# 최솟값을 위해서는 m[(i, k-1)] + m[(k, j)] 를 기억해둔다.

def solution(arr):
    M, m = {}, {} # - 기본 = 딕셔너리

    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    
    # - M, m 단일 숫자 본인 위치 값
    for i in range(len(nums)): # 숫자값들 넣어놓은 1차원 인덱스를 i,i 2차원인덱스화
        M[(i, i)] = nums[i] # 딕셔너리 k,v 추가.
        m[(i, i)] = nums[i] 
    
    # - 기호 기준 분할 
    for d in range(1, len(nums)):# - i와 j 사이의 거리 1. 가장 짧은 구간부터 모든 위치에서 차근차근 구해나감.  #[i,j_i보다큼]위해 d는 아래의 i에서 1씩 더 추가하며 j로 사용
        for i in range(len(nums)): # i는 nums 인덱스 따라 증가.
            j = i + d
            if j >= len(nums): # 간격 뒤쪽인 j가 nums 인덱스 초과
                continue
            
            maxcandidates, mincandidates = [], []
            
            # - 기호기준 분할한 값 연산
            for k in range(i+1, j+1): # k = i+1~j # [i,j]를 나누는거니까 i+1부터 j까지. 
                # - 이 방법이 처음부터 잘 연산되는 이유 : 자동으로 가장 작은 간격인 i~j=길이2(d=1)_계산=M(a,a), m(b,b) 값들 부터 이용.
                
                if ops[k-1] == '-':
                    mx = M[(i, k-1)] - m[(k, j)]
                    mn = m[(i, k-1)] - M[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
                else:
                    mx = M[(i, k-1)] + M[(k, j)]
                    mn = m[(i, k-1)] + m[(k, j)]
                    maxcandidates.append(mx)
                    mincandidates.append(mn)
            
            M[(i, j)] = max(maxcandidates)
            m[(i, j)] = min(mincandidates)
                    
    return M[(0, len(nums) - 1)]


# - 써보기 
    ops=arr[1::2]
    numbers=[ int(object) for object in arr[::2] ] 
    M,m={},{}
    for i in range(len(numbers)):
        M[ (i,i) ]=numbers[i]
        m[ (i,i) ]=numbers[i]
        
    # - 3)_1 짧은 구간 부터, 구간별 M,m  # 여긴 쪼개기라기엔(3)_3이 쪼개기 ) 쫌 애매하긴함. 완전 커버 되게만 두개로 쪼개는 건 아니라 [i,j]일때 항상 i=0 j=마지막 은 아니니까. 
    for length in range(2, len(numbers) +1 ): # 길이가 2인 구간~길이가 전체인 구간
        # 5,3,1,2,4 # - 딥러닝 윈도우 비슷~len(numbers_5)-(length_2-1)=4 # +-1상수는 특정케이스 한개로, 나머지 len(numbers) - length는 증감 체크
        for case in range( len(numbers)-(length-1)  ) : # - case = start. 변수이름 더 의미 가지게.
            
            # = !! M, m 값 찾기. 
            # - !! 아래의 다양한 쪼개기 경우에서 'M, m값.'. 부호로만 나누는 M,m화가 전부가 아님
            M_candidate, m_candidate= [],[]
            
            # 3)_3
            for k in range( length-1 ) : # 길이가 4처럼 length로 고정돼있다면, 어디서 쪼갤지
                
                # 3) 길이 2_(5,3)에서의 M,m구하기 (적기 good 3)구체화된다 ) 
                # - 중요 !! 알고리즘 의미 인덱스!  :[case] ~  k위치에서 쪼개~ [case+length-1] # - 이 인덱스를 미리 해둘걸? [start] ~[middle]~ [end]. middle은 start+k같은 것보다, middle자체의 값으로 해야 안 헷갈림. middle=start+k를 해두던가. 
                
#                 # - k는 0부터라 [case]보다 큰 값 아님.
                if ops[case+k]=='+': # - 얠 왜 case로 했었냐. case+k임... 쪼개진 위치의 중간인덱스 ##ops[case] <-> number[case], number [case+1]
                    M_candidate.append( M[ (case, case+ k ) ]+M[ ( case+k+1 , case+length -1 ) ] )
                    m_candidate.append( m[ (case, case+k ) ]+m[ (case+ k+1 , case+length -1 ) ] )
                else :
                    M_candidate.append(M[ (case, case+k ) ]-m[ ( case+k+1 , case+length -1 ) ] )
                    m_candidate.append(m[ (case, case+k ) ]-M[ ( case+k+1 , case+length -1 ) ] )

            M[ (case, case+length -1) ] = max(M_candidate)
            m[ (case, case+length -1) ] = min(m_candidate) # - ! 여기도 max로 복붙실화냐. 걍 기왕이면 복붙을 쓰지 말자
        
    # - ! return 위치가 for문 안 이었음. 해당 위치에서 answer=마지막 때의 old_answer로 하는 거랑 거기서 'return'해버려서 첫번째 때의 값을 가져오는거랑은 다름.
    return  M[ ( 0, len(numbers)-1 )  ] # - ! ()
    