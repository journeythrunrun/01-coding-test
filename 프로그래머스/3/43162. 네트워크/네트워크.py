# 1) 컴0~n-1  => 네트워크의 개수
# 2) 이어서 붙이기 -> set에? 없으면 추가

# n 200이하 -> n^3



def solution(n, computers):
    # a={1,2,3}
    # b={3,4}
    # print(a.union(b))#~ set
    network_index=[False]*n
    sets_list=[set([0])]# [..] int not iterable # 0이어야하는데 1로했었네 첫번째껄
    # network_index[0]=0
    # 4) 연결된 거 하나도 없으면 n개, 반복 시 초기값 첫번 째, n=1
    for i in range(len(computers) ) : # 얘네 for 2개로 따로 1인놈들 저장해서 시복줄이는것도
        for j in range( i+1, len(computers) ) :
            next_turn=False # 아무것도 없으면 expected an indented block 뜸
            
            if computers[i][j]==1 : # 1만 & 작은 것만
                find=[-1,-1] # sets_list에서 몇번쨰 인덱스에 해당하는 네트워크인지
                for k in range( len(sets_list) ):
                    if (i in sets_list[k]) : 
                        find[0]=k
                    if (j in sets_list[k]) : 
                        find[1]=k
                # print(find)
                if find[0]!=-1 and find[1]!=-1 and find[0]!=find[1] : # 달라야? 이미 같은 네트워크일 수 있음
                    # print(1)
                    sets_list[ find[0] ]=sets_list[ find[0] ].union( sets_list[find[1]] ) #~  set # ! 다시 저장까지 해야함

                    # print(sets_list)
                    sets_list.pop( find[1] ) # 제거 시복도 n이긴해도 여기서의 n은 sets_list길이라 짧을
                    # print(sets_list)
                    
                #~ 0이랑 False랑 똑같이 취급돼서 문제생김. 컴 0<->1 바꾸던 것도 
                elif find[0]==-1 and find[1]==-1 : # ! 인덱스 내부 둘 다 [0] x
                    sets_list.append( set([i,j]) )
                    # print(2)
                else :  # '한쪽'만 있는 경우->나머지 까지 연결되게 둘다 넣기. 이미 있는 놈 포함하여 둘 다 거기에 넣어도 됨(set이라 중복 알아서처리)
                    # print(3)
                    # if find[0]!=-1:
                    # find가 -1인 곳말고 값있는 놈 위치에.
                    target=max(find)
                    sets_list[target].add(i)
                    # if find[1]!=-1 :
                    sets_list[target].add(j)
                    
            # print(i,j,sets_list)
                        
                        
                    # if (i in sets_list[k]) or (j in sets_list[k]) :
                        
                        # 5) i 랑 j가 서로 다른 네트워크에 있으면 : (검사는 : 이미 둘다 네트워크 있을 때의 케이스임)
                        # -> 몇 번째 네트워크인지 저장해둔 후 , 나머지도 같은번호화 -> 그 변수이용해서 결과. 다른 숫자의 네트워크_ max() 
                        # 5_m2)set합체는 sets_list 다 검사해야. 근데 어차피 검사. set_list[k]에서 몇번째 저장돼있는지 저장하고, 그 위치의 sets 붙이기 .
                        
                        # if (network_index[i] !=False) and (network_index[j] !=False) :
                        #     for 
#                                 if v == network_index[j] :
#                                     network_index[]= v
#                         network_index[i]=k
                        
                        
                        # sets_list[k].add(i)
                        # sets_list[k].add(j)
                        # next_turn=True
                        # print(sets_list)
                        # break
                # if next_turn==True: # 여기 아래에 뭘 했었나. 당연히 continue인데
                #     continue#break
            
    
    # n-주의
    connected_computers = 0
    for aset in sets_list : 
        connected_computers+=len(aset)
    answer = n  if (len(sets_list)==1 and len(sets_list[0])==1) else  (n-connected_computers)+len(sets_list) 
    return answer
# 4) 나중에 큰 네트워크끼리 연결됐으면 ? 


