import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())
heap = []
for i in range(N):
    temp = int(input().strip())
    if(temp != 0):
        heapq.heappush(heap, -temp)
    else:
        try:
            print_val = -heapq.heappop(heap)
            print(print_val)
        except:
            print(0)
        
    
