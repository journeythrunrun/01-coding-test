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
    person = list(map(int, sys.stdin.readline().split()))  ## [1,3]
    person[1] -= 1 # 번째-1 => 인덱스화
    if person[0] == 1:  ## 남
        for j in range(person[1], n, person[1]+1 ):  # [디버깅] '인덱스화'된 놈의 배수라 다시 +1. 인덱스&번째&연산 등장 시 예시를 써놓든 하자
            swits[j] = 1 - swits[j]## 스위치 상태전환

    else:  ## 여
        swits[person[1] ] = 1 - swits[person[1] ] ## 자기 번호 자신 아래 양쪽 바꾸는 코드에서 바꾸면 두번바뀌어져서 안됨.
        for j in range(1, n + 1):  ## 이것보다 양쪽에서 먼저 끝남
            if person[1] - j < 0 or person[1] + j > n - 1:
                break
            if swits[person[1] - j] == swits[person[1] + j]:  ## (for문 내에서 계속) 양쪽 같으면
                swits[person[1] - j] = 1 - swits[person[1] - j]
                swits[person[1] + j] = 1 - swits[person[1] + j]
            else:
                break
## 20개씩 출력
for i in range(n // 20 + 1):  ## 2개
    print(*swits[i * 20:i * 20 + 20])
# - 다른 사람[jhwon07]
# for j in range(0, T, 20):
#     print(*SWC[j:j+20])

#  - 37m
#    + 그렇게 어려운 느낌은 아니었는데 오래걸렸네.
#      + 변수 쓸 때 안"뽑아놓고" 인덱스의 인덱스라 사용할 때 의미 포착 늦었나? 뇌논리 코드구현부분(for 등에서 범위 제한 등)이 빠를 정도로 익숙하진 않았나?