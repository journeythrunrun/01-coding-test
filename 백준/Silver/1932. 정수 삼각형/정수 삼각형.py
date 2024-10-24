# 1)
# 합이 최대가 되는 경로



# 2) 층 입력 받으며 . 층층이 저장해나가. 각경로. 
# a 
# b c : 



#~ 비슷한거 풀때 난 아래층에서부터(큰거 선택하여 경우의 수 줄임). 다른사람은?
# - 아래층에서부터 c1 c2 중 큰 거 위로 c2 c3중에 큰 거 위로
# 3) n=500 -> O(n^3)
# for i in range( len(layers)-1 ) : for j in range( len(layers[-i-1])-1 ):
# ## 7이면 그냥 더해주기 
# layers[-i-2][j]+=max(layers[-i-1][j], layers[-i-1][j+1]) # - 뒤층 -(i+1) #layers[i][j]+=max(after_layer[j], after_layer[j+1])
#~ 둘다 길이. 2층부터
# (3) 누적되기 위해서 layer값으로하기.
# inpu
n= int(input() )
layers=[ list( map(int, input().split()) ) for _ in range(n) ]
for i in range( len(layers)-1 ) : 
    for j in range( len(layers[-i-1])-1 ):
        ## 7이면 그냥 더해주기 
        layers[-i-2][j]+=max(layers[-i-1][j], layers[-i-1][j+1]) # - 뒤층 -(i+1) #layers[i][j]+=max(after_layer[j], after_layer[j+1])

print(layers[0][0], end='')
# 4) 층길이 1,... : 1 , 7 
# 2
# 7
# 3 8
# 값 0, : 





