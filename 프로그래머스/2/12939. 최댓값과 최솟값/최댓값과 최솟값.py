
# *문제 str출력!! 
def solution(s):
    # answer= list( s.split()) # str이든 ord이든 실제 작은 음수가 더 min 값일 줄
    answer= list(map(int, s.split()) )
    return ' '.join([ str(min(answer)),str(max(answer)) ])