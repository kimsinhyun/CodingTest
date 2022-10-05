def remove_zero_and_transform_to_bin(s, num_1):
    for i in s:
        if(i == "0"):
            s=s.replace(i,"")
            num_1 += 1
    temp_len = len(s)
    s = str(bin(int(temp_len)))[2:]
    return num_1, s

def solution(s):
    answer = []
    num_1 = 0
    num_2 = 0
    while len(s) != 1:
        num_1, s = remove_zero_and_transform_to_bin(s, num_1)
        num_2+=1
    return [num_2, num_1]
    # print(s)
    # print(num_1)
            
            
    # s=s.replace("0","")
    # print(s)
    return answer
