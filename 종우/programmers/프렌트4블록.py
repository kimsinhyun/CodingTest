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
            
            tr,tb,td = tracker[i+1][j], tracker[i][j+1], tracker[i+1][j+1]
            if r != cur or b != cur or d != cur:
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


# answer
def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    track = set()
    while True:
        for i in range(m-1):
            for j in range(n-1):
                block = board[i][j]
                if block == []:
                    continue
                if board[i+1][j] == block and board[i][j+1] == block and board[i+1][j+1] == block:
                    track.add((i,j))
                    track.add((i+1,j))
                    track.add((i, j+1))
                    track.add((i+1,j+1))

        if track:
            answer += len(track)
            for i, j in track:
                board[i][j] = []
            track = set()
        else:
            return answer
        
        while True:
            moved = 0
            for i in range(1, m):
                for j in range(n):
                    if not board[i][j] and board[i-1][j]:
                        board[i][j] = board[i-1][j]
                        board[i-1][j] = []
                        moved = 1
            if moved == 0:
                break
    return answer