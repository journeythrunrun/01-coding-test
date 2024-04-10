# 시간 제한 별 시간복잡도
# 마지막 카드 구하기

# 시간복잡도 크게 신경 안 쓴 방법

# 버스에서 푼 집중력 정도
n=int(input())

if n==1:
    print(n,end='')
    exit()
elif n==2:
    print( n,end='')
    exit()
target=list (range(1,n+1))
index=1

# 괜히 홀수 자동필터링효율화
# for num in range(2,n+1,2): # 2,4&[3].6[5]
while(1):
    if index==len(target)-2: # 인덱스 : target에서 보게 될 것. ==마지막꺼면 마지막 한 장 남은거고, 초과했으면 버리기 전에 이미 1장남았던 것
        print(target[-2],end='')
        break
    elif index==len(target)-1: # 인덱스 : target에서 보게 될 것. ==마지막꺼면 마지막 한 장 남은거고, 초과했으면 버리기 전에 이미 1장남았던 것
        print(target[-1],end='')
        break


#    elif index>=len(target)-1: # 인덱스 : target에서 보게 될 것. ==마지막꺼면 마지막 한 장 남은거고, 초과했으면 버리기 전에 이미 1장남았던 것
#        print(target[-1],end='')
#        break
    num=target[index] #  # 2,4&[3].6[5]

    target.append(num)# 1 '2 3 '4 "5" 2 '4[3]
    #print(f'temp:{index},{num},{target},')

    index+=2 # ->[3]=4
    

# 엣지 케이스 100퍼 처리 < 일단 푸는 속

# 25분 : 98퍼 정도에서 틀림 -> i) 엣지케이스!~ ii) 시간복잡도





    
