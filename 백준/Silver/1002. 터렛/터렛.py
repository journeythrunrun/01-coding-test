# 1) 무한대 =-1 
# -> 류재명이 있을 수 있는 좌표의 수


import sys
input=sys.stdin.readline
# 원래는 거리 2개면 최대 2개가 접점인데.
# 접점 가능 '위치', '움직'임이  '정수'임 : 조건을 위한 d는 실수계산 & "움직임 거리는 x + y"만 각각 정수화로 이용
n=int(input())
data=[input().split() for _ in range(n) ]

# 2) 거리는 정수인거 보니 대각선도 2로 가는 것 따질듯
# x1, y1 ~ x2, y2 => dx, dy
# m1) x2=x1+dx, y2=y1+dy 화 가능 #  dr=dx+dy # r2+r1<dr:0개,=:1개
# m2) r이 10일때 : [x로 몇칸 y로 몇칸 갈지] x4부호경우의수 -> set, in # t 범위가 없어서 시간복잡도 예상이 잘 안가긴함
#   + 굳이 도착 위치까지 필요 없어서 & 테스트셋 최대 개수 (시간복잡도)몰라서 m1 우선

# 파이썬 연산한계 및 ==체크를 위한 round(는 추가 안해줬음
for i in range(n):
    x1, y1, r1, x2, y2, r2=map(int,data[i])
    min_d=( (x2-x1)**2+abs(y2-y1)**2 )**0.5

    # -1 케이스 : 동일좌표 & 동일거리
    # 동일 좌표 케이스 처리
    if x1==x2 and y1==y2: # min_d==0_조건문 하나 압축화 하려다 시간 굳이
        if r1==r2: ##
            print(-1)
        else :
            print(0)
    else:
        if r1+r2<min_d:
            print(0)
        elif r1+r2==min_d: # <->abs(r2-r1)=dr
            print(1)
        else :# r1+r2>min_d ## X_시간 순으로 보면, 동일한 곳에서 만났다가 같은 거리만큼 움직이면 됨
            # 한 원이 완전히 다른 원 안에 들어와버릴때=0 :: r1=1 , r2=10000 # r2-r1
            if abs(r2-r1) > min_d:
                print(0)
            elif abs(r2-r1) == min_d:
                print(1)
            else:
                print(2)
# - 55m
#   + 디버깅 :# 0,0 1 1,1 1일때 r1+r2==min_d이지만 여러곳가능. -> min_d를 실수화

# - 다른 사람 코드 [ssu77089]
#   + 조건문 압축 특정 문제 해 굳이 따로는 안하겠음
# import sys
# input = sys.stdin.readline
# t = int(input())
# ans = []
# for _ in range(t):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     d = (x2 - x1) ** 2 + (y2 - y1) ** 2
#
#     if r1 == r2 and d == 0:
#         ans.append(-1)
#     elif (r1 + r2) ** 2 < d or (r1 - r2) ** 2 > d:
#         ans.append(0)
#     elif (r1 + r2) ** 2 == d or (r1 - r2) ** 2 == d:
#         ans.append(1)
#     else:
#         ans.append(2)
# print(*ans, sep='\n')