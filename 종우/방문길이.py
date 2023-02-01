# 0131_2
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

# 내 풀이
def solution(dirs):
    xcoor = 0
    ycoor = 0
    edges = set()
    
    for dr in dirs:
        if dr == "L" and xcoor > -5:
            edge1 = str(xcoor) + str(ycoor)
            xcoor -= 1
            edge2 = str(xcoor) + str(ycoor)
            edges.add(combedge(edge1, edge2))
        elif dr == "R" and xcoor < 5:
            edge1 = str(xcoor) + str(ycoor)
            xcoor += 1
            edge2 = str(xcoor) + str(ycoor)
            edges.add(combedge(edge1, edge2))
        elif dr == "U" and ycoor < 5:
            edge1 = str(xcoor) + str(ycoor)
            ycoor += 1
            edge2 = str(xcoor) + str(ycoor)
            edges.add(combedge(edge1, edge2))
        elif dr == "D" and ycoor > -5:
            edge1 = str(xcoor) + str(ycoor)
            ycoor -= 1
            edge2 = str(xcoor) + str(ycoor)
            edges.add(combedge(edge1, edge2))
            
    print(edges)
    
    return len(edges)

def combedge(edg1, edg2):
    if edg1 > edg2:
        return edg1 + edg2
    else:
        return edg2 + edg1

# 다른 풀이 : edge + diretion set
# direction doesn't matter, so add bothsides and later divide by 2
def solution(dirs):
    s = set()
    d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    x, y = 0, 0
    for i in dirs:
        nx, ny = x + d[i][0], y + d[i][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            s.add((x,y,nx,ny))
            s.add((nx,ny,x,y))
            x, y = nx, ny
    return len(s)//2