# 0604
# https://school.programmers.co.kr/learn/courses/30/lessons/17683

# initial solve (incorrect)
def solution(m, musicinfos):
    answer = ''
    m = substitute(m)
    potential = []
    for mi in musicinfos:
        start, end, title, sheet = mi.split(',')
        # get time
        sh, sm = map(int, start.split(':'))
        eh, em = map(int, end.split(':'))
        time = (eh-sh)*60 + (em-sm)
        music = (time // len(sheet))*sheet + sheet[0:(time % len(sheet))]
        music = substitute(music)
        if m in music:
            potential.append([time, title])
    
    # print(potential)
    if potential:
        return max(potential)[1]
    return

def substitute(s):
    newString = ''
    for i in range(len(s)-1):
        if s[i+1] == '#':
            newString += chr(ord(s[i])+32)
        elif s[i] == '#':
            continue
        else:
            newString += s[i]
    newString += s[-1]
    return newString