def solution(n):
    answer = 0
    fibo_list = [0,1,1]
    for i in range(3,n+1):
        left = fibo_list[i-1]
        right = fibo_list[i-2]
        fibo_list.append((left + right) % 1234567)
    
        
    return fibo_list[-1]