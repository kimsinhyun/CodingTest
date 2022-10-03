import sys
input = sys.stdin.readline
import heapq

N = int(input())

heap = []
for i in range(N):
    temp = int(input())
    if(temp != 0):
        heapq.heappush(heap, -temp)
    else:
        if(heap):
            print_val = heapq.heappop(heap)
            print(-print_val)
        else:
            print(0)
        
    