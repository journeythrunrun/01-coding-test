# 1) 원 형 집들. 인접한 두 집 털면 -> 경보
# -> 도둑이 훔칠 수 있는 돈 최댓값

# 2) money 길이 : 백만 O(n), 운 좋으면 O(nlogn) 
# - dp. 해당 위치까지의 최대값 ?  
# - 원형 처리 : 초기값 점화식? 완전탐색 회전활때 막판에 맨앞 인덱쓰가지 추가 계산?
# 점화식인데 옆 여러개씩?
# [1,2,3,1000, 3,_4 ,_1000,] # 4개? 
# [1,2,3,1000, 3,4,5, 1000,]
# m_x) 저번 문제 처럼 길이 계속 돌기엔 O(n)이라 한방이어야함. 
# 네개씩 추가? 분할?

# o x | o x | o x x o| x x_뒷애때문에 얘 x로 바꾸면.  o_| x o # 분할 가능한 곳 찾기 . 
# - m1) 더 좋은 값 나오면 바로 이전 값 pop 하고 지금꺼 먹음. 근데 이전 거 pop할 때 먹을 수 있게 된게 있을 수 있음. 그럼 그것 까진 붙여놓기? 그럼한도 끝도 없는데. 
#   + 일단 먹고, 나중에 pop하게 될 시 : 
# - m2) 2개나 4개씩 
# - 먹는 것 사이에 i. 안 먹은 게 2개있는 경우 == 4개봤을 때 양쪽 끝 두개가 나아서., ii. 1개 있는 경우 

# o x x (o) or o x o (x)  or x o x (o) 
# [1,2,3,1000, 3,_4 ,_1000,] # 4개? 
def solution(money): # 
    dp=[]
    
    if len(money)==3:
        return max(money)
    # 네개부터인 수식이라.
    dp.append( [ money[0],0] )
    dp.append( [ money[1],money[0]] ) # x , o   | o , x
    first=[]

    if money[0] >money[1] :
        first.append(True)
    dp.append( [ money[0]+money[2], max( money[1] ,money[0] )  ]  ) # , x,o | x, o,x | o, x , x
    #~ oxxo케이스 커버안
    
    for i in range(len(money) -3 ):
        a,b,c,d=i,(i+1)%len(money), (i+2)%len(money), (i+3)%len(money)

        # dp[d]
        #print(money[d])
        #print('first', first)
        if i == len(money)-4 and first==[True, True]:
            #print(first)
            dp.append( [dp[c][1] + money[d] -money[0] , max ( dp[c][0]+0, dp[c][1]   ) ]   )#먹 (첫번째꺼 더해졌었다면 빼야함), 안먹(저번꺼먹어도 되고 안먹어도됨.)
        else :
            if i==0 and dp[c][0] > dp[c][1] : # 저번꺼 먹음
                first.append(True)
            dp.append( [dp[c][1] + money[d]  , max ( dp[c][0]+0, dp[c][1]   ) ]   )#먹, 안먹(저번꺼먹어도 되고 안먹어도됨.)
            # 케이스에 따라 체크 귀찮다.
            
        
        #~ dp.append( [ max( dp[c][1] , dp) + money[d]  , dp[c][0]+0   ]   )#먹, 안먹
        # dp.append( [ max(dp[a][0]+dp[b][1]+dp[c][1] + money[d], dp[a][1]+dp[b][0]+dp[c][1] + money[d] ) , dp[a][0]+dp[b][1]+dp[c][0]+0   ]   )#먹, 안먹
        #print(dp)
    #print(dp[-1])
    # 마지막엔 중복해서 더해지면 안되니까. 식 약간 바뀜 : 마지막꺼 먹거나 안먹거나.
    # & 첫놈과 마지막놈 동시에 못먹음. - for문안에서 해야하나. 
    return max(dp[-1]) # max ( money[0]+dp[-1][1], dp[-1][0]  ) # max(dp[-1])# max(  [dp[-1][1]  , max ( dp[-1][0]+0, dp[-1][1]   ) ]   ) #마지막꺼 안먹거나 먹거나 [dp[c][1] + money[d]  , max ( dp[c][0]+0, dp[c][1]   ) ] 
    # return max(dp[-1])
    # dp=[ , , , ] # a,  b ,c,d에서 c기준으로 다음 인덱스까지 봤을 때 c까지의 최대값. b는 그렇게 결정된 old값.
    # 3) a를 먹었을 때의 max값 a를 안 먹었을 때의 max값. 새로운 애 만나고 pop하면 먹고 안먹는거 바꿔. -> 안먹는 '값을' 저장해놔. 그 money각값들 이어서 pop하는게 아니라. 
    # 20m
#     old_dp=[  ] # [ [먹, 안먹]
#     for i in range( len(money)  ): 
#         # - 연속으로 못먹으니까. 
#         # i. 바로 저번꺼 '안먹고' 이번꺼 '먹'는 게, (저번꺼 먹고 이번꺼 안먹는 것보다) 더 크다면  # 같으면 먹지마 
#         # -> i 먹
        
#         ## 네 케이스 중에 큰 값으로 
#         if old_dp[i-1][1]+money[i]>old_dp[i-1][0]+0 :
#             old_dp.append( [old_dp[i-1][1]+ money[i], old_dp[i-1][]  ] ) # 먹고 안먹는다 저장은 조건무관하게 똑같으려나
            
#             ## max값은 마지막 return때 
#             #~ 나머지값 저장 처리?
#         else : 
#         # ii. 바로 저번꺼 먹고 이번꺼 안먹는 게 더 크다면  
#         # -> i 안 먹
#             old_dp.append( [old_dp[i-1][0]+ money[i], old_dp[i-1]  ] )
        
#     # 초기값 인덱스 처리
    

#     return max(old_dp[-1] )

# 4) 집 수 3, ..
# 원소값 0,1,..
# 앞 두 개 
# - root 쓰던 거 while)nn

# - 1h 30m(75%)  x o o x 막판에 귀찮 & 타임오버로 조건 대충 디버깅만 하구 품(논리보다)
# - 귀찮다
# - 다른 사람 풀이 (+9점 https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
#   + 이전 특정 꺼 먹었는지 안먹었는지 여부 무관하게, max()에 포괄돼있다 
def solution(money):
    # - 원 순환 : 중복은 안되니까 [0 ~ 마지막 -1] , [1~마지막] 두 경우의 일차원 범위로 나눠서 품 

    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    for i in range(2, len(money)-1): # 첫 집  경우
        dp1[i] = max(dp1[i-1], money[i]+dp1[i-2]) # 후자에 o x x o도 포괄됨.  
        

    dp2 = [0] * len(money) # - 길이 길어서 메모리 낭비일줄 크게 상관없네 
    dp2[0] = 0 # - 첫 번째꺼 안먹음. for문을 끝까지 돌려서 마지막꺼 까지 감안하도록함. 
    dp2[1] = money[1]

    for i in range(2, len(money)): # 마지막 집 경우
        # 점화식.
        dp2[i] = max(dp2[i-1], money[i]+dp2[i-2])

    return max(max(dp1), max(dp2)) # 두 경우 중 최대
