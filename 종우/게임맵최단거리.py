# 0211
# https://school.programmers.co.kr/learn/courses/30/lessons/1844


# my attempt at bfs
def solution(maps):
    answer = 0
    x_a = len(maps[0]); y_a = len(maps)
    been = set()
    queue = []
    been.add((0,0))
    queue.append((0,0,1, been))
    
    while queue:
        x, y, l, track = queue.pop(0)
        if x == x_a and y == y_a:
            return l+1
        
        if x < x_a-1 and maps[y][x+1] == 1 and (x+1,y) not in track:
            track1 = track.copy()
            track1.add((x+1,y))
            queue.append((x+1, y, l+1, track1))
        if y < y_a-1 and maps[y+1][x] == 1 and (x,y+1) not in track:
            track2 = track.copy()
            track2.add((x,y+1))
            queue.append((x, y+1, l+1, track2))
        if y > 0 and maps[y-1][x] == 1 and (x,y-1) not in track:
            track3 = track.copy()
            track3.add((x,y-1))
            queue.append((x, y-1, l+1, track3))
        if x > 0 and maps[y][x-1] == 1 and (x-1,y) not in track:
            track4 = track.copy()
            track4.add((x-1,y))
            queue.append((x-1, y, l+1, track4))
            
    return -1