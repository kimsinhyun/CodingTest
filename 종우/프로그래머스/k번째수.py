# 0226
# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        start, end, id = command
        part = array[start-1: end]
        part.sort()
        answer.append(part[id-1])
    return answer