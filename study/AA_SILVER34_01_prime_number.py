# https://www.acmicpc.net/problem/1929

m,n = map(int, input().split())
# m1) 각 수의 배수 뺴기
# m2) append -> 시복을 위한 set.add

# 2) 일단 시복 최적화는 무시하고 풀어볼까
seta=set()
seta.add(1)# 1 소수 아님!!!!!!!!!
for numb in range (2, (n)//2+1 ): # seta는 제외대상이기 때문에 검사대상의 끝이 몇 개 더 추가 돼도 괜찮음.
    i=2
    while(numb*i <(n)+1 ):
        seta.add(numb*i)
        i+=1

# 2, 3, 4, 5, 6
for numb in range (m, (n+1) ):
    if numb not in seta:
        print(numb)

# - 약 40분
#   + 1차 약 30분 : 78퍼 정도에서 틀림
#             = 엣지케이스 -> 1 소수아님( 금방 찾은듯 문제 조건보다가인가 코드 for범위보다가인가 )
#   + 예전에 소수 문제 알고리즘 읽기, 풀기 경험 있음 - > 거기에 핵심 알고리즘들도 있었을 테니 + 오래돼서 다 까먹었을 테니 기왕이면 거기 꺼 정리?

#   + 스터디 문제 설명의 힌트인 "에라토스테네스의 체" 개념에 대한 공부를 하지 않고 풀어봄 # 단, 체라는 단어를 듣고 과거의 알고리즘 기억이 조금 떠올랐을 수 있음

# - 집에서 코딩하면 문제 풀다가 다른 생각 드넹 집중