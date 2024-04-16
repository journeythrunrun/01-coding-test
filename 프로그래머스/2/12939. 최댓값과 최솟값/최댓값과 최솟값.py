
# str출력!! 
def solution(s):
    # answer= list( s.split())# str이든 ord이든 음수가 작은 값일 줄
    answer= list(map(int, s.split()) )
    # answer=list(map(int,s.split(' ')   )   )  
    
    
    return ' '.join([ str(min(answer)),str(max(answer)) ])