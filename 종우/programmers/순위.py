# 0405
# https://school.programmers.co.kr/learn/courses/30/lessons/49191

# solve using floyd-warshall
def solution(n, results):
    answer = 0
    floyd = [[0] * n for i in range(n)]
    
    for r in results:
        floyd[r[0]-1][r[1]-1] = 1
        floyd[r[1]-1][r[0]-1] = -1
    
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if floyd[i][k] == 1 and floyd[k][j] == 1:
                    floyd[i][j] = 1
                    floyd[j][i] = -1
                if floyd[j][k] ==1 and floyd[k][i] == 1:
                    floyd[j][i] = 1
                    floyd[i][j] = -1
    
    for r in floyd:
        if r.count(0) <= 1:
            answer += 1
    
    return answer