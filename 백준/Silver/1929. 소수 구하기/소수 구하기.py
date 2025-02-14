# https://www.acmicpc.net/problem/1929
# m이상 n이하에서의 소수 출력

###### 오랜만에 복습용? (읽고 나서 풀기)
# 1) 1,000,000 - > 
# 소수는 하나 이상 무조건 있음
import sys
readl=sys.stdin.readline
m,n=map(int, readl().split() )
seta=set([1])

for start in range(2,n//2+1): 
    end=2
    while(start*end<=n):
        seta.add(start*end)
        end+=1
for out in range(m,n+1):
    if out not in seta:
        print(out)

# - 시간복잡도
#   > https://github.com/journeythrunrun/01-coding-test/blob/f4b541dd2efbb16a17d8bc70ab8c17308ca1df18/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4/3/42898.%E2%80%85%EB%93%B1%EA%B5%A3%EA%B8%B8/%EB%93%B1%EA%B5%A3%EA%B8%B8.py#L152
#   > 10^6 : NlogN

#   + 한 번 클로드에게 물어봐 보았다 & 내가 좀 덧붙임 : O( n/2 + n/3 + ...n/n_n의배수는 안하니까 n까지 안가긴하는데 대충 시복 최대용 계산 간략화 )  ) = O( n * (1/2 + 1/3 + 1/4 + ...)  ) = O(n log n) # 증명은 클로드가 하던 거 보다가 교수님 설명이랑 너무 차원이 달라서 걍 내가 참고해서 종이에 써서 해봄. 개인적인 이유로 클로드를 먼저 쓰고 있긴 하다만 챗쥐피티가 좀 더 잘하는 것 같긴하다 ㅎㅋㅋㅋ 싫다는 건 아님 지금은 어떠한 이유로 클로드 먼저 쓰고 있을 정도임

# - seta 만드는 것도 m으로 시복 줄이기?

# - pypy가 10배 빠르기도 하네

'''
### 예전 풀이
m,n = map(int, input().split())
# m1) 각 수의 배수 빼기
# m2) append -> 시복을 위한 set.add

# 2) 일단 시복 최적화는 무시하고 풀어볼까
seta=set() # seta : 소수가 아닌 것들의 모음
seta.add(1)# - 1 소수 아님!!!!!!!!!

# - 시간복잡도 : 딕셔너리, set
# m이상 n 이하에서 소수가 아닌 것들의 모음을 배수를 이용해 seta에 저장한 후 제외해줄 거임.
# 제외 대상 : 2[numb]*2[i], 2*3, ..., 3*2, 3*3, ....
#   i의 범위 : 곱한 결과가 n 이하

# - 예전 코딜리티 알고리즘 글 복습 [111번 글]
#   + O(nloglogn)
#   + 내 코드 변수 numb를 i로 하고 내 코드 변수 i를 1씩 증가시키며 곱하는 대신, 그 i를 더해나감 & k라는 곳에 '결과값을 저장해서 사용
#   + 두 숫자 변수의 min, max 설정
#     + 1. 내 코드 변수 numb의 최대값 부분은 n//2인 것과 달리 sqrt(n)임. 3.에 의해 그러함.
#   
#     + 2. 내 코드 변수 numb가 1씩 증가하며 순차적으로 검사한 것과 달리 소수인 numb에 대해서만 검사함[중복 패쓰. ex 4는 이미 소수2의 배수로 검사했었음]
#     + 3. 곱할 앞 자리 숫자가 바뀌면 두번째 숫자는 다시 2부터[a*2 부터] 했던 것과 달리 a*a부터함. 
#       + a*(a보다 작은 수)는 이미 이전 루프에서 (a보다 작은 수)*a로 됐을 것이기에 그러함. # Ex. 2*3, 3*2 두번 검사할 일 없음.


#   + 변수 타입을 리스트로 한 건 문제에서 요구하는 결과가 달랐던 것도 있음. 
#     + 그래도, in set타입 검사가 평균 O(1)이라해도 평균과 달리 항상 O(1)인 리스트 조회가 더 빠를 것임 ((문제 풀땐 걍 빠르게 생각나는 시복 비슷한 방법으로 했음))
#       > 그래서 예전 필기에, 시간복잡도 : 딕셔너리, set라고 해놓기도 했었나봄

for numb in range (2, (n)//2+1 ): # > numb의 범위 : numb는 최대 numb*2 == n 까지만 검사해주면 되기에 range로 끝범위 +1해줌 # seta는 제외대상이기 때문에 numb 몇 개 더로 인해 검사대상의 끝이 더 추가 돼도 결과 영향없음.
    i=2
    while(numb*i <(n)+1 ):
        seta.add(numb*i)
        i+=1

# 2, 3, 4, 5, 6
for numb in range (m, (n+1) ):
    if numb not in seta:
        print(numb)
'''
# - 약 40분
#   + 1차 약 30분 : 78퍼 정도에서 틀림
#             = 엣지케이스 -> 1 소수아님( 금방 찾은듯 문제 조건보다가인가 코드 for범위보다가인가 )
#   + 예전에 소수 문제 알고리즘 읽기, 풀기 경험 있음 - > 거기에 핵심 알고리즘들도 있었을 테니 + 오래돼서 다 까먹었을 테니 기왕이면 거기 꺼 정리?
#     + [소수]* multiple만 제거 ==(_sqrt(n)을 초과하지 않는)

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