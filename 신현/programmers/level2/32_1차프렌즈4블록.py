def solution(m, n, board):
    from collections import deque
    answer = 0
    temp = [deque([0]) *(m) for _ in range(n)]
    for i in range(len(board[0])):
        for j in range(len(board)):
            temp[i][j] = board[j][i]
    go_on = True
    while go_on:
        remove = [deque([False]) *(m) for _ in range(n)]
        for i in range(len(temp)-1):
            for j in range(len(temp[j])-1):
                # ===========================================
                if(temp[i][j] == temp[i][j+1]):
                    if(temp[i][j] == temp[i+1][j]):
                        if(temp[i][j] == temp[i+1][j+1]):
                            if(temp[i][j] != "_"):
                                remove[i]  [j]   = True
                                remove[i]  [j+1] = True
                                remove[i+1][j]   = True
                                remove[i+1][j+1] = True
        remove_num = 0
        for i in range(len(remove)):
            remove_num += sum(remove[i])
        # print(remove_num)
        if(remove_num) == 0:
            return answer
        else:
            answer+=remove_num
                
        temp_len = len(temp[0])
        for i in range(len(temp)):                        
            temp[i] = deque([temp[i][k] for k in range(len(remove[i])) if remove[i][k] != True])
            for j in range(temp_len - len(temp[i])):
                temp[i].appendleft("_")   
        
        # for i in temp:
        #     print(*i)
        # print()
        # for i in range(len(remove)):
        #     for j in range(len(remove[0])):
        #         print("T" if remove[i][j]==True else "F", end=" ")
        #     print()
        # print()
        # print()
        # go_on=False
            
    return answer
