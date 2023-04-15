import sys

sys.stdin = open('test.txt', 'r')



# dfs
def dfs(cur):
    visited[cur] = 1
    res_d.append(cur)
    for i in nodes[cur]:
        if visited[i] == 0:
            dfs(i)
    

# bfs
def bfs():
    while(len(queue) != 0):
        cur = queue.pop(0)
        visited[cur] = 1
        res_b.append(cur)
        for i in nodes[cur]:
            if visited[i] == 0:
                queue.append(i)

# main
n, m, s = map(int, input().split())

nodes = [[] for _ in range(n+1)]


for i in range(m):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

for node in nodes:
    node.sort()

res_d = []
visited = [0] * (n+1)
dfs(s)

print(res_d)

visited = [0] * (n+1)
queue = [s]
res_b = []
bfs()
print(res_b)