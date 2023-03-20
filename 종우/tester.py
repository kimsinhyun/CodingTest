def solution(number, k):
    answer = ''
    nums = [int(i) for i in number]
    poten = [0] * len(number)
    for i, n in enumerate(nums):
        next = nums[i:]
        print(next)
        print(max(next))
    print(poten)
    
    return answer

solution('1924', 2)