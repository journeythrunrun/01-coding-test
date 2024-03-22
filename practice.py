from typing import Mapping

# 1) 1_집 0_빔
# => 총 단지수 출력, 단지마다의 집의 수 오름차순

# 2) 1뜨면 주변 bfs든으로 연결 1수  세기& 0화
# 1 뜨면 큐append
# 2.2 ) 0건너가는 건 걍 첨부터? & 종료조건 ~~ 걍 전체 돌고 1뜨면 큐짓
# m2) 입력받으면서 1값 위치 체크 하고 처리하던가.
# 3) 정렬

# * 01문자열
n = int(input())
map0 = [list(map(str, input())) for _ in range(n)]  # 0 먼저 시작시 주의 전에 나 정수필요할 땐 효율 어케햇더라

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# visi대신 0화 ->
result = []
while (1):
    exist = False
    for i in range(n):
        for j in range(n):
            if map0[i][j] == '1':
                exist = True
                # 큐
                temp = 1
                que = [[i, j]]

                while (que):
                    v = que.pop(0)
                    for k in range(4):
                        nx, ny = v[0] + dx[k], v[1] + dy[k]
                        if nx >= 0 and nx < n and ny >= 0 and ny < n and map0[nx][ny] == '1':
                            map0[nx][ny] = '0'
                            temp += 1
                            que.append([nx, ny])
                result.append(temp)  # :단지
                continue  # 한번더 쳌? 꼬인 ㄱ경로 굳이 자세히 생각은 안햇음

    if exist == False:
        break
print(len(result))
result.sort()
for a in result:
    print(a)
