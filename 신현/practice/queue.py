# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input().strip())
# dq = deque()
# for i in range(N):
#     command = input().strip().split(" ")
#     if(command[0] == "push"):
#         print(int(command[1]))
#         dq.appendleft(int(command[1]))
#     elif(command[0] == "pop"):
#         try:
#             temp_val = dq.popleft()
#             print(temp_val)
#         except:
#             print(-1)
#     elif(command[0] == "size"):
#         print(len(dq))
#     elif(command[0] == "empty"):
#         print(1 if dq else 0)
#     elif(command[0] == "front"):
#         try:
#             print(dq[0])
#         except:
#             print(-1)
#     elif(command[0] == "back"):
#         try:
#             print(dq[-1])
#         except:
#             print(-1)
#     else:
#         print(command[0])
#     # print(dq)
                    
             