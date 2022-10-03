import sys
input = sys.stdin.readline

V = int(input())
E = int(input())

graph = [[0] *(V+1) for _ in range(V+1)]

for i in range(E):
    a,b = map(int, input().split())
    graph[a][b] = 1

    
for k in range(V+1):
    for i in range(V+1):
        for j in range(V+1):
            if i == j:
                graph[i][j] = 1
                graph[j][i] = 1
            if(graph[i][j] == 1) or ((graph[i][k] == 1 )and (graph[k][j]) == 1):
                graph[i][j] = 1
                graph[j][i] = 1
                
for i in graph:
    print(*i)
           
answer = []
# for i in range(1,V+1):
#     cnt = 0
#     for j in range(1,V+1):
#         if graph[i][j] == 0 and graph[j][i] == 0:
#             cnt +=1 
#     answer.append(cnt)
for i in graph[1:][1:]:
    print(i.count(0))
# print(answer)