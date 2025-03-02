# - 문제집_DFS+BFS 필수 문제_로봇 청소기_https://www.acmicpc.net/problem/14503
# 
# # > 다시 푼 이유
#   복습하다가 왜 저렇게 비효율적알고리즘으로 했지 싶어서 그 비효율 방법을 이해하려하다가 걍 새로 효율적인 코드로 짬. 더 효율적인 방법 검증도 될겸. 코드 전체 짜는 연습도 될겸.

# //// 250301 복습 : 왜냐 코테는 암기인 부분들이 있어서(함수 등) 오랜만에 보면 다르기 때문이다. 다른 이유로 몇달 간 코테 공부를 계속 하고 있진 않았었다

# - 1) # => 총 청소칸 수 
#  1) 현재 칸이 청소 안돼있는 경우 : 현재칸 청소
# -> 2)주변 4칸이 다 청소 돼있는 경우 : 뒤로 한칸 후진할 수 있으면, 후진 -> 1)검사
# -> 뒤로 한칸 후진할 수 없었다면(# 디버깅 : 아 '벽'이면 후진할 수 없는거고' 청소했던 곳'은 괜찮은 거였음
# ), 멈춤
# -> 2-2) 주변 4칸 중 청소 가능한 칸 있는 경우 : 반시계방향 90도 회전(-1씩) & 앞칸이 청소 가능하면 전진 (방향 건네며 dfs) -> 1)

import sys
inpu= sys.stdin.readline

n,m = map(int, inpu().split())
r,c,d = map(int, inpu().split())
amap = [  list( map(int, inpu().split())) for _ in range(n) ]

dr=[-1,0,1,0]
dc=[0,1,0,-1]
cnt=0
# 끝쪽 맵 다 벽1

# 이미 방문했던 곳은 방문 안하기? 굳이? 어차피 청소 안돼있는곳으로 가는 거라 검사하게 돼서 비슷
while(1):
    exist=False
    # print(r,c,d) # - 알고리즘 바꾸면 전체적으로 영향 미칠 수 있는 거 다시 다 보기? 디버깅이 빠르나? 비슷하나? # 1,1,1 1,1,0이 왜오지 아 후진. 첨엔 청소했던 곳도 후진 못하게 해서 cnt를 여기서 하는게 ㄱㅊ햇는데 청소했던 곳도 후진 가능하게 하니까 cnt를 아래 조건문 안에 넣어야함
    
    if amap[r][c]==0:
        amap[r][c]=2 # 청소한곳. 후진을 위해 벽의값1과구분함
        cnt+=1
    # for a in amap :
    #     print(a)
    temp_d=d # 4방 검사용 방향
    for i in range(4):
        temp_d= temp_d-1 if temp_d!=0 else 3 # -1 한 번 된 방향부터 검사.
        nr,nc= r+dr[temp_d], c+dc[temp_d] # 주변 4칸 검사 # temp_d
        if 1<=nr<=n-2 and 1<=nc<=m-2 and amap[nr][nc]==0 : # 끝값은 벽이라 뺌
            r=nr
            c=nc
            d=temp_d
            exist=True # for 탈출 뿐 아니라 while continue도 하고 싶으면 추가 작업해야함.
            break # continue <-> break. for 탈출하려는 거니까 break맞았지. 
    if exist==True:
        continue
    # 여기까지 온 거 : 사방에 청소 가능한 곳 없음 -> 후진 가능하면 후진
    nr,nc =r-dr[d], c-dc[d] 
    if 1<=nr<=n-2 and 1<=nc<=m-2 and amap[nr][nc]!=1 : # 후진 가능한 곳인지(청소한곳은 괜찮고 벽만 아니면 됨)
        # print("후진")
        r=nr
        c=nc
        continue
        # 자동으로 1)로 가짐
    else :
        break
    
print(cnt)
# - 대략 30분? 근데 복습하다가 그냥 더 효율적인 방법으로 직접 푼 거라 시간 기준을 뭐로 둘지 애매하긴 함


# 1)
# 빈칸0 or 벽1
# 현재 빈칸 처음봄 : 방문화
# 주변도 다 청소돼있는 경우 : 한칸 후진(*벽이면 멈춤) -> 주변검사
# -> 주변 있 : 반시계 방향 90도회전 -> 미방문 빈칸_전진 
# => 청소하는 칸 수

# ////
#  빈칸0 or 벽1 => 청소하는 칸 수
# - 1) 현재 칸이 청소 안돼있는 경우 : 현재칸 청소
# -> 2)주변 4칸이 다 청소 돼있는 경우 : 뒤로 한칸 후진할 수 있으면, 후진 -> 1)검사
# -> 뒤로 한칸 후진할 수 없었다면, 멈춤
# -> 2-2) 주변 4칸 중 청소 가능한 칸 있는 경우 : 반시계방향 90도 회전(-1씩) & 앞칸이 청소 가능하면 전진 (방향 건네며 dfs) -> 1)
# # -> 

# n, m= map(int, input().split() ) #
# dr=[-1,0,1,0] //// 시계방향
# dc=[0,1,0,-1] # 북 동 남 서
# r, c, d_i = map(int, input().split() )
# count=0
# map0=[]
# for _ in range(n):
#     map0.append(  list( map(int, input().split() ) ) ) # list
# force=[False]
# # - 예시 케이스 정확하게 보기
# #   처음에 1,0 개수 잘못셈

# # - while 방법으로 잘 풀어지면 일부러 b/dfs 방법으로 풀려고 안 해도 됨
# # 직관적 떠오른 while법보다 아는 재귀함수 꼴로 풀어내려다가 더 복잡해진 것 같기도 함[약간 다른 상황이기도 했구][재귀용0다맞추기문제아니었으며 그코드도맞게 만들었엇긴함]
# # 재귀꼴로 안하고 while로 해버리곤해서 재귀꼴로 연습하려했던건데, 재귀의 개수제한이 더 심하니까 둘 다 ㄱㅊ한 건 반복문으로 풀어버리는 방법이 나을 수도 있음

# # while(1):
# #    if map0[r][c]==0:
# #        count+=1
# #    map0[r][c]=2 #청소할 곳 

# def fs(r,c,d_i ):  #//// r, c, 현재 진행 중인 방향
#     if force[0]==True : #////
#         return 
#     #print(r,c,d_i)
#     global count
#     if map0[r][c]==0: #//// 1)
#         count+=1
#     map0[r][c]=2 #청소할 곳  #////
#     temp_di=d_i #//// 체크용 방향temp와, 전진용 방향. 근데 걍 알고리즘 때 합쳤어도 되긴함
#     exist=False
#     for i in  range(4): # 있는 경우 회전 #//// 주변에 청소 가능한 곳 있는지
#         # - 문제 설명을 통한 상황 흐름 인지 : 정확하게 구체화
#         # 어차피 있을경우 1번 거치면서도 결국 반시계방향으로 회전하면서 가짐-> 조건말과 동일상황으로:그냥 반시계검사시 그걸로 갖기 ㄱㅊ
#         nr=r+dr[temp_di]
#         nc=c+dc[temp_di]
#         # print('new target',nr,nc,d_i)
#         if nr>=0 and nr<n and nc >=0 and nc < m and map0[nr][nc]==0 : # 완전
#             exist=True //// 주변에 있다
#             break
#         if i!=3 :# 이건 이전 재귀풀이용 때 했던 거 #//// 마지막 i 가 아니면 temp_di를 반시계방향으로 돌리기. 굳이 이 조건문까지 해서 초미세 효율화할 필요까진 없긴 함. 
#             temp_di= -1 if temp_di==-4 else temp_di-1  # 시반대방향
#     if exist==True : #//// 주변에 청소할 곳 있으면
#         d_i= -1 if d_i==-4 else d_i-1 # -  <-> good_ d = (d + 3) % 4 #//// 반시계 회전
#         nr=r+dr[d_i] #//// 
#         nc=c+dc[d_i] 
#         # 문제 1번이 어디의 1번을 말하는 거람 / # 문제 이해가 애매한데 문제 풀면서 각 다양한 경우싀 수 풀이 다 하는 것도 웃기고   
#         # -> 근데 확률상 큰 1번 말하는 거 같긴 함
#         if  nr>=0 and nr<n and nc >=0 and nc < m and map0[nr][nc]==0:
#             fs(nr,nc,d_i) #//// 전진
#         else :
#             fs(r,c,d_i) # 바로 앞쪽 칸은 아니더라도 다른 회전 하기 위해 1번 돌아가기
#     else:
#         nr=r-dr[d_i] # 네 방향 다 본 후 후진할 거임
#         # 전체 갯수랑 다르게 나오려면 그대로 빠꾸는 아니어야 함_4번째 연산 전 사용한 d_i가 그 1번째와는 다른 방향일듯
#         nc=c-dc[d_i]
#         if nr<=0 or nr>=n-1 or nc <=0 or nc >= m-1 or map0[nr][nc]==1 :
#             force[0]=True
#             return
#         fs(nr,nc,d_i)
#             #if map0[nr][nc]==1 :
#             #    force[0]=True
#             #    return 1
#             #else :
#             #    fs(nr,nc,d_i)
#     # - X
#     # fs 함수로 한칸 후진 자동 방법으로 하기엔, 네방향 다 본 후 어디보고 있는 상태에서 후진하느냐에 따라 다를 수 있음.
#     # 문제 설명 알고리즘, 예시 답에 의해 다 없으면 마지막으로 본 4번째 방향을 보는 상태로 후진하는 걸 알 수 있음
        
# fs(r,c,d_i)
# # 다른 생각하지 말기
# print (count)
# #print(map0)

# # - 약 2시간
# # - 문제 푼 후 다른 사람 풀이도 봄
# # [1]jike246
# ##N, M = map(int, input().split())
# ##r, c, d = map(int, input().split())
# ##arr = [list(map(int, input().split())) for _ in range(N)]
# ##dr = [-1, 0, 1, 0]
# ##dc = [0, 1, 0, -1]
# ##
# ##def robot(r, c, d):
# ##    cnt = 1
# ##    arr[r][c] = 2
# ##    while 1:
# ##        for _ in range(4):
# ##            d = (d + 3) % 4
# ##            nr, nc = r + dr[d], c + dc[d]
# ##            if arr[nr][nc] == 0:
# ##                arr[nr][nc] = 2
# ##                cnt += 1
# ##                r, c = nr, nc
# ##                break
# ##        else:
# ##            r, c = r + dr[d] * (-1), c + dc[d] * (-1)
# ##            if arr[r][c] == 1:
# ##                return cnt
# ##
# ##print(robot(r, c, d))
    
    
