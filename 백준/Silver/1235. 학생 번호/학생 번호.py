# https://www.acmicpc.net/problem/1235

# 0)
# 3
# 1212345
# 1212356
# 0033445
# 예제 출력 3

# 1)
# 학생 번호 : 길이 같음
# - 뒤에서 몇자리(k)까지로 줄일 수 있니 # -> 최소 자리수

# 2) 뒷 자리부터 병렬로 보며(OR 저장) 같을 경우 그사람들만 계속 진행하며 k값 올리기
# -> 같은 놈들끼리 저장 및 비교

# bfs로 하기엔 모든 사람 조합할필요없음
# 3) 학생번호 : 리스트_-1 / while_자릿수용 while_사람용_index  <-> for & 탈출
n= int(input())
# -> m) 그냥 [:]로 다 비교 하기엔 사람 조합이 많지
# target=[True]*n  # **인덱스 0부터
students=[ input() for _ in range(n)]

k=0
target=[]
person_set = []

for i in range(1,len(students[0])+1):# 자릿수 증가
    k+=1
    if len(person_set)==0: # i==1 , 처음 -> 초기화
        person_set=[ range(n) ] # 그대로 [ range(n) ] 임. list()랑은 다름.
    exist=False

    #  초기화 위치 단락 이동 시 : 각 변수 의미 및 앞뒤 layer 체크한 후, 붙여넣기
    # old_set=person_set[:] # 2차원이라.., # 주소 안 가지도록
    temp=[]
    while(person_set): # 한 digit 당 사람들
        persons=person_set.pop() # 이전까지 같은 값 가져왔던 사람세트 or 처음:전부 # [사람들1,4,5 ] [2,3] 
        # print(persons)
        target = [[] for _ in range(10)]  # '그 숫자'로 같은 놈들끼리' 행으로 저장 -> 검사
        seta = set() # 중복인 애들 내에서 또 같은 숫자 가지는지 검사할 때, 해당 digit이 나온적 있는 값인지 체크용
        exam = set()  # 초기화 위치 : 뒤에 for에 쓰이기 때문에[이건 한 bit당] 거기 넘는 level 초기화 해야함 
        # 3, 4개이상인놈들 2, 3번 append시 중복피하기 위해

        for person in persons: # persons : 한 집단 # n 1000이니까 그냥 다 돌자 
            str_numb = students[person][-i] # 3
            # print('why', person,str_numb,seta) 
            # 디버깅 : 다른 person_set의 다른 행[다른 집단]으로 부터 같은 digit으로 겹치면 꼬임-> 각 집단 끝나고 중복사람들 저장 # 현재는 이것 반영수정한 코드 / tap중요
            #   -> 현재 persons가 같은 집단임
            target[int(str_numb)].append(person)# target[값]=[그 값 가지는 사람들, ,]  # 이때까지 같은 값을 가져온 모임인 persons내의 각 사람들을, digit을 행이름으로 가지는 target변수에 추가 저장[~~연결리스트]
            # 아래 그냥 str로 그대로 사용
            if str_numb  not in seta : # 처음 보는 숫자
                seta.add(  str_numb  ) # '5'

            else : # 2번 이상 봄: 다음번에  검사하게 될 중복애들. 
                #exam.append( [    ]  ) # 뭘로 같은지는 상관없고 누구들끼리 같은지만 상관있음-> target에 있는 '사람들'이 중요함
                exam.add(  int(str_numb)   ) # 다음 번에 검사해야할 "digit" # 사람 아님
                # 타겟 행돌며 길이가 2이상일 떄 검사 or<--=> 검사대상 exam에 사람만 추가
                exist=True
            # print('exam',exam)
        # 한 집단 비트 값 살펴보기 다 끝나고 나서
        for ex in exam : # 검사 대상 digit들
            temp.append( target[ex] ) # 해당 행["집단사람리스트"]으로 붙여줌
                                        # target을 통해 값[digit]=>그 값을 가지는 사람들 리스트
    for t in temp: # while 탈출 조건인 person_set이랑 엉켜서 위에서 append해주던 값 여기서 해줌
        person_set.append(t)

    # print ('뒤에서 i번째 같은놈들', i, person_set,exist)
    if exist==False: #  한 번도 중복 안 나왔으면 : while 탈출
        break
print(k, end='')

# - 2h 3m _ 디버깅
#  + for에서 n을 자릿수 개수로 써버림..
#  + 답맞았는데 쌩쑈시간++[6번째까지 같은놈들이면 7번째가 답 맞지] # - *내가 임의로 만든 예제_답 문제기반 E2E엄밀 생각
#  + person_set 추가 및 while조건 엉킴
#   중간에 생각했던 건데, 다른 거 해결 하려고 넘어가고 이거 다시는 안 한듯
# #! 하고 해결 스택에 추가해라.. 다른 원인 아니고 이것'도' 해결안됐었다
