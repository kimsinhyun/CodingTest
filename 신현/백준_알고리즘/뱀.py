from collections import deque
def pp():
    for i in graph:
        print(i)
    print()
    
N = int(input())
graph = [[0]*(N+2) for _ in range(N+2)]
for i in range(len(graph)):
    for j in range(len(graph)):
        if i == 0 or j == 0 or i==N+1 or j==N+1:
            graph[i][j] = 2
num_apple = int(input())
apples = [list(map(int, input().split())) for _ in range(num_apple)]

graph[1][1] = 2
for a in apples:
    x,y = a
    graph[x][y] = 1
# for g in graph:
#     print(g)
num_move = int(input())
moves = []
for i in range(num_move):
    time, direction = input().split()
    time = int(time)
    moves.append((time, direction))
    
moves = deque(moves)
dx = deque([0,-1,0,1])
dy = deque([1,0,-1,0])
currnet_dir_x,currnet_dir_y = dx[0],dy[0]  #오른쪽

snake = deque([(1,1)])
time = 1
while True:
    # pp()
    head_x, head_y = snake[-1][0] , snake[-1][1]
    if moves and time-1 == moves[0][0]:
        if moves[0][1] == "D":
            dx.rotate(1) ; dy.rotate(1)
        elif moves[0][1] == "L":
            dx.rotate(-1) ; dy.rotate(-1)
        moves.popleft()
    head_x += dx[0] ; head_y += dy[0]
    # print(head_x, head_y, "time:", time)
    # if (head_x==0 or head_x>=N) or (head_y==0 or head_y>=N):
    #     break
    if graph[head_x][head_y] == 1:
        graph[head_x][head_y] = 2
        snake.append((head_x,head_y))
    elif graph[head_x][head_y] == 0:
        graph[head_x][head_y] = 2
        snake.append((head_x,head_y))
        tail_x,tail_y = snake.popleft()
        graph[tail_x][tail_y] = 0
    elif graph[head_x][head_y] == 2:
        time+=1
        break
    time += 1

print(time-1)