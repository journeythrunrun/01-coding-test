# 1)스위치 n개(100이하)  :  1(on), 0(off)
# > m 100
# - 스위치 번호 받음
# 남(1) :  "받은 번호의 배수 (들) " 스위치 번호: 스위치 상태 전환

# 여(2) : 받은 번호 중심으로 이어서 양쪽 좌우 대칭인 것들 : 스위치 상태 전환

# -> 스위치 상태

# 2) 

import sys

n = int(sys.stdin.readline())
swits = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

for _ in range(m):
    person = list(map(int, sys.stdin.readline().split()))  # [1,3]
    person[1] -= 1
    if person[0] == 1:  ## 남
        for j in range(person[1], n, person[1]+1 ):  # -+1 ## 배수
            swits[j] = 1 - swits[j]  # ~ ## 스위치 상태전환




    else:  ## 여
        swits[person[1] ] = 1 - swits[person[1] ]
        for j in range(1, n + 1):  # 이것보다 왼쪽에서 더 빨리 끝날 수도 있음
            if person[1] - j < 0 or person[1] + j > n - 1:
                break
            if swits[person[1] - j] == swits[person[1] + j]:  # 계속 같은 상태
                swits[person[1] - j] = 1 - swits[person[1] - j]
                swits[person[1] + j] = 1 - swits[person[1] + j] # 2번
            else:
                break
    # print(swits)
# 번째라 swith [ -1
## 20개씩 출력
for i in range(n // 20 + 1):  # 2개
    print(*swits[i * 20:i * 20 + 20])


