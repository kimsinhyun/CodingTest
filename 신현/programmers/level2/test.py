answer = 0
def dfs(current_row, previous_col, score, land):
    global answer
    if current_row >= len(land):
        if answer<score:
            answer=score
    else:
        for i in range(4):
            if (i != previous_col):
                dfs(current_row+1, i, score+land[current_row][i], land)            
                 
def solution(land):
    """
    1. N행 4열
    2. 한 행씩 내려옴
    3. 같은 열을 연속해서 밟을 수 없음
    """
    global answer
    for i, s in enumerate(land[0]):
        dfs(current_row=0, previous_col=i, score=0, land=land)
        print(f"answer={answer}")
    return answer

