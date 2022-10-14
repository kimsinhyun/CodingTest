# 1006_2
# 피보나치 수 5 (백준)
# https://www.acmicpc.net/problem/10870

# 피보나치 DP 재귀
# 재귀적으로 피보나치 호출하지만, 한번 계산하면
# 피보나치 숫자 리스트에 보관해두고 읽어옴

n = int(input())

fibvals=[0,1]
def fib(n):
    if n < len(fibvals):   
        return fibvals[n]
    else:
        # difference bw normal fib and dp fib is here
        # append to array here
        fibvals.append(fib(n-1) + fib(n-2))
        return fibvals[n]

print(fib(n))