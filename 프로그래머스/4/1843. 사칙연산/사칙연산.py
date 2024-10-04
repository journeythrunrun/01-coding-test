# 1)
# 숫자, +, - 
# -> 다른 연산순서 결과중 최대값

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
#         # 값 동기화 . 리스트로. ! 새 리스트로 정의 말고 해당 리스트의 값에 반영해야함.
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

#  - 다른 사람 풀이 씀 [https://www.ai-bio.info/programmers/1843]

def solution(arr):
    M, m = {}, {}

    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    
    for i in range(len(nums)):
        M[(i, i)] = nums[i]
        m[(i, i)] = nums[i]
    
    for d in range(1, len(nums)):
        for i in range(len(nums)):
            j = i + d
            if j >= len(nums):
                continue
            
            maxcandidates, mincandidates = [], []
            for k in range(i+1, j+1):
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

