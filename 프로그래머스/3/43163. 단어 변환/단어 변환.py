# 1)
# - 한 번에 한 개의 알파벳, words에 있는 걸로만 바꿀 수 있음
# -> 최소 몇 단계 필요한지 \ 불가_0
# - 알파벳 : '소문자', 단어 길이 같음,
# - words : 중복단어 없음 | begin target 다름 

# 2) 50 : O(n^4)
# m1_ 알파벳 한개 씩 다른 것들? 
# m2_O(n^4)니까 전체 훑기법 :팩토리얼은 안됨
# _ 한개 다른거씩 연속해서 찾아서 ->  열글자라 n^4로 안될 수 있음
# - 최소 횟수 : 



#~ m_bfs유형문제인거 알고 bfs : [bfs로 풀기 생각해보기?. 확실한 거랑 다르긴함] : 풀수 잇는지 생각할 수 있는 법 ? !~ 

#~ - bfs시복
# - 각 글자로 갔을 떄 글자 -1만큼의 for방향
# in words : 한개만 다른지 -> 아. 
# [m_new:  [begin에서 한개만 다른 것이 words에 있는지 (X_set에서) "bfs"(의미및 돌아가는거로 인해 시복가능한거 바로 알기. 미니멈값위해서도?효율? bfs)로 미방문 찾아나가기](target이랑 멀어져도 words에 있는 걸이용하려고 돌아서 갈수 있음) !중요!!!! 미방문만 갈거라 n!아님. ㅎㅋ
# -> or 알파벳이나 한글자다른것들의 map지도화?_words연결리스트생성&bfs미니멈숫자_)_:n!?  
#   + 중복 방문 안할거임 : 이미 방문했을 때가 미니멈이라 다시 올필요 x 
from collections import deque
def solution(begin, target, words):
    # set_words=set(words) # set으로 하면 방문체크 귀찮
    visited=[0]* len(words)
    # 3) 다 같으면 안 가고 두개가 위치도 같으면 감 -> 집어 넣기
    new_words=deque( [ [begin, 0] ] )# append아니고 처음 정의니까  [ [# begin~~ new_words
    
    # print(new_words)
    # for문 & 반복문 보다 while이 깔끔할듯
    while(new_words): # 1회씩
        
        go=new_words.popleft() # begin, t
        # 타겟 찾기
        
        #  new_words로부터 시작하여 미방문애들 중에 대상 찾아보
        #~ for i, word in enumerate(new_words) :#~ 시행 순간 new_words
        for i, word in enumerate(words):
            if visited[i]==True or word == go[0] :
                continue
            # 1개 빼고 같은거 check
            # check=[0]*len(word) # 숏코딩으로 하면 시복 차이는?
            check=True # 움직여서 건너갈 대상인지
            warn=False # 위의 내용을 위한 체크
            for j in range(len(word)) :# 조건으로 시복 단순화 귀찮
                if word[j] != go[0][j]: 
                    if warn ==True: # 대상 아님
                        check=False
                    warn=True
                    
            if check==False : # 다음 워드 검사로 넘어가기  
                continue
            # 대상인 word임 : 게임끗
            if word == target :
                return go[1]+1
                
            new_words.append( [word, go[1]+1  ] ) #~요소 인덱스처리
            visited[i]=True
        
        
    # return 못했으면 못찾은 거임
    return 0
# 4)
# 단어의 길이 3~10. 
# words길이 3~50 : 큐라 알고리즘 상 차이가 없긴함 그래두
# -> 3 :  ["hot","dot","dog"]

# 불가 0 
# - 중간 출력 확인? 시간 안남았을땐 굳이


# 뒤에 모니터석으로 가보장
# ! ,^

# 코테 시간 : 문제 당 40m 컷
# 요새 bfs만 쓰는듯 dfs