# 1)2)는 문제 풀 때의 노트라 시간 절약하며 쓴 말 상태 꽤 보존.
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

# - m_bfs유형문제인거 알고 bfs  [bfs로 풀기 생각해보기?. 확실한 거랑 다르긴함] 
# - bfs시복 
# - 각 글자로 갔을 떄 글자 -1만큼의 for방향
# in words : 한개만 다른지  
# -> [m_new:  [begin에서 한개만 다른 것이 words에 있는지 (X_set에서) "bfs"(의미및 돌아가는거로 인해 시복가능한거 바로 알기.)로 미방문 찾아나가기](begin이 target이랑 더 멀어지게 돼도 words에 있는 걸 거치기 위해 돌아서 갈수도 있음~~ 걍 map에서 돌아서 도착하는거) 

# - > !중요!!!! 미방문만 갈거라 n!아님. ㅎㅋ 
# - > or 알파벳(_굳이 더 생각안했음)이나 한글자다른것들의 map지도화?(가능한 방법. 그방법도 시복 비슷함)_words연결리스트생성&bfs미니멈숫자_)_:n!? : 아님
#   + 중복 방문 안할거임 : 먼저 방문했을 때가 미니멈으로 닿은 순간이라 다시 도착한 더 큰 값 필요 없음 

from collections import deque
def solution(begin, target, words):
    # - bfs 시복 
    #   + 원래 기본형은 O(n) 맞는데, 이 문제 조건은 그 O(n)개가 다른 word들[O(*n)]과 연결된 애인지를 체크(=조건에 부합하는지)해야해서(연결맵없어서) [~~탐색했더니 미방문하게 됐던 애들이면 다른 출발애가 다시 걔들과[O(*n)] 조건 탐색(O(_*m))하게 돼서] O(n) 아님
    
    # - set으로 하면 in은 좋아져도 사용하려 한 [방문체크] 귀찮음. [미방문 됐던 애들만 add하는 set으로 이용]하는 방법도 있긴함_굳이
    ##set_words=set(words) 
    
    visited=[0]* len(words)
    #3) 모든 글자가 다 같으면 안 가고 1개 빼고 같으면(위치도.) 감 -> 집어 넣기
    new_words=deque( [ [begin, 0] ] )# - deque : 요소인 v가 단순 정수 아니고 길이가 2이상이라 or append아니고 정의하며 넣고 있으니까 요소(_[begin,0]) 겉에 [] 더 씌워야함 ## begin~~new_words
    # - while 방법이 코드 더 깔끔 : <-> m_x1미방문만 인 거 엄밀히 생각하기 전인 코드 방법=코드 상 반복문&new_words의 for문&탈출조건 설정((시복은 아마 비슷)) 
    
    while(new_words): # 1회씩
        go=new_words.popleft() # - O(n)_여기랑 while 부분 : go로 나올 애로 '미방문'했던 애들만 넣었기 때문임 ## while,pop이어도 튀어나오는 출발 애가 n개로 한정 돼있음. 시복 금방 알아야함  ##begin, t
        #   + max가 O(n)인 거고 애초에 조건 상 평생 방문할 일 없던 word는 포함 안됨
        
        ## 타겟 찾기
        #  new_words로부터 시작하여 미방문애들 중에 대상 찾아보
        # - a_O(n) * b_O(n) 에서 a b 출발 도착 헷갈리지 마삼. 아래 주석 처리한 건 m_x1 관련해서 작성하던 초본이긴 했음. 그래도 new_words의 초기값이 words일 때만 같은 거구 나중에 달라짐
        ## for i, word in enumerate(new_words) : 
        for i, word in enumerate(words): # O(n)  & 방문했던 애는 아래에서 바로 continue
            if visited[i]==True or word == go[0] : # O(m) 
                continue
            # 1개 빼고 같은거 check
            # check=[0]*len(word) # 숏코딩으로 하면 시복 차이는? : 걍 빨리 탈출할 수도 있는 조건으로 길게 커스터마이즈함
            check=True # 움직여서 건너갈 대상인지
            warn=False # 위의 내용을 위한 1,2회관련 체크
             # - 시복 알고도 다시 또 어라 하기도 하네. !가 아니고 n은 두번만 곱해짐. 경로 마냥 연속해서 가서 단 두 발자국 아닌 느낌 나긴 하는데, 그 경로를 미방문만 가면서 데이터 저장해서 넘겨주기에 n(:첫발지칭)*n(두발)으로 감. 직렬의 병렬화 느낌 조금 난다랄까. ( 해당경로로 dfs로 간다기보다 bfs로 해당 애를 추가해줌(두번째 발자국 후에 바로 가지 않고 첫번째 발자국에 넘겨줌 ) 그 애가 나중에 첫 발자국으로서 앞 O(n)에 포함됨)
            for j in range(len(word)) : #O(m) # 조건으로 시복 단순화 귀찮_어느정도 해버림. 
                # - [코딩 시간을 아끼자] 이러한 for 문내에 금방 탈출은 큰 의미 없음
                if word[j] != go[0][j]: 
                    if warn ==True: # 대상 아님
                        check=False
                    warn=True
                    
            if check==False : # 다음 워드 검사로 넘어가기  
                continue
            # 대상인 word임 : 게임끗
            if word == target :
                return go[1]+1
                
            new_words.append( [word, go[1]+1  ] ) # - bfs로 최소값 구할 때 : 부모에서 +1 하기 위해 디큐의 마지막 요소에 거리 넣어줌
            visited[i]=True
    # 아직도 return 못했으면 못 찾은 거임
    return 0
# 4)
# 단어의 길이 3~10. 
# words길이 3~50 : 큐라 알고리즘 상 차이가 없긴함 그래두
# -> 3 :  ["hot","dot","dog"]
# 불가 0 


# - 1h(+1점) (+2m은 코딩 공부용필기한 거에 쓰였다 치고 확인 더 함)
#   > 코테 시간 : 슬슬 문제 당 40m 컷으로 두고 연습하자
#   + 시복 빠르게 계산 못해서 시간 꽤 걸린듯. 출발~도착 리스트(조건 검색을 위하여.) 헷갈리지 말기. 둘다 words에서 시작해서 이름 헷갈릴 수 있으니 start~arrive도 좋을듯


# - 5) 중간 출력 확인 : 시간 남으면 하기.

# - visited : 굳이 [연결리스트] 만드는 방법 안 써도 [visited이용하면서 for in 에서 탐색]하면 시복 잘 줄여짐. 연결여부 조건으로 찾기를 for문 안에서 탐색해나가는 거로 대체 

# - 다른 사람 풀이(0.85ms)_내께 더 빠름(최대 약 0.47ms) 근데 난 코딩 시간을 줄여야함 (( 굳이 연결관계 체크 안 해도 되는 word들끼리 안하게 돼서 맵 미리 만든 것보다 시간복잡도 더 나을듯 ))

#   > 신성한 , malza321 , 김다함 , 한충신 외 11 명
#   + 제너레이터 : 이터레이터를 생성해주는 함수, yield 사용 [https://dojang.io/mod/page/view.php?id=2412]
#     + ~~ 함수 다 돌렸을 때 yield 됐던 순서대로 for in 에서 나옴
# def number_generator():
#     for a in range(2):
#         yield a
# for i in number_generator():
#     print(i) # 0  1 출력
'''
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            # - 미방문 체크 : in 거리 담은 딕셔너리에서 함_평균 O(1)
            if next_word not in dist: 
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)
'''
'''
3.3 in의 시간복잡도 [초기에 적었던 거라 쓰는 방식이 달랐어서 출처를 모르겠네 코딜리티인지 챗쥐피티인지]

Container TypeTime ComplexityReference
List	O(n)	Pythn Documentation
Tuple	O(n)	Python Documentation
Set	    O(1) (average) / O(n) (worst case)	Python Documentation
Dictionary O(1) (average) / O(n) (worst case)	Python Documentation
'''
'''
- tuple [튜플]
: 다양한 자료형으로 입력 가능
: 인덱스 접근 가능
: 불변 타입 자료형 [  '요소'의 추가, 삭제, 수정이 불가 ] 
'''

# - m_bfs유형문제인거 알고 bfs로 품 
#   + -> [bfs로 풀기 생각해보기. 확실한 거랑 다르긴함] 
#   + 풀수 있는지 생각할 수 있는 법
#     + (1) 방문, 전체 탐색해봄 (2)중복방문 안해도됨  
#     + (3) 연결, 맵 비슷 (4) 최소, 출발, 도착
#     + (5) !되버리려나   (etc) 문제 풀어가다가 익숙 습득 

# - [시복 계산]!중요!!!! 미방문만 갈거라 n!아님
#   + 문제 케이스보면서 뇌로 논리 돌리기보다, 코드 짰으면 코드에서 계산하는 게 빠름. 짜기 전에 계산해야 하긴함. 그럼, O(출발_bfs_n[실행 순서는 while & bfs로 중간중간 이어도 n개임!! ]*n나머지 *m )
#     > 나머지 때, 모든 n에서 미방문 체크하는 것보다 사전에 미방문인거 append해 놓고 거기에서 도는 방법도 있겠지만 시복(_worst) 똑같을 때 굳이 그 정도 최적화할 필욘 없을 듯. 이걸로 맞는 거 여부가 달라질 일이 적을 거 같음
#   + 추가 : worst case도 큰 껍질에서 n + n-1 + n-2 + ..((~~O(n*n_) )) 관련이지 n! 아님 . n! 이려면 *인 거라 [맵 머리에 그려보면, 조건 등에 의해 네 위치만 갈 수 있는 거랑, 아무 곳이나 갈 수 있는 거 경우의 수 차이 어마어마함. [경로라 * 느낌 날 수 있지만 bfs&큐로 저장]을 통해 전체 경로 경우를(탐색을) *아니게 함 ](( * 인 거는 모든 word들로 이동도 가능한 상황임)) ((=*이려면 모든 걸로 건너갈 수 있을 때 또 다시 했던 거 빼고 모든 걸로 넘어갈 수 있어야함))

#   + m_연결((한글자다른것들의)) map지도화(시복 유사&내방법이 좀더 빠름) : words두개로 연결리스트생성  -> bfs 미니멈: 생성_n! 아니고 n^2임.

# - dfs : 요새 bfs(def포함 10)만 써버려서
#   + def포함 6 : 
'''
def dfs(v): # [0,1]
    visited[v]=True
    print(v) # dfs : 꼭 먹을 때 출력 | dfs라 깊게 갈 때, 다 쓰고 출력하면 늦고 처음 닿을 때 먼저 출력
    
    for nv in graph[v]:
        if not visited[nv]:
            dfs(nv)
    
'''
# > 듀얼 모니터
#   > 코테 공부할 때는 시험 볼 때 쓸 노트북으로만 하장