def solution(m, n, board):
    count = 0
    board = [list(i) for i in board]
    
    tracker = [[0]*n for i in range(m)]
    print(tracker)
    # find 4 pair blocks
    for i in range(m-1):
        for j in range(n-1):
            cur = board[i][j]
            r,b,d = board[i+1][j], board[i][j+1], board[i+1][j+1]
            
            tn,tb,td = tracker[i+1][j], tracker[i][j+1], tracker[i+1][j+1]
            if n != cur or b != cur or d != cur:
                continue
            if tracker[i+1][j] == 0:
                count += 1
                tracker[i+1][j] += 1
            if tb == 0:
                count += 1
                tb += 1
            if td == 0:
                count += 1
                td += 1
                
    print(tracker)
            
    
    # track found blocks
    # count removed number
    # reorder blocks
    
    answer = 0
    return answer