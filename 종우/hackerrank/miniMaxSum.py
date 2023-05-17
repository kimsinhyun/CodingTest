# 0517

def miniMaxSum(arr):
    total = sum(arr)
    smallest = 1e10
    largest = 0
    for x in arr:
        tmp = total - x
        if tmp > largest:
            largest = tmp
        if tmp < smallest:
            smallest = tmp
    print(f"{smallest} {largest}")
            
            

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
