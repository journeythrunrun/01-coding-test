# 0) numbers	target	return
# [1, 1, 1, 1, 1]	3	5

# 1) len(numbers): 2개~20개_ 요소=자연수 
# 더하거나 뺴서 타겟 값을 만들 수 있는 경우의 수

# 2) m1) 완전 탐색 : 2^(20)? : 시복 초과하겠다. 근데 2라서 그렇게 크진 않음 1000000정도네
# m2) 동일한 숫자는 더하거나 빼도 결과는 같음 
# -> 각 숫자의 개수(숫자가 다 다를 수 있어서 worst case 시복 줄이기에는 의미 없음. 부분점수면 가능하겠지)


# [0,1]
def solution(numbers, target):
    answer = 0
    to=[0,1]
    # m1-v1) 중복가능 ㅠ -> 함수이름 기억 안남 OR 만들기

    # m1-v2) 빈 앞은 0으로 채운 n자릿수의 bin()로 -> 이진수 0,1을 각 인덱스의 +,-로 맵핑
    max=int('1'*len(numbers)) # '11111'
    # 2진수에서 10진수로 돌아오는 코드는 뭐지
    # 에라이 함수 떠올리기 시도 시간보다 이건 그냥 구현하는게 훨씬 빠르네 (1만있는 케이스라 그랬을 수도 있음) => 아무튼, 구현도 되게 쉬울 수 있다 구현도 방법은 1차로 떠올려봐라.
    dec_max=sum([ 2**(i) for i in range(len(numbers))  ])
    
    index_numb=[]
    for a in range(0,dec_max+1): ## ex 0001 ~ 1111
        indexs=bin(a)[2:]
        str_indexs='0'*(len(numbers)-len(indexs) )+str(indexs) #앞에 0추가
        temp=sum([ +numbers[i] if str_indexs[i]=='0' else -numbers[i] for i in range( len(str_indexs))  ]) # 'if' 'else' 'for'임. []안에서 for이 맨 앞에 오면 에러 뜸. <-> 예전에 봤던 특정 강의자료 오류 있었나.
        if temp ==target:
            answer+=1 # answer+1은 디버깅에서 문법오류 안뜨고 끝까지 돌아가버림.
    # 굳이 '0'-> 0 이나 '0' -> + 맵핑하는 특정 변수 생성보다, if문으로 바로 연산    
    return answer
# 4) target=1 / 2개

# - 52분
#   + 문제 풀이법 보다, 코딩 피지컬에서 시간 많이씀

# - 2진수 등 -> 10진수화 [https://spec.tistory.com/475]
#   + m1) "0b" 붙어있는 것에 -> int(str1, 2)
# a = "0b11001000"
# print("2진수 -> 10진수 : ", int(a, 2))
#   + m2) 0b붙어 있는 숫자형식에 -> int(val1)
# a = 0b11001000
# print("2진수 -> 10진수 : ", int(a))


# - bfs dfs 장점이 무엇인가? (복잡상황 말고에서 itertools로 풀 수 있는 케이스에서 장점은?)
#   + itertools로 풀 수 있는 케이스면 그걸로 푸는 게 효율적임 
#    (( 왠지 이 상황에서 bfs장점이 뭐인가 싶더라 ))
# + 최소 경로 '케이스' 
# + '노드가 너무 많은 케이스(그래프 등)', itertools는 메모리 소비가 심할 수 있지만 bfs는 발자취만 임시로 가져갈 수 있음 

# + (복잡한 문제라서 BFS여야할 때)

# - DFS BFS문제긴 한데 안 쓴 사유 : dfs로도 풀 수 있을 것 같았는데 재귀함수 안좋대서(난 bfs 재귀로 구현했었음. 시간 많으면 재귀 아닌 bfs구현 다시 보던가) 다른 방법 사용
    


# - 확통_중복 ㅠ : "product"
#   + [ㅠ]product(자리구별/반복뽑[중복] 가능) [[프로프로프로]] / [P]permutations(자리구별o/반복x)
#   + combinations_with_replacement() ( 자리구별x / "반복o")
#   + combinations( 변수_iterable/2차원 리스트도 ㄱㄴ/.. , r ) # 한 껍질 벗긴 것에서 r개 뽑아줌

#   + m1) product(list1, repeat=3)_list1의 요소를 통째로[행이 될 수도 있음] repeat개 고름
#   + m2) product( *2rd_list)_list1의 각 행에서 1개씩 고름_반환하는 각 튜플의 요소 수 = list1의 행의 수  



# - 다른사람 코드 2[김현우 , 탈퇴한 사용자 , 박재민 , JayLee92 외 238 명]
#   + l = [(x, -x) for x in numbers]
    # print(l)
    #  print(list(product(*l))) # 두 껍질 내에 대한 구별된 경우의 수 . 
    # [GPT] l : 이중 리스트 or 리스트 속 튜플
    # * : unpack
    # repeat = 4랑 매우 다름

    # [(4, -4), (1, -1), (2, -2), (1, -1)]
    # [(4, 1, 2, 1), (4, 1, 2, -1), (4, 1, -2, 1), (4, 1, -2, -1), (4, -1, 2, 1), (4, -1, 2, -1), (4, -1, -2, 1), (4, -1, -2, -1), (-4, 1, 2, 1), (-4, 1, 2, -1), (-4, 1, -2, 1), (-4, 1, -2, -1), (-4, -1, 2, 1), (-4, -1, 2, -1), (-4, -1, -2, 1), (-4, -1, -2, -1)]

# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)


# - 더 들여다볼 필요 못 느낌
# - 다른 사람 코드1 [안대찬 , 양양 , 김나영 , 이준기 외 92 명]
#   ( 재귀네 & 이미 해결할 수 있는 문제의 수학적 specific해는 아닌가. 유형자체를 잘 몰라서 못 푸는 빈출이나 하자 ) 
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])




