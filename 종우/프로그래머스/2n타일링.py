# 0217
# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    fib = [0]*(n+1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = (fib[i-1]+fib[i-2]) % 1_000_000_007
    return fib[n]


# my solution !!! need to divide in every step
def solution(n):
    fib = [1,2]
    if n == 0: return 0
    if n == 1: return 1
    for i in range(2, n):
        fib.append((fib[i-1]+fib[i-2])%1000000007)
    return fib[n-1]
