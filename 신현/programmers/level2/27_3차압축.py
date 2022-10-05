def solution(msg):
    import string
    dic = list(string.ascii_uppercase)
    start = 0
    end = 1
    answer = []
    while True:
        if (end > len(msg)):
            answer.append(dic.index(msg[start:end-1])+1)
            break
        if msg[start:end] in dic:
            end += 1
        else:
            dic.append(msg[start:end])
            answer.append(dic.index(msg[start:end-1])+1)
            # print(msg[start:end])
            start=end-1
            end = start+1
    # print(f"start = {start} ; end={end} ; len={len(msg)}")
    # print(answer)
            
    
    return answer