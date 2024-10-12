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
    start=1#times[0]*n
    end=times[-1]*n # 대충
    
    find=False
    dict1={}
    while(start<=end): # start > end이면 탈출
        
        # print(dict1)
        
        mid=(start+end)//2 # mid~~answer # 14->2 13->2 12->1 22 11 
        # print(start,mid,end,'->')
        #조건 #미리계산하기엔 굳이
        #answer_28//times[1] +  answer//times[1]
        result=0
        for time in times:
            result+=mid//time
        if n <=result : # 만족 # <=
            end=mid-1
            dict1.update({mid:True})
            #find=True
        else:#if n > result : # - 올려야함
            #if find==True:
            dict1.update({mid:False})
            start=mid+1
        #~print(start,mid,end)#긴거
    # 넘는 게 정답일 수도 있음
    # -> <=만족 때 왼쪽으로 '연속'으로 갔는데 불만족할떄까지. 우연히 정답 딱 일치하는거말고 start-end= 1길이 나올떄까지 계속 계싼해야함[return안하고 끝까지 계산& 저장. 막판케이스OR 배열에 저장해두기&탐색]. 
    # 
    list1=[start,mid,end]
    list1.sort()
    temp=0
    # print('after',start,mid,end)
    for sme in list1:
        if dict1[sme]==True:
            return sme
        # if list1.count(sme) >temp:
        #     use=sme
        #     temp=list1.count(sme)
            
        
    #use 
    #answer = 0
    # return use
# 4) n = 1, 2, 
# times[] =1,2
# 심사관 명수 : 1,2
# 답 없을 때의 얘기 없으니 패쓰(조건에 의해 나올일이 없)


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

# - 이분 탐색 
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
