# 0208_2
# https://school.programmers.co.kr/learn/courses/30/lessons/17686


# 내 풀이
def solution(files):
    # divide filename into parts
    dig = ["0", "1", "2", "3", "4", "5", "6", "7","8","9"]
    divfiles = []
    for j, file in enumerate(files):
        num = False
        strpart = ''
        intpart = ''
        for i in range(len(file)):
            c = file[i]
            if not num:
                if c not in dig:
                    strpart += c
                else:
                    intpart += c
                    num = True
            else:
                if c in dig:
                    intpart += c
                else:
                    break
        divfiles.append((strpart.lower(), int(intpart), j))
    
    # order files
    divfiles.sort(key=lambda x : x[1])
    divfiles.sort(key=lambda x : x[0])
    
    answer = [files[k[2]] for k in divfiles]
    return answer


# 다른 풀이 regex
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b