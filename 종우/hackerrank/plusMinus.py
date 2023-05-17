# 0517

#!/bin/python3

def plusMinus(arr):
    denominator = len(arr)
    pnz = [0, 0, 0]
    for x in arr:
        if x > 0:
            pnz[0] += 1
        elif x < 0:
            pnz[1] += 1
        else:
            pnz[2] += 1
            
    for x in pnz:
        print("{:.6f}".format(x/denominator))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
