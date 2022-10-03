def solution(numbers, target):
    answer = 0
    n_len = len(numbers)
    def dfs(idx, t_val):
        nonlocal answer
        if n_len == idx:
            if(t_val==target):
                answer += 1
                return
        else:
            dfs(idx+1, t_val+numbers[idx])
            dfs(idx+1, t_val-numbers[idx])
    dfs(0,0)
    
    
    return answer