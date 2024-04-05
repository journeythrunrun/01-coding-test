# https://www.acmicpc.net/problem/1929

m,n = map(int, input().split())
# m1) 각 수의 배수 빼기
# m2) append -> 시복을 위한 set.add

# 2) 일단 시복 최적화는 무시하고 풀어볼까
seta=set()
seta.add(1)# 1 소수 아님!!!!!!!!!
# - 시간복잡도 : 딕셔너리, set
for numb in range (2, (n)//2+1 ): # seta는 제외대상이기 때문에 numb 몇 개 더로 인해 검사대상의 끝이 더 추가 돼도 결과 영향없음.
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


# - 타인 [ssaemo] : 어차피 볼 거면 codility 코드가 더 낫다
# import sys
# readl = sys.stdin.readline
# def f():
#     candidates = [1] * (n+1)
#     candidates[1] = 0
#     i = 2
#     while i**2 <= n:
#         if candidates[i]:
#             ii = i*i
#             while ii <= n:
#                 candidates[ii] = 0
#                 ii += i
#         i += 1
#     prime_nums = []
#     if m <= 2:
#         prime_nums.append('2')
#     if m % 2 == 0:
#         mm = m+1
#     else:
#         mm = m
#     for i in range(mm, n+1, 2):
#         if candidates[i]:
#             prime_nums.append(str(i))
#     s = '\n'.join(prime_nums)
#     sys.stdout.write(s)


# m, n = [int(i) for i in readl().split()]
# f()
