# 1)
# 가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사 받기 가능
# - (2) 심사대 비어 있는 곳 있어도, 다른 심사대 끝나기까지 남은 시간+소요시간이 더 빠르면 거기 쓰고 심사대 비게 냅두기 ㄱㄴ
# -> 모든 사람이 심사를 받는 데 걸리는 시간 최소화

# 2) times길이 십만 : o(log n) 
# times요소의 배수마다 n감소 // (굳이 이거부터) & (2)
# -> 최소값 : [n*min(times), ] # 굳이 엄밀
# 1분 ->
# m_한명마다 times = [1 , 4, 5]를 탐색 times업데이트?
# times.sort()
# 한명이 심사위원 고르면 -> 그 시간만큼 times값 감 소 하기엔 다른에가 빨리끝날수도 <-> 남은 시간바뀌면 정렬안됨. 우선순위큐 logn이네 반복문 n회. 해당심사위원 pop했다가_old 다시 해당심사위원 값 넣기. 다른 심사위원에게도 시간 흐른건 새로 pop한 거에 누적된 old 빼. 근데 사람씩 진행하기엔
# 3) 반복문 n회에서 pop한값-누적?old값이 조건위배될때까지 pop(n) (다시append)
# m_정답시간을 times에 분배_ 28분 _times에서 더 작은 7분
# answer//times[0]
# 27 : > 만족x ## answer탐색logn, 계산 n
# n=a+b==<= answer_28//times[1] +  answer//times[1] # 4+2
# 29 : <
# -
# -> answer 탐색 [1,] 쭉 말고 바
# (X_조건을 같은경우로만? n명 넘을필요없으니 ㅇ동시에 넘어질 수 있지). 막판에 누구한테 가도 같이 끝날 수 있구
# -> 답같을 때 정답왼쪽으로 갔는데 불일치할떄까지
# m_times 각 원소들 자체적인 값으로 동일한 값 만들?
def solution(n, times):
    times.sort()
    # print(times)
    start=1# - 최소값 대충 잡는다 해도 기왕이면 1,0으로 해라. times[0]*n는 아니지.
    end=times[-1]*n # 대충
    # - 마지막쯤 케이스 : 탈출없는 while문에서 L=M=R됐던 값 : While문 밖에서의 M (while밖은 end < start 상태이고 케이스에 따라 막판에 end나 start가 바뀜)
    #   > Ex. 1,3일때_2 (1,4일때_2 -> 34or 12) -> [1)길이1]i. 1,2_1 ii. 2,3_2  [L,R이 1차이일 때 M은 L화]->[2)동기화] i-i.1,1_1 i-ii.2,2_2 , ii. 3,3_3 ->[3)탈출된비동기화] i-i.1,0_(old1) 되고 탈출, i-ii.2,1_old2 되고 탈출 ii. 3,2_oldOR4,3_old3되고 탈출
    #   + 엄밀 생각은 시간걸리니까 딕셔너리에 update해두고 동기화된 값, 앞 뒤 두개씩 조사하면 편함. L-1_F, R+1_T인거라 [2)False,L=M=R,True] 이라서 한개씩만 조사해도 충분하긴함
    
    ##find=False
    # dict1={}
    ##answer 값 범위에서 탐색
    while(start<=end): # start > end이면 탈출
        mid=(start+end)//2 #1,4->2 13->2 12->1 22 11 
        
        # - 정답시간을 times에 분배. 만족 : n=a+b ==<= answer_28//times[1] +  answer//times[1]
        
        result=0
        for time in times:
            result+=mid//time
        if n <=result : # 만족 경우[answer로 n명 충분히 검사함] 
            # - 타겟이 더 작은 쪽에 있으니까 왼쪽으로 가기 위해 -1
            end=mid-1
            # dict1.update({mid:True})
            #find=True
        else:#if n > result : 
            #if find==True:
            # dict1.update({mid:False})
            start=mid+1
            
    # - 경우 : n명 넘는 값이 정답인 케이스일 수도 있음((ex.막판에 어디에서 가서하든 종료시간 똑같을 때))
    #   + -> 만족 때 왼쪽으로 '연속'으로 갔는데 불만족할때까지.((왼쪽이 불만족이며 자신이 만족일 때가 답)) (일치케이스가 아니고 이상이면 만족이라 우측죄다 만족케이스이어서 연속으로 가면 이진탐색의 이점을 잃음 그래서 -> ) 우연히 정답 딱 일치하는거말고 start-end= 1길이 나올 때까지 계속 계산해야함(그게 정답인 불만족만족의 경계인 이유 : 왼쪽탐색/오른쪽탐색을 하게 되는 조건이 만족/불만족이기 때문임. 그래서 이진탐색하며 두 조건 경우의 경계를 찾아나감.)[return안하고 끝까지 계산.(&저장_꼭 안해도됨)] m1 막판케이스 OR m2 배열에 저장해두기&탐색_이 문제에선 마지막에 나오는 경계찾으면 돼서 전체 다 탐색할 필요없음]. 
    
    # - False가 True되는 순간 : 아래 자세하게 생각하기에 시간들어서 최종 L,M,R 다 검사함. 
    #   + ex. 숫자안겹칠때_L-1이하_False L_ M_  R_ R+1이상_만족임 -> 마지막으로 검사하는 M : L이나 R이 M이랑 같음'~~ L_F M_ R_T' : ## 업데이트된 L,R은  항상  검사했던 M이 아닌 값  인 건 아님. M은 //이기도 함. L이 M+1로 업데이트 된 건 맞는데, 오른쪽에서 왼쪽으로 다가오다가그 M+1을 검사했을 수 있음)
    #   + while에서 동기화 후[2)False,L=M=R,True] 탈출했을 때, (i)L이 증가됐으면_'동기화됐던값인'M값 케이스가 불만족된거= M+1=증가된L (ii)R이 증가됐으면_동기화 케이스가 만족된거=정답M
    if start > mid :
        return mid+1
    else :
        return mid
    # dict1에 저장하는 방법 위아래에서 껐음
#     list1=[start,mid,end]
#     # print(list1)
#     list1.sort()
    
#     #temp=0
#     # print('after',start,mid,end)
#     for sme in list1:
#         if dict1[sme]==True:
#             return sme
#         # if list1.count(sme) >temp:
#         #     use=sme
#         #     temp=list1.count(sme)
#     #use 
#     #answer = 0
#     # return use
# 4) n = 1, 2, 
# times[] =1,2
# 심사관 명수 : 1,2
# 답 없을 때의 얘기 없으니 패쓰(조건에 의해 나올일이 없)


# - 1h 8m(+2?점)
#   > 이분탐색 첫 문제라, 이분탐색 돌아가는 중간 출력 학습용으로 40m보다 더 시간씀
    # + 이분탐색(이진탐색) : (1) 정답자체변수(t), 조건관련변수(n, 변수가 아니고 식일 수도 있음) 중 한 가지 '탐색'. (2) 변수들끼리의 단조성
    # + 정답시간을 길이가 N인 times에 분배해서 계산. 만족 : [충족해야하는 조건과 관련된 변수]n=a+b ==<= answer[정답변수]_28//times[1] +  answer//times[1]
    # + 이분탐색 쓰면서도 최적화식 생각해야하기도함. 첨에 //했을 때 그 식 먼저 구체화하는 게 빨랐겠다. | 최적화식_케이스에서의 식에서 생각

# - 다른 사람 풀이[신동주 , 변동현 , 이성재 , 탈퇴한 사용자 외 11 명] 
#   + answer = start로 하심. end 값 변경 때 mid로 한 거나 start<end 조건 차이로 인해 딱 저거인가. 난 처음 이론에서 배운 등호로 쓸 거라 적당히 패쓰
#   + False -> True 여야하니까 R을(R+1말구) True로 고정했네. True로 변경되는 R+1보다 R | 한쪽이라도 확실히 알고 있는 거 좋지

# def solution(n, times):
#     answer = 0
#     start, end, mid = 1, times[-1] * n, 0 ##정렬된 리스트란 조건 없지 않나 -1안되지 않나. 뭐변경됐다네 ㅇㅎ

#     while start < end: 
#         mid = (start + end) // 2
#         total = 0
#         for time in times:
#             total += mid // time

#         if total >= n:
#             end = mid 
#         else:
#             start = mid + 1
#     answer = start
#     return answer


# - 변수의 전역성_리스트(mutable_set, dict까지.)
#   + 함수 밖에서 선언한 거면[함수 내에서도 전역으로 쓸 수 있음] 괜찮지만, [함수 내에서 시작된 거면] 다른 함수에서 사용하려할 때 리스트여도 변수로 건네야함 (([로컬에서[함수] 선언한 것도 전역인 건 아님]))
    #   + 리스트와 다른 특징을 가진 타입의 차이 : 전역 '리스트'면[함수 밖에서 정의된 리스트] 함수 내이더라도 'global 글자 없이도' '그 전역 리스트를 바꿀 수도 있[인덱싱]'을 뿐, 
    #   + 함수 내에서 요소값 변경 말고, 재정의(리스트자체 = )를 하면 그 이름의 로컬 리스트가 생기는 것임
'''
aaa=13
def bbb():
  print(aaa) # - 뒤 라인 추가하면 에러 뜸. 아래 라인이라도 재정의 해버리면 함수에서 로컬변수 돼버렸기에 그럼 # local variable 'aa' referenced before assignment
  # aa=24
bbb()
print(aaa)
'''    
# - O(log n) : 시간복잡도, 점근 표기법에서 log의 밑은 중요하지 않음. [https://joyhong-91.tistory.com/12]

# - 이분 탐색 [이론 공부 : https://www.youtube.com/watch?v=-Gx0T92-7h8&list=PLVsNizTWUw7H9_of5YCB0FmsSc-K44y81&index=26]
#   + (1) 조건 : 이미 정렬된 리스트 | O(log n)
#   + (2) 구현 : 함수에서 쓸꺼면 list도 입력으로 받자. ((그 리스트가 solution이라는 함수에서 만들어진 거일 수도 있기 때문임))
'''
def binary(list1, start, end, target):
    while(start<=end):
        mid=(end+start)//2
        if list1[mid]==target:
            return mid
        elif list1[mid] > target :
            end=mid-1
        else :
            start=mid+1
    return None
'''
#   + (3) 라이브러리 : from bisect import bisect_left, bisect_right 
#     + 함수(list1, value): 정렬된 list1에서 value를 삽입할 인덱스의 가장 왼/오른쪽

#   + (4) 사용 환경 케이스_파라메틱 서치 
#     + (4.1) 최적화 문제를 결정문제(예/아니오)로 바꾸어 해결하는 방법. 
#     + (4.2) 탐색할 정답변수와 만족해야하는 조건 변수가 [단조함수관계] (같은 값 연속해서 가질 수 있는 상황이면 정답이어야하는 순서부터 탐색해서 해결? 하기엔 이진탐색임. 후조건처리로 정답인곳 앞뒤 탐색을 다른 값이 나올때까지 하고 그 중에 고를 수 있음 )
#     + (4.1) 큰 범위 예시 : 최소나 최대 찾기 문제

# - 코테 시 추가로 생성해도 괜찮은 정도 대략(시간, 메모리 제한 있음)
    # a=list(range(10000000))
    # 백억_메모리에러, 십억,억_실행시간 10초 초과, 천만_10초보단 낮음.
#   + 1초 & 192MB 문제_솔루션 외 추가 생성[https://www.acmicpc.net/problem/2178]
#     + [백만]_성공_대충8MB로치자. 천만_[pypy3]는성공(40ms&약80MB(128MB문제도 있으니 천만 지양)추가됨)python3에선메모리초과