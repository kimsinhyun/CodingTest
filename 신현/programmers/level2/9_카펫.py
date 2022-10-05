def solution(brown, yellow):
    for i in range(2, int((s:=brown+yellow)**(1/2))+1):
        if s%i==0 and 2*(i+s//i-2)==brown:
            return [s//i, i]
