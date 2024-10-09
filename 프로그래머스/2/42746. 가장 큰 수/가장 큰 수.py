# 0 이상의 정수 0 -> 정수 붙여 만들 수 있는 가장 큰 수 

# 2) 십만 -> O(nlogn)
# m1_ 전체 -> max()
# m2_앞대가리 높은 숫자부터 미리 sort -> 9가 98보다 우선. 
# 0 처리

# str -> ord로 바꿔서 요소요소 sort?
# 한자리와 두자리 : 7 75 # 똑같은 숫자 있으면 그 다음꺼 붙여서 더 높은? 보단 넘버 훑으며 중간에 넣기? 
# 9로 시작하는 거 : 9,10,10,10 -> 9,4 ->9,3,3 # 높은 순으로 할꺼라 한자리면 최대값 10_X_ 3x 34 : 3333 으로 우선순위해둬야하나_ 마지막 숫자  34 
# 맨마지막 요소에 길이 붙여놓고 길이 만큼.
# 17_ _ 17_1_6_ 17_9_4_ 15

# 1 0 0 0  1 111
# 17_7말고"(높아봤자_다음가능한숫자_그건 a,b보다 작음.자가복제?_완전똑같으면 짧은거먼저쓰면되니_그후최대값인자기자신값_ 15였으면?)""->_(17)  177(177) 그 뒤에 1보다 큰게 앞인거 먼저 나올일 없어서 무조건 후자가나음 -> 앞 숫자보다 작은지 큰지? 17717 17177 그 뒷숫자가 앞숫자보다 큰지 하드코딩? [ a vs b : ab ba 중에 더 큰거->lamba에서 두 요소 이용불가-> \더 작은 c는 a,b다 쓰고 나서니까.  \ X_짧은쪽에 c붙여서 비교]

# ((나머지가 16  15 있으면,  다음 숫자나 4자리다비교해야하는거아닌가
# => 다음 숫자 붙여보고 더 높은 수 붙이기 자릿수때문에 다를 수 있는데, 둘다 붙여높으면 자릿수 같음 _ 그렇게 정렬하드코딩을 lambda로 하기엔. 두 요소값다 이용해야함. 
#X_그냥 해당값 먼저했을떄랑 아닌 것중에 더 큰거이어서 
# sort = n logn <-> heapq

# - 각 10 숫자에서 각각정렬이 나으려나 : 4이면 


# 요소수까지하면 nlogn개클수도 있겠는데. 최대길이_4*n이라 상수라 ㄱㅊ
def solution(numbers):
    # - push pop 다 할 거면_근데 변경되는 요소수까지 반영하여 계산해보진 않았음 : heapq_nlogn+nlogn <-> sort_n+nlogn+n 
    # - 디큐 : 따로 sort하는 거 없음 
    q=[]
    for number in numbers : # 277
        str_number = str(number)# '277'
        q_part= [ int(one) for one in str_number] # [2,7,7]
        for i in range( 4-len(q_part) ): # - 남은 길이만큼 자가복제 & 나중에 쓸때는 길이만큼만 가져다 씀       
            q_part.append( q_part[i])# - int(str_number[i] ) ) 안되는 이유 : str_number에 6이 있으면 그걸 여러번 반복해야하는데 길이1개라 인덱스로 3번반복불가. append된 q_part는 연속 가능. 
            # print(i, str_number, q_part)

        q_part.append(len(str_number)) # 나중에 정답에 얼만큼 붙일지 알기 위해 길이저장
        q.append(q_part)
    q.sort(reverse=True)
    answer = ''
    for target in q: # [2,7,2,7,2]
        for i in  range( len(target)) :
            if i >= target[-1] : # 길이 넘으면 안 붙이기
                break
            answer+= str( target[i] )
    if answer[0]=="0": # 가장 큰숫자가 0인 상황. 0으로만 1개이상 이어진 경우
        answer="0"
    return answer
# 4) numbers길이 1, 
# 원소 0, 


# - 1h_시간초과로 테스트케이스 1개 질문방에서 값봄(+3점)
#   >  54m : 1문제 틀림 
#   + [0,0] -> "0" : 0주의 :'int 0'은 '붙여도' '0'. | 길이는 1부터여도 2까지 보기? 
#  - 이전에 풀었던 문제들->캘린더

# - 다른 사람 풀이 [Roasters , 김나래 , 김래현 , 김준호 외 4496 명]
def solution(numbers):
    numbers = list(map(str, numbers)) # - map이용해서 빠르게, 정수인 list->str인 list화 ##['3','38','1000','0'] ##sort=	['0', '1000', '3', '38']
    a.sort()
    print(a) 
    numbers.sort(key=lambda x: x*3, reverse=True) 
    # - x*3로 해도 정렬할 기준인 거고 그 x를 해당 순서로 정렬하는 거임.
    # - 복제한 것을 sort기준으로 함으로써, 굳이 number의 요소들 하나하나 처리할 필요 없음. 
    # - '문자열이' 'sort가 됨'. : '문자열 기준의 sort'라서 문제에서 원하는 대로 거의 sort 됨. 
    #   + 그러나 '3'이 '38'보다 작음처리임. 실제론 후자가 먼저 쓰여야 하니, 앞서 내가 푼 방법처럼 자기복제.
    # - 정렬할 값으로 복제한 게 최대 길이 초과해도 괜찮음. 복제한 게 길이가 더 길었는데 그 초과한 길이 직전까지 같다는 거는 그냥 그 복제한 거 쓰는 게 맞는 거임 (이유는 내 풀이 전 부분에 좀 적어둠)
    # - 0 : 마지막에 int 씌워주고(00 0화) 다시 str씌워주면 됨
    # - ''.join
    return str(int(''.join(numbers))) 




# - 다른 풀이2 [이준성 , KYUYOUNG-SHIM , 임지수 , 이현성 외 47 명]
#   + 적었던 방법 중 a,b 합친 결과 두개 비교하는거 sort에서 커스터마이징 가능했음
#   + key=  functools . cmp_to_key (comparator)  & comparator(a,b) 정의_return_정렬할 때 a가 큰 쪽이라 칠 경우에 1, b가 큰 쪽이라 칠 경우에 2, 같을 때 0 반환하도록 
#     > sort, sorted 다 가능
import functools
def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer