# 10개씩 출력
m, n = map(int, input().split())

# eight
#  / five/ four
# nine  
# 1 : one
# / seven/  /six 
# 3 three  2 two

# 0 : zero

dict1={ "8" : 0, "5":1, "4":2, "9":3, "1":4, "7":5,"6":6,"3":7, "2":8,"0":9 }
# m 딕셔너리 / [ , ] 앞 기준 정렬
result=[]
for num in range(m, n+1):
    lis_num=list(str(num)) # 8 / ['2', '8']
    temp=[0,-1,num]
    for i in range(len(str(num))):
        temp[i]=dict1[lis_num[i]] # 4 
    
    result.append(temp )
result.sort(key=lambda x: x[0:2])

for i, temp in enumerate(result):
    print(temp[2], end=' ')
    if (i+1)%(10)==0: # 이 프린트를 뒤
        print()    
# 22m

