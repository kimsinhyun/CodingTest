def solution(n):
    answer = ""
    while n:
        if n%3 != 0:
            answer += str(n%3)
            n = n//3
        else:
            answer+="4"
            n=n//3-1
    return (answer[::-1])
        
