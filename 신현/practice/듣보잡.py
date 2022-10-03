import sys
input = sys.stdin.readline

N, M = map(int,input().split())
list1 = set()
list2 = set()
for _ in range(N):
    list1.add(input().strip())
for _ in range(M):
    list2.add(input().strip())
    
answer = sorted(list(list1.intersection(list2)))
print(answer)