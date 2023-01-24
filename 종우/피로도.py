# 0124_1
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

# 내 풀이
import itertools
def solution(k, dungeons):
    max_d = 0
    visit = list(itertools.permutations([i for i in range(len(dungeons))]))
    for i in visit:
        n_d = 0
        life = k
        for j in i:
            if dungeons[j][0] <= life:
                n_d += 1
                life -= dungeons[j][1]
            else:
                break
        if n_d > max_d:
            max_d = n_d
    return max_d

# 다른 풀이 dfs
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer