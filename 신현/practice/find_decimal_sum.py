# https://www.acmicpc.net/problem/2581
import sys

input = sys.stdin.readline
def find_decimal(num):
    for i in range(2, int(num**0.5+1)):
        if(num%i) == 0:
            return False
    return True

M, N = map(int,input().split(" "))
list = [i for i in range(M,N+1) if find_decimal(i)]

print(sum(list))
print(min(list))