# 1005_2.py
# 이진 변환 반복하기
# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnv = 0
    rm = 0
    while(s != "1"):
        rm += s.count("0")
        s = s.replace("0","")
        s = bin(len(s))[2:]
        cnv += 1
    
    answer = [cnv, rm]
    return answer