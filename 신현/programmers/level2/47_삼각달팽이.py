
        
def solution(n):
    x=-1
    y=0
    temp = [[0]*(i+1) for i in range(n)]
    val = 0
    for i in range(0,n):
        for j in range(i,n):
            if i % 3 == 0:
                x+=1
            elif i % 3 == 1:
                y+=1
            elif i % 3 == 2:
                x-=1
                y-=1
            val+=1
            temp[x][y] = val
    answer = []
    for i in range(len(temp)):
        answer.extend(temp[i])
    return answer
        
