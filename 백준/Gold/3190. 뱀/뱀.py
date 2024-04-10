n = int(input())
k = int(input())

apple = []
for i in range(k):
    # 행, 열 좌표로 입력 준대
    apple.append(list(map(int, input().split())))
    apple[i][0] -= 1  ## -1
    apple[i][1] -= 1  ## -1

l = int(input())
turn = []
for i in range(l):
    turn.append(list(map(str, input().split())))  # str ["12" 'D"]

    # t초 후 L or D로 회전
map = [[0] * n for _ in range(n)]

# 사과 위치시키기
for i in range(k):
    map[apple[i][0]][apple[i][1]] = 1

# !가져다쓰면[행_y세로][열_x가로] -> 인덱스용 변수 저장, 가져다 쓸때 [1]<->[0]
# ->걍 dx dy해라
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 동 북 서 남 #X_[notx, noty]_d= [[1,0],[-1,0],[1,0],[0,1]]
present = [0, 0]
go = d[0]
go_index = 0
map[0][0] = 2  # 뱀 몸=2

bem = []  # append & pop(0)
# heapq.push(tail, (count,[0,0])) # count=0
t = 0
bem.append(present[:])

while (1):  # 뱀 몸=2
    # 방향 전환
    if len(turn) > 0 and t == int(turn[0][0]):
        if turn[0][1] == 'L':
            go_index += -3 if go_index == 3 else 1

        else:
            go_index += +3 if go_index == 0 else -1
        go = d[go_index]
        turn.pop(0)
    # 이동 (L or D) 및 new 위치!
    t += 1
    present = [a + n for a, n in zip(present, go)]  # new =[go[i]+present[i] for i in len(go)]
    bem.append(present[:])  # !present_새위치후 뱀 머리 위치 업데이트_머리 먼저 들이밀고 break체크 #~

    # [ 1,0 ] -> 2
    # print(map)
    if present[0] >= 0 and present[0] <= n - 1 and present[1] >= 0 and present[1] <= n - 1:  # try :
        new_visit = map[present[0]][present[1]]
    else:  # except :#! 인덱스에러_초과시에만 발생하고 음수는 계산돼버림 주의. # 벽 부딪힐 케이스
        break

    if new_visit == 1:  # 사과가 있음
        map[present[0]][present[1]] = 2  #! new_visit =2

    elif new_visit == 0:  # 사과가 없음
        map[present[0]][present[1]] = 2  #!new_visit=2
        # tail제거
        # [1]_디버깅용 출력
        erase = bem.pop(0)  # ~ 이미 비었으면#heapq.pop(tail)
        map[erase[0]][erase[1]] = 0
        # [2]_디버깅용 출력
    else:  # new_visit==2 or  # 자기몸
        break
print(t)
