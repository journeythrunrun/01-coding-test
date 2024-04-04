# https://www.acmicpc.net/problem/17219

# 주소 : 영어, -, .  / 중복 없음 / 비밀 번호 : 대문자만
# 길이 최대 20
# 반드시 나왔던 거 검색
# n개의 줄
# m개의 줄  / 비밀 번호를 찾고 싶은 주소


# 2) []:

# m1) 시간 초과
# 시간복잡도 m2) 처음부터 알파벳 유관하게 저장
# m3) 딕셔너리
import sys
n, m =map(int, sys.stdin.readline().split())

dict1=dict()
set1=set()
for _ in range(n):
    a, b= sys.stdin.readline().split()
    dict1.update({ a : b })

answer=[]
for i in range(m):
    target= sys.stdin.readline().split()[0] # split : 리스트화되기에 [0]
    # for a in lista:
    # print(target)
    # if a[0]==target:
    # 찾기
    # m1) in set1
    # m2) 키 있으면 반환해주고 없으면 특정값 주는 get

    # 조건 : 해당하는 주소 무조건 있다.
    print(dict1[target])

# - 24분 : 실버 4끼리도 차이가 많이 나긴 하네
#   + 8분 : 82퍼에서 시간초과 : 갑자기 속도가 느려진 거 봐서는, 엣지 케이스

# - 딕셔너리 조회
#   + 내부 해쉬테이블 : 함수 평균 O(1)
'''
- 딕셔너리 조회
# 샛기~~셋겟
>> 3에러 없는 조회 ( & _ 없으면 원하는 값 반환 ㄱㄴ ) & "저장" 
: 1) dict1.setdefault(key, 11) # 가진 value 출력, 없는 키면 11 저장 & 출력

>> 4조회만  ( & _ 없으면 원하는 값 반환 ㄱㄴ )
: i) x.get('a',0) # value 출력, 없는 키면 에러 없이 0 출력
: ii) dict1[key1]은 원하는 값 반환은 없음

'''
