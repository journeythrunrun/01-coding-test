# 1)합의 최대값

# 2) 각 층 (해당 위치에서의 최대값_아래에서부터 두개 중 최대값

# 500 이하면 시간복잡도 충분하니까 .  max 긴층에서 안돌릴려면, 아래에서부터 가자
# 2) 연속 두 개 중 최대값 그 위층이랑 더하기 ( 개수 같음 )

def solution(triangle):
    recent_layer=[ triangle[-1] ] # - 아무리 나중에 이 변수를 append & -1인덱스로 사용한다고 해도, 재정의든 append든 중복되면 안되니까, 아래의 for문 아래가 아니라 여기서 했어야지. 급하게 하기보다, 완벽한 위치인지 따지고 조심하면서 초기값 설정
    for i in range(len(triangle) -1) :# ! 재수정할 때 -1빼먹. break문으로 대신 하려고 했던 거 수정하다가 어차피 오류나서 다른 거 먼저 수정함. 아직 미처리한 거 뭔지 아래에 적어두기!!!! # - 아래부터 두 층씩(두번째 층 위치에서) 연산해서 -1   ##층 
        # if i == len(triangle)-1:
        #     break
        # low_layer=[]
        calculated_layer=[]
        ##print(triangle[-(i+1 +1)] )#recent_layer)
        
        for j in range(len(triangle[- (i+1) ])-1): # ! 여기를 layer로 했어서 위층부터 돼버렸었음 # - 두 값씩 연산해서 -1. ##layer_5->4,4->3
            ##print(i,j) #~1 0   2 0 2 1 아하, 위층부터돌구나##1 0 ~ 3 1
            # - i,j에서 i가 0말고 1부터 출력됨.-> 위층 부터 돌아버려서 & 인덱스 복잡 
            ##for j 수정할때 좀 확실히 하구 수정하자 대충 돌리지말구
            
            # - 다음 층에서 사용할 old값은 이전 층에서의 '최종값'임. 이전 층에서의 초반값아님. ## low_layer.append( max(layer[j],layer[j+1]) ) # 다음 층에서 이용할 값
            
            # if i ==0: # 초기값 1층화로 대신 처리
            #     max_value=max(layer[j],layer[j+1])
            # else :
            #max_value=max(low_layer[j],low_layer[j+1])
            max_values=max(recent_layer[-1][j],recent_layer[-1][j+1]) ##그냥 1차원 리스트로 개수로 인덱스 계산해서 거슬러갈수있겠지만 인덱스 수식 귀찮. 
            
            ##print('recent', recent_layer) # 이 for문 아래에선 맞게 나오는데 여기서는 똑같은거만나왔었음
            ## print('--',  recent_layer[-1][j] )
            calculated_layer.append(triangle[-(i+1 +1)][j]+max_values)# 현재 레이어까지의 최대값_ 차근 차근 위로 저장해나감
            # 첫줄처리(층도 emunerate로 인덱스사용해서 바로 첫 회전부터 1층 2층 함께 계산함), 마지막처리### 아랫층처리인 max_value는 layer가 아니라 이전에 더해온 애랑 더해야지 
        # if i ==len(triangle) -1:
        #     max(recent_layer[-1][0],recent_layer[-1][1])
        #     recent_layer.append( triangle[0][0]+max_values  ) # -(i+1 +1)
        # else :
        recent_layer.append( calculated_layer )
                
        ##print(calculated_layer)
    return recent_layer[-1][-1]

#  4) 큰 알고리즘 맞춘 후 = [마지막층 자동 계산 됨]# 


# - 1h 17m (+1점) : 알고리즘은 초반 20m 쯤에 했던 거랑 똑같은데, 인덱스 오류 디버깅 개오래걸림.
# - 인덱스
#   + 인덱스 가볍게 가져가기 & 덩어리 가져오기 : 메모리 효율이고 뭐고, 시간복잡도 이내이면, 그냥 해당 층 특정 변수이름으로 가져와서(디버깅 편함) 사용하자
#     + 게다가 인덱스는 앞뒤 끝 처리나 연산에서 실수하기도 쉬움


# - 디버깅
#   + 똑같은 변수도 여기저기에서 출력해보기. 틀렸다는 건 '잘못 생각하고 있는 게'있다는 거니까 맞는 것 같은 곳도 확인해봐야함.
#   + 인덱스 에러 나면 기본적인 것도 출력. 어디서 꼬였을지 모름
#   + 특히 인덱스 _ for문에서 사용하는 특정 변수 '덩어리 출력' (recent_layer[-1], recent_layer[-1][j])

# - 해설 비슷해보임