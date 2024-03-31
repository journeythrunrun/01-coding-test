# https://www.acmicpc.net/problem/11047


# 1) (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
# 동전 N종류 : 바로 이전 동전의 배수
# -> 합 = K원을 만들기 위해 필요한 최소 동전 수
# 2) 최소_큰 동전부터 소비해야함.

# 3) 수식 : left=나머지 몫=코인수 (left)//동전


# 4) 엣지케이스
n, left = map(int, input().split())
coins=[ int(input()) for _ in range(n)]

i=1
result=0
while (0<left):
    # coins[
    left, result =left%coins[-i], result+ left//coins[-i]
    i+=1
print(result, end='')

# - 9m
# - 체감상 실버 3~4가 프로그래머스 Lv1(난이도 쉬운거부터 풀어서 최근 기억이 Lv1에서도 어려운 걸로 가중됐을 확률있음)이랑도 비슷하네