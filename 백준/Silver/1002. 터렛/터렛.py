# 1) 무한대 =-1 
# -> 류재명이 있을 수 있는 좌표의 수

# 2) 거리는 정수인거 보니 대각선도 2로 가는 것 따질듯
# x1, y1 ~ x2, y2 => dx, dy
# m1) x2=x1+dx, y2=y1+dy 화 가능 #  dr=dx+dy # r2+r1<dr:0개,=:1개 
# m2) r이 10일때 : [x로 몇칸 y로 몇칸 갈지] x4부호경우의수 -> set, in # t 범위가 없어서 시간복잡도 예상이 잘 안가긴함


# 원래는 거리 2개면 최대2개가 접점인데. 정수 움직임&위치땐 -> r 계산도 x + y정수화로#~
import sys
input=sys.stdin.readline
n=int(input())
# 동일좌표
# -1 : 동일좌표 & 동일거리

data=[input().split() for _ in range(n) ]

for i in range(n):
    x1, y1, r1, x2, y2, r2=map(int,data[i])
    min_d=( (x2-x1)**2+abs(y2-y1)**2 )**0.5
    if x1==x2 and y1==y2:
        if r1==r2:
            print(-1)
        else :
            print(0)
    else:
        if r1+r2<min_d:
            print(0)
        elif r1+r2==min_d: # <->abs(r2-r1)=dr
            print(1)
        else :# r1+r2>min_d ## X_시간 순으로 보면, 동일한 곳에서 만났다가 같은 거리만큼 움직이면 됨
            # 원이 안에 들어와버릴때 0 : r1=1 , r2=10000 # r2-r1
            if abs(r2-r1) > min_d:
                print(0)
            elif abs(r2-r1) == min_d:
                print(1)
            else:
                print(2)
# 0,0 1 1,1 1일때 ==이지만 여러곳가능.
# -> min_d를 실수화

