import sys

input = sys.stdin.readline
N,K = map(int, input().strip().split(" "))

human_list = list(range(1, N+1))
kill_order = []

def kill_people(human_list,start_idx, K):
    if(len(human_list) < 3):
        kill_order.extend(human_list)
        return
    for i in range(start_idx, len(human_list)):
        if i == (K-1):
            kill_order.append(human_list[i])
            human_list =  human_list[i+1:] + human_list[:i] 
            kill_people(human_list, i, K)
            
kill_people(human_list, 0, K)
join_str = ', '.join(map(str, kill_order))
print( f"<{join_str}>")