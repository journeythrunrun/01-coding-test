# 0) numbers	target	return
# [1, 1, 1, 1, 1]	3	5

# 1) len(numbers): 2개~20개_ 요소=자연수 
# 더하거나 뺴서 타겟 값을 만들 수 있는 경우의 수

# 2) m1) 완전 탐색 : 2^(20)? : 시복 초과하겠다. 근데 2라서 그렇게 크진 않음 1000000정도네
# m2) 동일한 숫자는 더하거나 빼도 결과는 같음 
# -> 각 숫자의 개수(숫자가 다 다를 수 있어서 worst case 시복 줄이기에는 의미 없음. 부분점수면 가능하겠지)


# [0,1]
# from itertools import pi
def solution(numbers, target):
    answer = 0
    to=[0,1]
    # 중복가능 ㅠ -> 함수이름 기억 안나면 직접 만들기? 빈 앞은 0으로 채운 n자릿수의 bin()로
    # print(list(permutations([0,1], 2)) )
    
    # 
    max=int('1'*len(numbers)) # '11111'
    # 2진수에서 10진수로 돌아오는 코드는 뭐지
    # 에라이 그냥 구현하는게 훨씬 빠르네 이건 (1만있는 케이스라)
    dec_max=sum([ 2**(i) for i in range(len(numbers))  ])
    
    index_numb=[]
    for a in range(0,dec_max+1): ## ex '0001' ~ '1111'
        indexs=bin(a)[2:]
        str_indexs='0'*(len(numbers)-len(indexs) )+str(indexs)   #앞에 0추가
        # index_numb.append(str_indexs)
        # print(str_indexs)
        temp=sum([ +numbers[i] if str_indexs[i]=='0' else -numbers[i] for i in range( len(str_indexs))  ]) #~
        # print( temp)
        if temp ==target:
            answer+=1 # answer+1은 오류 안뜨네
    
    
    # for b in asum: # str
    #     if b== target :
    #         answer+=1
    # amap=[[0,1] for _ in range(len(numbers))]
    
    
    # bfs dfs장점 / 이건 아마 bfs
    return answer
# 4) target=1 / 2개



