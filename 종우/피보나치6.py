# 1013_1
# https://www.acmicpc.net/problem/11444


# 내가 푼 코드
n = int(input())
a = 0
b = 1
divnum = 1_000_000_007
for i in range(1, n):
    a, b = b, (a%divnum+b%divnum)%divnum

print(b)

# 그냥 iterative하게 풀면 시간초과
# 시간 맞추려면 행렬곱으로 풀어야함
