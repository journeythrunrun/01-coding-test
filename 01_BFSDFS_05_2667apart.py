# - 문제집_DFS+BFS 필수 문제_단지번호붙이기_https://www.acmicpc.net/problem/2667

# 1) 1_집 0_빔
# => 총 단지수 출력, 단지마다의 집의 수 오름차순

# 2) 1뜨면 주변 bfs든으로 연결 1수  세기& 0화
# 1 뜨면 큐append
# 2.2 ) 0건너가는 건 걍 첨부터? & 종료조건 ~~ 걍 전체 돌고 1뜨면 큐짓
# m2) 입력받으면서 1값 위치 체크 하고 처리하던가.    [  복잡도로 실패해서 결국 이 방법으로 전환  ]
# 3) 정렬

# * 01문자열
n = int(input())

map0 = []
ones = []
for i in range(n):
    map0.append(list(map(str, input())))  # 값 검사해서 1인 값의 위치 append할 거라 for을 통해 입력 받음
                                            # <-> # map0=[ list( map(str,input() )) for _ in range(n) ]
    for j in range(n):
        if map0[i][j] == '1':
            ones.append([i, j])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# visit대신 값 0화 & 체크
result = []


for target in ones:
    if map0[target[0]][target[1]] == '0':  # 단지화로 인해 0돼있을 수 있으므로 ones에서 뺀 것도 0체크 먼저 함.
        continue  # break아님

    que = [target]
    temp = 1 # - append할 때 ++[~~ print]해버림
    #  <-> 0 with pop할 때 temp++[~~ print]
    #     1대1 상황 맵핑 맞을듯. 1개 짜리도 따로 탈출문 만들진 않았으니 1개 pop가능하지.
    # - 디버깅 _ 출력값 분석 : 단지 개수 빼고 단지당 집 수만 값이 다 1 큼
    map0[target[0]][target[1]] = '0'  # bfs_ visit

    # print('target',target)
    # not_append=False
    while (que):
        v = que.pop(0)
        # if map0[v[0]][v[1]]=='0': # 미방문법이 더 낫다. # 이거 때문에 값 2,1,1작게 나온듯
        #     not_append=True
        #     break

        for k in range(4):
            nx, ny = v[0] + dx[k], v[1] + dy[k]
            if nx >= 0 and nx < n and ny >= 0 and ny < n and map0[nx][ny] == '1':
                que.append([nx, ny])
                map0[nx][ny] = '0' # visit
                temp += 1 # - 이름 의미 넣어라 # agroup_n 단지 당 수 # count

    # if not not_append :
    result.append(temp)  # 결과 출력용 단지 하나씩 수 저장

print(len(result))
result.sort()
for a in result:
    print(a)
# - 1h 13m ( 당연히 m1 풀이도 포함한 시간임. 항목만 보기 편하게 나눠놨을 뿐임 )

# - 변수 이름 : map0 -> 실수하기 쉬우니까 amap
# - 'bfs'는 결국 빠른 완전 탐색이야. '탐색'은 상황에 따라 forfor로 안 하는 게 나음
#   > 주변의 1 탐색만이 아니라, 그 시작 애를 정하는 '전체 탐색'케이스들에서도 쓰는 게 낫다.
#   > <-> 나_시작애 탐색m : 데이터 입력 시 '1'인 자료들 따로 만들기


# - 백준 : 주석 안 지워도 됨 (( 실행시간 영향 적음, 상황 마다 다를 수도 있음 ))
# - 내 미방문 체크법( 방문 시 걔의 값을 0으로 함으로써, 값이 1인지 검사하는 조건에서 자동으로 미방문체크도 되도록 값을 변경하게 짰음)


# - 첫 시도 [메모리 초과라뜨는데 알고리즘도  그냥 틀렸었음]
#   >  첫 노드 방문 처리를 안 했음
#   >  map0[i][j] == '1' 비슷한 코드에서 복붙할 때 제발 글자단위! == 에러발견못함
#
#   >  while 또 안해도 이미 forfor로 완전탐색인데 while 탈출조건 설계 때문에,  forfor 두번 하면 탈출이라 시복은 동일해서 괜찮음
#   -> exist 저렇게 하면 무조건 forfor 한 번 더 하게됨
#   ( 이유 : forfor한번이면 문제 해결되고 그 후 전체맵에 1이 없게 돼도, 그거 만들어가던 forfor에서 1나온적 있기에 while은 다음차례 때야 한번도 안 등장_탈출가능
#   2*O(n*2) 이라 빅오 똑같( exist 출력해보니 True False나옴 ) )

# -  필요없는 검사 회전까지 한 while : **완전엄밀히 생각하기** 엄밀하게 (이 문제 알고리즘의 딥한 케이스나 흐름)끝까지 생각은 안 해봤었음.
#  (시복 큰 차이 없을 거란 계산에서 그런거라기보다, 걍 문제 수준들이 시복 널널했었으니 추가 생각 시간 절약함: forfor한방이면 어차피 이미 끝날지를.))
#   -> 시간 급해도 알고리즘 상에선 엄밀 끝까지 생각하자?
#   > 같은 단지인지 검사 끝나고 처음부터 다시 돌아야한다고  생각했었음 ( forfor이 그 '시작대상'을 하고 있었는데 생각 너무 덜하고 급하게 풀었나. )
#     이건 바이러스같은거고, '시작대상'도 방문했던 곳 다시 할 필요도 없지.

# n= int(input())
# map0=[ list( map(str,input() )) for _ in range(n) ]

# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
#
# result=[]
# while(1) : # while 또 안해도 이미 forfor로 완전탐색
#     exist=False # exist : forfor돌면서 1(시작  대상인)이 한번도 안 나왔을때만 while문 탈출
#     for i in  range(n):
#         for j in range(n):
#             if map0[i][j]=='1':
#                 exist=True #
#                 # 큐
#                 temp=1
#                 que=[[i,j]]
#                 map0[i][j] = '0'   #~ 넣어야  정답임
#                 while(que):
#                     v=que.pop(0)
#                     for k in range(4):
#                         nx, ny=v[0]+dx[k], v[1]+dy[k]
#                         if nx >=0 and nx <n and ny >=0 and ny <n and map0[nx][ny]=='1':
#                             map0[nx][ny]='0'
#                             temp+=1
#                             que.append([nx,ny])
#                 result.append(temp) #
#                 # continue # 한번더 쳌? 꼬인 ㄱ경로 굳이 자세히 생각은 안햇음

#     if exist ==False:#
#         break
# print(len(result))
# result.sort()
# for a in result :
#     print (a)
