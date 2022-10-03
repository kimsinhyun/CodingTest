tower = int(input())

route = []
def hanoi(n, start, temp, dest):
    if( n == 1):
        route.append([start, dest])
        return
    hanoi(n-1, start, dest, temp)
    route.append([start, dest])
    hanoi(n-1, temp, start, dest)
    
hanoi(tower, 1,2,3)

print(len(route))
for i in route:
    print(i[0], i[1])