# 합의 최대값

# 2) 각 층 (해당 위치에서의 최대값_아래에서부터 두개 중 최대값

# 500 이하면 시간복잡도 충분하니까 .  max 긴층에서 안돌릴려면, 아래에서부터 가자
# 2) 연속 두 개 중 최대값 그 위층이랑 더하기 ( 개수 같음 )

def solution(triangle):
    recent_layer=[]
    recent_layer.append(  triangle[-1]   )
    # recent_layer=[ triangle[-1] ] # 아무리 append한다고 해도. 이건 재정의잖아 ㅜ append로 왜안했었누
    # 그리고 append할 거면 아래 for문 아래에서 하면 안됐지
    for i in range(len(triangle) -1) :# -1빼먹 # 층 # 아래부터 두 층씩 연산해서 -1
        #~
        # if i == len(triangle)-1:
        #     break
        # low_layer=[]
        
        
        calculated_layer=[]
        ##print(triangle[-(i+1 +1)] )#recent_layer)
        
        for j in range(len(triangle[- (i+1) ])-1): # 여기가 layer라 위층부터 됐었# 두 값씩 연산해서 -1. layer_5->4,4->3 
            # "초기값대신 마지막 처리 "두개 짜리 더할 일 없을 땐 for문 안돔
            ## print(i,j) #~1 0   2 0 2 1 아하, 위층부터돌구나
            # > 1 0 ~ 3 1, 마지막 층 여긴 안옴. 왜 i가 0이 아니라 1부터지 _ for j 수정할때 좀 확실히 하구 수정하자 대충 돌리지말구
            # low_layer.append( max(layer[j],layer[j+1]) ) # 다음 층에서 이용할 값
            # if i ==0: # 초기값 1층화로 대신 처리
            #     max_value=max(layer[j],layer[j+1])
            # else :
            #max_value=max(low_layer[j],low_layer[j+1])
            max_values=max(recent_layer[-1][j],recent_layer[-1][j+1]) # 그냥 1차원 리스트로 개수로 인덱스 계산해서 거슬러갈수있겠지만 인덱스 수식 귀찮
            ##print('recent', recent_layer) # 이 for문 아래에선 맞게 나오는데 여기서는 똑같은거만나왔었
            ## print('--',  recent_layer[-1][j] )
            calculated_layer.append(triangle[-(i+1 +1)][j]+max_values)# 현재 레이어까지의 최대값_ 차근 차근 위로 저장해나감
            # 첫줄처리(층도 emunerate로 인덱스사용해서 바로 첫 회전부터 1층 2층 함께 계산함), 마지막처리### 아랫층처리인 max_value는 layer가 아니라 이전에 더해온 애랑 더해야지 
        # if i ==len(triangle) -1:
        #     max(recent_layer[-1][0],recent_layer[-1][1])
        #     recent_layer.append( triangle[0][0]+max_values  ) # -(i+1 +1)
        # else :
        
        recent_layer.append( calculated_layer )
        
        # 인덱스 쓰니까 디버깅 더럽네 한 레이어씩 가져와서 출력해서 보던 해야지.. 
        
        ##print(calculated_layer)
    return recent_layer[-1][-1]

#  4) 큰 알고리즘 맞춘 후 = [마지막층 자동 계산 됨]# 