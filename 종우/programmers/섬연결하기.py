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

# solve using kruskals    
def getParent(parent, a):
    if parent[a] == a:
        return a
    return getParent(parent, parent[a])

def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)

    if parent[a] < parent[b]:
        parent[b] = a
    else:
        parent[a] = b

def findParent(parent, a, b):
    if getParent(parent, a) == getParent(parent, b):
        return True
    return False

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x:x[2])
    parent = [i for i in range(n)]

    count = 0
    for cost in costs:
        if count == n-1:
            break
        
        if not findParent(parent, cost[0], cost[1]):
            unionParent(parent, cost[0], cost[1])
            answer += cost[2]
            count += 1

    return answer