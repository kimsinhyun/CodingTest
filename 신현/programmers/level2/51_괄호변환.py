def func1(p):
    if not p:
        return "",""
    for i in range(1,len(p)+1):
        if(p[:i].count("(") == p[:i].count(")")):
            return p[:i] if p[:i] else "",p[i:] if p[i:] else ""
    return "",""

def func2(p):
    p = list(p)
    from collections import deque
    if p:
        stack = deque([p[0]])
        while p:
            if(p[0] == ")" and stack[-1] != "("):
                return False
            elif(p[0] == ")" and stack[-1] == "("):
                stack.popleft()
                p.pop(0)
            else:
                stack.append(p[0])
                p.pop(0)
        return True
    else:
        return False

def reverse_p(p):
    p = p.replace("(","t").replace(")","(").replace("t",")")
    return p

def solution(p):
    answer = ""
    test = "12345"
    if not p:
        return p
    u, v= func1(p)
    # print(f"u={u}, v={v}, answer={answer}")
    if func2(u):
        answer = u + solution(v)
    # print(answer)
    else:
        t1 = u[1:-1]
        t2 = "(" + solution(v) + ")"+ reverse_p(t1)
        answer += t2
    return answer

# test = solution("(()())()")
# test = solution("()))((()")

# print("test", test)