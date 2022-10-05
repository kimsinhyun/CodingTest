def solution(s):
    answer = True
    temp_flag = 0
    for ele in s:
        if(ele == "("):
            temp_flag+=1
        elif(ele == ")"):
            if(temp_flag == 0):
                return False
            else:
                temp_flag-=1
    if(temp_flag == 0):
        return True
    return False