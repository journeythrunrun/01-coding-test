# 1)
# 상근이네서 출발. 맥주 한박스 20개 시작. 50미터에 한병씩 마심. (49?)
# 편의점 :
# 최대 20개

# 편의점 가면 맥주20개화. 스테미나 무조건 맥스.  #$

# 2)값맵해버리면60,000*60,000 _ 근데 주변탐색용변수말고  visited맵은 생성쪽이라 그래도 상관없나봄. 그때 최대값이?  /  O(t_50*  (n_100개+66*66맵?   ) )
# 20개*50미터=1,000당(까지갈수있음)  amap화. //1000
# 사방 1000씩  인덱스
# x 쳐져있던 거 실화


# n을 갈수있나 사방 완전탐색

from collections import deque
import sys
input=sys.stdin.readline

t= int(input()) 
# - 예시를 통해서 딱 1천까지 ㄱㄴ한거 확보

# - 내가 쓴 방법이 1000압축화 노드에는 자기 자신말고 다른애들도 있어서 8방말고 9방으로 자신 노드도 확인해야함 ##이렇게 중복으로 노드에 압축시켜놓을거면말야
dr, dc=[-1,-1,-1,0,0,0,1,1,1],[-1,0,1,-1,0,1,-1,0,1]# - dr . 점 실화냐 # 근데 이건 힌트 안주는 거로 연습하려고 일부러 안좋은 에디터써서 확대 몰라서 그런 거일 수 있음 원랜 코테에서 글자 작게만 봐야하는 경우는 없즤

answer=""
for _ in range( t) :
    n= int(input()) # - ! 각 테스트케이스마다 주는거다.. 예시의 한줄한줄살피기..
    temp_answer="sad"
    
    i_r, i_c = map(int, input().split() ) 
    i_r+=32768 # - 음수 귀찮으니 땡김. 
    i_c+=32768
    visited= [[0]*66 for _ in range(66)] # 0을 저 위치[ ]안에서 반점으로 복제하는 거지
    
    # 값이 좌표 정보니까 amap의 인덱스 정보로 치환
    amap= [[ []for _ in range(66) ]for _ in range(66)] # 최대값 65~. （32,767＊２）[65]까지여야하므로.  # 계단처럼 앞쪽  숫자 기준으로 내릴거임 
    # - !  [[ ]for _ in range(66) for _ in range(66)이건  4356행0열이 돼버리네]
    #   + ! 0과 달리 공백이라 concat할 요소가 없지.　빈리스트를　복사하려　했었으니　애초에　공백은　아님
    #   +  [[]]*66하면 concat는 되는데 리스트를 복사해버려서 주소 복사돼버림
    
    #　－　[[[], 이상해보여도　이게　맞음．　열이　길이가　있고　그　각　행，열에　요소로　빈리스트가　있는　것임．#　－ [[],［］이건　열의　길이가　０인거임
    
    for i in range(n) :
        r,c = map(int, input().split() )
        r+=32768
        c+=32768
        amap[r//1000][c//1000].append([r,c])
        # 여러개 저장할 거니까 빈 리스트로 초기화하고 좌표 append    # 900 이면 0에. 1900이면 1에 
        #＃ 가까운 놈부터 가는 그런거 말고 그냥　매번 완전탐색?은　경우의　수　오바임　ｎ＊＊ｎ이니
        #＃ 해당 몫의 값들 저장? 
        #＃middle = [list(map(int, input().split() ) ) for _ in range(n) ]

    
    f_r, f_c = map(int, input().split() ) 
    f_r+=32768
    f_c+=32768 # - 디버깅으로　주석처리　할　때　ｉｎｐｕｔ（）이　주석되지　않게　주의． 앞뒤에 길게 섞여　있을　수　있음．　
    amap[f_r//1000][f_c//1000].append([f_r,f_c])
    
    q=deque([ [i_r//1000, i_c//1000, i_r, i_c] ]) # 인덱스，　, 그 번대의 실제 좌표，
    #　－visited[i_r//1000][i_c//1000]=1 ＃　－　필요　없음．아래　ｉｆ문에서　설명．　# - ！리스트 인덱스　：　 [][] 각각임!! 사이에　반점 안됨!!!!
    pass_set={(i_r, i_c)}

    # 같은　ｒ，ｃ에서　　봤던　ｎｒ，　ｎｃ도　다른　실제값에서　본　거면　다름．
    v=i_r//1000,  i_c//1000, i_r, i_c
    # i와 같은 노드에 있는 형제들.　
    for candi in amap[v[0]][v[1]]:# 　－ 복붙시 모든 글자  요소 다 체크.  # amap에 i는 없음　：　어차피　ｑ에　ａｐｐｅｎｄ하려고　하는　건데　이미　했음．
        if abs(v[2]-candi[0])+abs(v[3]-candi[1]) <=1000 : #　－  서로끼리 건너갈 수도 있음（다른　부모에서는　접근　불가능하지만　형제들끼리　발판삼아　더　확장할　수도　있음）　－＞　ｄｒ，ｄｃ에　자기자신도　추가．　＃　－　　그냥 첫 노드를 미방문으로 하고 시작하는　거는　첫노드에서만인　건　둘빼치고（자기　자신끼리에서　안하고　다른　노드　갔다오면　못돌아오는　케이스도　가능．같은노드　첫놈－＞같은노드　다른놈이　아니라　다른　놈들끼리도＜－＞여야함．）　미방문　기준은　노드가　아니라　실좌표값이어야함－＞ｐａｓｓ＿ｓｅｔ．　ｎｏｄｅ당　많은　개수가　가능하기에　그　ｖｉｓｉｔｅｄ는　필요없음．
            pass_set.add( (candi[0],candi[1]) )
            q.append( [v[0],v[1], candi[0],candi[1] ]  )
    # ａｍａｐ에　ｍｉｄｄｌｅ과　ｆ　다　넣어두고，　ｉ를　시작으로　갈　수　있는　ａｍａｐ의　실제좌표값을　ｑ에　다　넣음．　그　ｑ에　ｆ도　있으면　ｈａｐｐｙ
    #　－ amap에 i 랑 f가 왜 안들어가있지　： 32768로 더하면 천의자리 뒤에도 달리질　수　있어서 다른　노드화　될　수　있음．　 그럼 8방법이 쫌 꼬일 수 있는 건가. 그래도 평행이동인디　：　평행이동이라　이동　가능한　거면　각　ｘ，ｙ에　대하여　두　점이　최대　１개의　경계선（노드값　한쪽＋１）이　있을　수　있음
    #　　＞　 근데 1다른것도 아니고 3이다르다니 연산이 문제가. i는 32, 33d으로 맞는데 f가 이상하네　： f 미들 후에 받기에　그건　미들이었음ㅋ
    while(q):
        v=q.popleft()
        # 사방 검사. 갈 수 있니?
        # 디버깅_방문을 이렇게 많이 할 필요 없는데. 
        if (v[2],v[3])==(f_r, f_c) : # - 정확히 같은 거 아니고 이내이면 되는지？　알고리즘　상　정확히　같은　거　맞음．　거리가　이내이면　ｑ에　넣어줬기　때문임．
            # －　코드　수정전＿f도 i와 같은 노드에 있으면 에러가　나지.　＃＃　후보군인 amap의 가장 안쪽 요소에 f가 q안에 들어왔었는지 보는 코드인데. 처음에 i할때 동일한 노드의 i와 middle만 큐에 넣어주면 그 노드는 더이상 방문도 못함 ：근데 amap에 i랑 middle말구  노드에 f넣어놨는데..
            temp_answer="happy"
            break
          
        for i in range(9):
            nr,nc=v[0]+dr[i],v[1]+dc[i]
            
            if 0<=nr<=65 and 0<=nc<=65 :#　－　and visited[nr][nc]==0 : #＃　ｎｒ　 얘넨 찐값이 아니라 //임.다른 놈으로부터 끝에서 시작하면 걔는 가게될 수도 있음.
                # 얘넨　기본　ｂｆｓ에서　 추가로 (1) ＇편의점＇이  방문가능한 자식이 되려면  (2) 부모 좌표로 부터 ＇1000이하＇여야하는 조건도 있음
                # 그 위치에 있는 값들
                for candi in amap[nr][nc]:# －　리스트에 요소　없는데 pop하면 에러 뜸　－＞ for | get은 딕셔너리
                    if abs(v[2]-candi[0])+abs(v[3]-candi[1]) <=1000 and (candi[0],candi[1]) not in pass_set: #$
                        pass_set.add( (candi[0],candi[1]) ) 
                        q.append( [nr,nc, candi[0],candi[1] ]  )
    
    # - 디버깅_입력을 '한줄 씩' 넣어보니까 알겠네 : 입력을 반복문에서 받고 있고 각 회전마다 정답이 1개씩 있더라도, 최종 정답 출력은 for문 밖에서 여러 정답 모은걸 마지막에 한번에 다 출력.
    answer+=temp_answer
    answer+='\n'
print(answer, end='')

# 4)
# t=0_에러는 뜨지 말아 / n=0,1,2_
# x,y 음수, 0, 같음, _중복_이미 방문해서 또 방문 안함 
# nr&nc는 같아도 실제값은 다른 놈 들어오면 그 새로운 놈은 미방문된 상황이라 그 실제값좌표로 미방문 체크해야함. 
# - 해당 nr nc에서 그 좌표들 for로 다 돌아서 괜찮을까? 관계성이 서로 전부<->가 안돼버리는 상황임. : 그 nr nc의 모든 좌표를 한 부모와의 거리만 비교하는 코드긴함. 그렇지만 관계성이라 순서는 없기에, 한 노드에서 모든 가능한 곳으로 출발하게만 하면됨. 그래서 실제값에 대해선 미방문처리 이용하여 코딩해도 괜찮음  ->암튼 실제값 필요 => q의 요소에 3,4번째에 실제값 추가함. 아무튼 모든 이동가능한 노드에서 갈 수 있는 곳을 다 검사하면 그노드는 전부체크한거임.(자신에게 도착하는 거 안따져도 됨. 두점에 대하여 거리는 어디서 출발하나 같음)
# 자기 자신쪽에 있는 건 안보나. 처음에 자신의 노드넣을 때 자신의 여러가진 안 넣어줌.  
# - 4방이 맞나?  8방의 끝쪽들은 두 좌표 다 1000 이상인 거라 아님 ? : 근데 끝값에서 조금씩만 커서 넘어갔을 수 있음!!! 평행이동시도 그렇고 둘 사이의 한 축에 대한 경계선은 최대1개 있음



# - 정답인 핵심 알고리즘 짜는 건 30~50m? 별로 안 걸린 것 같은데 세부 알고리즘, 디버깅 ++이 3h 넘게 걸린듯(시간초과라답도 봄)

# - 2)실제값을 인덱스로 가지는 맵 만들면 60,000*60,000 _ 근데 완전탐색으로 이동할 대상인 맵변수 말고 visited맵에서 인덱스로 접근해서 체크할 거면 생성쪽이라 시복크게 차이 없을 수도.(근데 너무 커서 이정도면 차이있다.) 어차피 난 set으로 하긴했음 뭐가 더 빠를진 변인통제 실험은 아직 안해봄
#   + a=list(range(10000000)) : [백만]_성공_대충 python_40MB,60ms | pypy_8MB,4ms. 천만_[pypy3]는성공
#   + 시복 :  O(t_50* (n_100개+66*66맵?이라기엔 실제값 n개 방문하며 bfs로 완전탐색하긴하는데 맵의 dr dc이용함. drdc이용해도 q에 넣는 건 최대로 실제값 n개임   ) )
#     + 시복_곱하기 : O ( t_50*  (n_100+ qpop_n_100*for_9방_9*for_노드맵_이건상황마다다르고qpop과좀 섞여있을터인데a)   ) : popleft로 시작되는 애가 n개고. 그 n개에서 다른 놈들로 검사는 *k임. 산발해서 세지 말고, popleft된 한놈 기준으로 땡겨서 세면 편함
#       + a : 가장 첫번째로 for돌 때 worst이면 바로 옆 노드에 다 있는 건데 그러면 다 pass_set에 추가되긴함.(worst 예시생각해야 그나마 따지는 거에 진전이 잘 생김) 그리고 한노드에 몰려있으면 다른 노드엔 없는 거라 무조건 곱하기 연결(모든9와모든v에대하여 a번이어야함)은 아님. 시복내인 거 계산하기 편하려면 n개라 쳐도 시복내라 깊게 생각 안해도 됐음.
#     + 맞춘사람 마지막페이지 최대시간 보니까 5000ms(python)정도임 내께 80ms정도니까 개충분 맞음

# - IDLE 근데 쫌 쓰기 위험하긴하네. 주석 형식과 글자랑 들여쓰기 위치 정도 깨지기도 함
# - 이건 pypy보다 python이 빠르네
# - input=sys.stdin.readline ( 144ms->76ms화됨. input이미 있는 놈인데 input이름으로 먹일 수 있네. 물론 실행마다의 오차도 존재는 함.)

# - 다른 사람 코드 [melon940925]
#   + 개짧네 쩌네. 뭔가 아이디어 머리 굴려서 돌아서 풀기보다 bfs 이용해서 바로 효율적으로 엄청 잘 풀은느낌 나네.
#   + 나도 풀 때, 경로에 구별된 의미 없고 방문했는지만 의미가 있어서[옛날 확통 마냥 따지기] bfs한 노드에서 n개 검사해도 미방문만 보면 시복 적은 걸 확실히 바로 잘 알았어야함.
'''
import sys

sys.setrecursionlimit(10 ** 5)
si = sys.stdin.readline

t = int(si())


def solution():
    n = int(si())
    start = list(map(int, si().split()))
    stores = [list(map(int, si().split() + [False])) for _ in range(n)] # - 값 입력 받을 때, 한 좌표마당 False도 붙여 놓음
    end = list(map(int, si().split()))

    def dfs(cur_x, cur_y): 
        if abs(cur_x - end[0]) + abs(cur_y - end[1]) <= 1000: # - 현재 점에서 마지막 점 갈 수 있는지
            return True
        ret = False
        for i in stores: # - 모든 좌표 검사네 
            if i[2]: continue # - 실제 좌표값에 대하여 방문한 놈들 패스 # - n개 다 검사하면 n**n이라 생각했는데, 문제 특성상 n**n아니고 미방문한 애들만 가는거네! 방문했으면 경로 무관하다는건 : n에서 n개 검사해도 미방문 애들만이라 시복 괜찮다는 거 # - n+...+1?
            if abs(cur_x - i[0]) + abs(cur_y - i[1]) <= 1000:
                i[2] = True
                ret = ret or dfs(i[0], i[1])
        return ret

    print('happy' if dfs(start[0], start[1]) is True else 'sad')

for _ in range(t): solution() 
'''
