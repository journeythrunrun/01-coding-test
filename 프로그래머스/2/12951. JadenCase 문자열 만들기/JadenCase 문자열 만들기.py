# 1) '단어의' 첫_대문자or비영어 & 나머지_소문자 
# 2) 첫:소문자면대문자로 / 나머지: 대문자면 소문자로 / 공백도 그대로
def solution(s):
    answer=''
    # print(f'11{ord(" ")}hhh{chr(ord(" "))}'  )
    # ord & chr_ character
    # 같은 층 애들한테 ord 다 똑같이 씌워줬는지 체크. 자주 실수하는 것 같음.
    j=0
    for i in range(len(s)) :# i==0케이스 앞으로 뺴려다가 말았잖아
        if j==False and ord('a')<=ord(s[i]) and ord(s[i]) <= ord('z') :
            # .upper
            answer+=chr(ord(s[i])-ord('z')+ord('Z')) # a-z=A-Z

        elif j!=False and ord('A')<= ord(s[i]) and ord(s[i]) <= ord('Z'): # 작은 시간복잡도 줄이기는 굳이 안함
            answer+=chr(ord(s[i])+ord('z')-ord('Z'))
        elif s[i]==' ':
            j=False
            answer+=s[i] # 이미 문자인데 chr을 여기에도 다 붙일 필요 없다!
            continue
        else :  
            answer+=s[i]
        j=True
    return answer

# - 26m, +7
#   + 쉬운데 오래 걸림 : chr ord 동일 적용 안 한 거 빨리 못찾음, 문제를 잘못 이해한 시간 조금
# - .lower() .upper() 방법을 ord보다 먼저 떠올리자.(시간복잡도 차이는 모름)
