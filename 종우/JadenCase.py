# JadenCase 문자열 만들기
# 10.03
# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    a = s.lower()
    if a[0].isalpha():
        a = a[0].upper() + a[1:]
    for i in range(1, len(a)):
        if a[i].isalpha() and a[i-1] == " ":
            a = a[:i] + a[i].upper() + a[i+1:]
    return a

# return s.title()
# 내장함수 하나로 풀 수 있음.. ㅋㅋㅋ