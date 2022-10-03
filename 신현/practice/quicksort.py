
def quicksort(arr):
    if(len(arr) <2):
        return arr
    
    pivot_idx = len(arr)//2
    left_idx = 0
    right_idx = len(arr)-1
    pivot_val = arr[pivot_idx]
    print()
    print(f"pivot_val = {pivot_val}")
    while((left_idx < right_idx)):
        print(f"l: {arr[left_idx]} ; r: {arr[right_idx]}")
        if(arr[left_idx] >= arr[pivot_idx]):
            if(arr[right_idx] < arr[pivot_idx]):
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx] 
                print("swap")
            else:
                right_idx-=1
        else:
            left_idx += 1
        print(arr)
    print(f"left_list  = {arr[:right_idx]}")
    print(f"right_list = {arr[left_idx:]}")
    return quicksort(arr[:right_idx]) + quicksort(arr[left_idx:]) 
    
if __name__ == '__main__':
    arr = [10, 50, 30, 20, 40, 42, 12, 45]
    test = quicksort(arr)
    print(test)