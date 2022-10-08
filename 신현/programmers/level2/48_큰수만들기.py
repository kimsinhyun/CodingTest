def solution(number, k):
    stack = []
    for num in number:
        if not stack:
            stack.append(num)
            continue
        if k > 0:
            while stack[-1] < num:
                stack.pop()
                k -= 1
                if not stack or k <= 0:
                    break
        stack.append(num)
    print(k)
    stack = stack[:-k] if k > 0 else stack
    return "".join(stack)