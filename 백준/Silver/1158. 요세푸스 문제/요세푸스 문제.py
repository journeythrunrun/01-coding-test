# https://www.acmicpc.net/problem/1158

# 0)
# 7 3
# 예제 출력 <3, 6, 2, 7, 5, 1, 4>

# 1) N명 '원' _ K번째 사람 제거 반복 _ 사람 다 제거 될 때까지
# -> 제거된 순서

# 2) 시복 널널할듯_k, n 둘 다 범위 5000까지임
# m1) pop, remove _ 문제 푸는 속도 + 부분점수
# m2) index
# m) 대상 남아있는거 지나면서 카운팅
# m)[이 방법씀] 각 위치인덱스에 인덱스로 더할 값 저장  0, 1

n,k = map(int, input().split())
target=list(range(1,n+1))
icount=[1]*n # 인덱스 0으로 땡겨서씀. ( 사람 n명 )
i=0

index=0
oldlen = len(target)
print('<',end='')
for time in range(n):# <->m2)pop_while (target):
    # 새 인덱스 찾기
    fork=0
    j=index # 진짜 index는 남겼으며 한 명씩 건너갈 j라는 임시 인덱스 사용
    while (fork<k):  # k가 되면 탈출 [k개 건너감]
        # if index not in seta: # 다른 방법 쓰려던 거 남겨둠
        fork+=icount[j] # 0_이미 제거 된 애라 카운팅 포함 안됨 1 
        index = j # 그냥 index로만 해도 되는데 문제 성공했던 코드를 보존하고자 추가 압축 안했음(그때도 문제 풀이 시간 때문에 추가 압축에 시간 들이진 않음)
        j= 0 if j+1 == n else j+1 - 다음 인덱스 / 맨 끝에서 0으로 돌아오는 거 주의
        # index+=1
    # index=j

    # if k * i > len(target) - 1 : # m 섞어서 쓰지 말기. pop할꺼면 -> index도 밀림 <-> pop안할꺼(시복 나음)면_썻던 인덱스 통과하기
    #     oldlen= len(target)
    #     index=
    # else
    #     index = index+i# (k * i) # % len(target)
    # j
    # while(1):
    #     if count[index]==1
    #         index= (k*i)%len(target) # <-> index()
    #     j+=1
    icount[index]=0
    if time<n-1: # 마지막 출력에서의 '>'를 위해 출력 분리 
        print(target[index],', ',sep='',end='')# m2)target.pop(index)) # 포맷팅 복습?
    # i+=1
    #
print(target[index],'>',sep='',end='')


# - 40m
#   문제도, 방법 떠올리기도 쉬웠는데, 구체화 단계에서 _ 저게 더 좋아보이네+빨라보이네 하며 너무 이방법 저방법 왔다갔다/섞어써버림
#   -> 2) 3) 구체화 완벽하게 하고 풀기
