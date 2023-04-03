# 0403
# https://school.programmers.co.kr/learn/courses/30/lessons/42861


# initial solve
def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2])
    visited = [False] * n
    for i in costs:
        if not visited[i[0]] or not visited[i[1]]:
            visited[i[0]] = True
            visited[i[1]] = True
            answer += i[2]
    
    return answer

