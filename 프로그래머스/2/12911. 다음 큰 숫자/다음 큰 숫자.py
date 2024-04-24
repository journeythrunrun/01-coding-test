# 0)n	result
# 78	83
# 1) n보다 큼 & 2진수로 변환했을 때 1의 갯수가 같음 & 그 중 가장 작은 수

# => 다음 큰 숫자

# 2) m) for하기엔 n이 크니까, 2진수 조건 먼저 처리해보자 <-> m2) n이 숫자가 커도 조건을 만족하는 다음 큰 n과의 간격은 크지 않을 거라 ㄱㅊ함
# -> 1의 갯수 
# -> 그 개수로 보다 큰 숫자 중 가장 작은 거 만들기 / 1 땡겨가기 등
#   m1) 수학적 : 1을 앞으로 땡길건데, i) 가장 뒤에 있는 1을 땡길거임. ii)1이붙어있어서 뒤에서 첫 번쨰가 아닌 1을 앞으로 떙겼으면, 나머지 1은 다 뒤로 몰아버릴수 있음.
#   m2) bin, 1숫자세어가며

# 3) 
# -> bin(n)[2:].count('1')
# -> 0 index부터 '1'이 나오는 다음 인덱스 까지 검사 -> 붙었는지 판정
# -> i) 안붙 : 맨뒤1땡기기 / ii) 붙 : 뒤에서 첫 번쨰가 아닌 1을 앞으로 떙겼으면, 나머지 1은 다 뒤로 몰아버릴수 있음.

# 집중 집중
def solution(n):
    cnt=bin(n)[2:].count('1') #'1001110'
    while(1):
        n+=1
        if bin(n)[2:].count('1')==cnt:
            return n
        
#     bin_n=bin(n)[2:] #'1001110'
#     until_next,side=False, False        
#     for i in range(len(bin_n)):
#         if until_next==True:
#             if bin_n[i]=='1':# side=True
#                 # 1이 아닐 떄까지 검사 / 코드 압축은 귀찮
#                 while(bin_n[i]!='1') :
#                     i+=1
#                 # # 0인 위치. 0이 없음ㄴ
#             else:
#                 list_n=list(bin_n)
#                 list_n[i],list_n[i-1]='1','0'
#                 answer=str(list_n)
                
                
#             break
#         elif bin_n[i]=='1':
#             until_next=True
#     # i = 첫 뒤1 다음 위치
#     return 0#bin_n if side==False else
# 4)
# 앞으로 떙길 위치가 없다면. i가 그런 위치라면 '추가' & int
# 1이 1개도 없을 때 : 자연수라 발생하지 않는 경우임
# n은 1,000,000 이하