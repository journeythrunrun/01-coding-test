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

for i in range(1,len(students[0])+1):# 자릿수 증가 # 아 n이 사람수였네1!!!!!

    k+=1

    # n_decimal = [0] * 10
    if len(person_set)==0: #
        person_set=[ range(n) ]#~ # person_set # 그대로 [ range(n) ] 임. list()랑은 다름.
    # else :
    #     persons= target[exam]
    exist=False

    # 갑자기 indent추가해줄 때 , 초기화 위치 단락이동해줄 때, 단순복사 말고 각 변수 의미 및 앞뒤 layer 체크
    exam = set()  # 뒤에 for에 쓰이기 때문에[이건 한 bit당] 거기 넘는 level 초기화 해야함 # 3,4개이상인놈들 2,3번 append시 중복피하기 위해
    # old_set=person_set[:] # 주소 안 가지도록
    while(person_set): # digit 당
        persons=person_set.pop() # [사람들1,4,5 ]
        print(persons)
        target = [[] for _ in range(10)]  # '그 숫자'로 같은 놈들끼리' 행으로 저장 -> 검사
        seta = set()

        for person in persons: # n 1000이니까 그냥 다 돌자 # index+=1 # for로 다 돌진 않음
            str_numb = students[person][-i] # 3
            print('why', person,str_numb,seta) # 다른 person_set의 다른 행으로 부터 같은 digit으로 겹치면 꼬임
            target[int(str_numb)].append(person)  # 첫번째 사람인덱스도 저장하기 위하여 앞에서 append
            # 아래 그냥 str로 그대로 사용
            if str_numb  not in seta : # 처음 보는 숫자
                seta.add(  str_numb  ) # '5' # 조건이랑 코드 한줄 줄일 수 있는데 굳이

            else : # 2개이상이라 검사하게 될 것. # 이미 있으면 그놈들끼리 다음 데시말에서 검사할 것
                #exam.append( [    ]  ) # 사람. 뭘로 같은지는 상관없고 누구들끼리 같은지만 상관있음.->그래서 데시말 행
                exam.add(  int(str_numb)   ) # 검사해야할 digit
                # 타겟 행돌며 길이가 2이상일 떄 검사 or<--=> 검사대상 exam에 사람만 추가
                exist=True
            # print('exam',exam)
        # 중간에 생각했던 거긴하네. 그때 old_set 하려다가 왜 안해결하고 넘어갔었지.. #! 하고 해결하고 넘어가라 다른 원인 아니고 이것도 해결안됐었다
        # <-> while조건문
        # person_set pop으로 자동 초기화
    for ex in exam : # 해당 비트 다 끝나고 나서 for ###~
        person_set.append( target[ex] ) # 해당 행=사람들만 붙여줌 #~ target[ex] 가 같은 digit이 다른 person집합에서 출현시 덮여써져버림

    print ('뒤에서 i번째 같은놈들', i, person_set,exist) #  aaaa 3 []  / X_ aaaa 5 [[0, 1]] True 왜 5에서 끝나나했더니 n잘못봄
    if exist==False: #  한번이라도 같은 경우 계속 하기 <-> 다다르면 break
        break

print(k, end='')


# 디버깅 : 왜 있던 같은 요소에서 다른 거가되지 똑같이 안되지

#
