arr = [10, 50, 30, 20, 40, 42, 12, 45]

def merge_sort(arr):
    print(len(arr))
    if(len(arr) < 2):
        return arr
    mid = len(arr)//2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])
    print(f"left_list: {left_list}")
    print(f"right_list: {right_list}")
    sorted_list = []
    left_idx, right_idx = 0,0
    while((left_idx < len(left_list)) and (right_idx < len(right_list))):
        if(left_list[left_idx] < right_list[right_idx]):
            sorted_list.append(left_list[left_idx])
            left_idx +=1
        else:
            sorted_list.append(right_list[right_idx])
            right_idx +=1
    sorted_list += left_list[left_idx:]
    sorted_list += right_list[right_idx:]
    print(f"sorted_list: {sorted_list}")
    return sorted_list
            
test = merge_sort( arr)
print(test)