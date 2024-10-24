# 1)
# 합이 최대가 되는 경로

# 2) 층 입력 받으며 . 층층이 저장해나가. 각경로. 
# a 
# b c : 

# 비슷한거 풀때 난 아래층에서부터(큰거 선택하여 경우의 수 줄임).
# - 아래층에서부터 c1 c2 중 큰 거 위로 c2 c3중에 큰 거 위로
# 3) n=500 -> O(n^3)
# for i in range( len(layers)-1 ) : for j in range( len(layers[-i-1])-1 ):
# ## 7이면 그냥 더해주기 
# layers[-i-2][j]+=max(layers[-i-1][j], layers[-i-1][j+1]) # - 뒤층 -(i+1) #layers[i][j]+=max(after_layer[j], after_layer[j+1])
# 둘다 길이. 2층부터
# (3) 누적되기 위해서 layer값으로하기
n= int(input() )
layers=[ list( map(int, input().split()) ) for _ in range(n) ]
for i in range( len(layers)-1 ) : # - 두 for 모두 : '길이' '-1' 돌기
    for j in range( len(layers[-i-1])-1 ):
        ## 7이면 그냥 더해주기->더해짐코드
        layers[-i-2][j]+=max(layers[-i-1][j], layers[-i-1][j+1]) # - 아래층[뒤층]부터 : -(i+1) #layers[i][j]+=max(after_layer[j], after_layer[j+1])
print(layers[0][0], end='')
# 4) 층길이 1,... : 1 , 7 
# 2
# 7
# 3 8
# 값 0, : 

# - 20m 
#   + 디버깅 없이 바로 맞췄는데 비교적 최근에 비슷한 문제 풀었었음
#   > 레벨3~~실버1이네 이것만 유독 그런가 [https://school.programmers.co.kr/learn/courses/30/lessons/43105]

# - import sys
# inpu=sys.stdin.readline

# - 다른 사람 풀이
'''
import sys
g=sys.stdin.readline
l=[0]
for i in range(int(g())): # - n이라는 변수에 입력받은 값을 저장 안 하고 바로 사용
 # - '위층 부터' 입력 받으며 바로 계산. 대신 위의 값을 아래로 두개씩 내림. 시복 차이는 안남
 #   + 대신 마지막층이 길면 max()때 더 걸림. 위층으로 올라가는 게 시복 나을듯. 근데 layers 저장해두고 하는 거랑 한 층씩 받으면서 하는 거랑의 엄밀한 시복차이는 모르긴함.
 #   + 위 층 부터의 방법도 조건 세부화에 따라 필요할 때 있을 수 있음
 t=[int(x)for x in g().split()] 
 d=[l[0]+t[0]] # i_0 :[a, a], _1:[a+b1] # - 중복해서 내릴 때 각 층의 첫 부분과 끝 부분은 겹쳐서 내려지는 값 없어서 그대로 끝값 더하면 됨
 d.extend([max(l[j-1],l[j])+t[j]for j in range(1,i)])# i_2_j1
 d.append(l[-1]+t[-1]) #[a+b1, a+b2]
 l=d # l : - 이전 층 관련 값으로 사용하기 위해 미리 저장해둠
print(max(d))
'''

# - 커밋_백준 
#   > 아마 주석 제외 실제 돌아가는 코드가 같으면 재커밋 안되나봄. 같은 페이지면 다시 열어서 제출해도, 로딩 너무 빨리 돌아가고 체크표시 뜨면서 제출 안된 상황
#   + 앞으론 pypy -> python으로 완성본 제출
#   > 예전 것도 수정본 업로드 안 된 것들 있겠네. 대체로 문제 들어가서 최근 꺼 보면 되긴함.
  