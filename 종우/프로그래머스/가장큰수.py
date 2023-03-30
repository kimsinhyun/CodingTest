# 가장 큰 수
# 10.03
# https://school.programmers.co.kr/learn/courses/30/lessons/42746

# 내가 푼 최대
import itertools
def solution(numbers):
    answer = 0
    largest = []
    # sort each number into starting digit
    digs = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
    poten = [str(x) for x in numbers]
    for dig in poten:
        if dig == "0":
            largest.append("0")
            continue
        digs[int(dig[0])].append(dig)
    
    # get largest from each dig
    for each in digs.values():
        if len(each) == 0: continue
        eachmax = maxpermute(each)
        largest.append(eachmax)
    largest.sort(reverse=True)
    return ''.join(largest)

def maxpermute(numbers):
    answer = 0
    for subset in itertools.permutations(numbers, len(numbers)):
        if int("".join(subset)) > answer:
            answer = int("".join(subset))
    return str(answer)

print(solution([6, 10, 2]))
print(solution([69, 420, 7, 88, 6, 60]))
print(solution([65, 420, 7, 88, 6, 60]))

# 정답 확인
def solution(numbers):
    # 숫자들 문자열로 바꿈
    numbers = list(map(str, numbers)) 
    # 모든 수 3번 반복, 이건 정렬을 위해
    # !스트링의 경우 내림차순으로 정렬한 것! 
    # 예)
    # 69, 6, 60 -> 696969>666>606060
    # 65, 6, 60 -> 666>656565>606060
    numbers.sort(key=lambda x: x*3, reverse=True) 
    # 문자열로 합치고 -> 정수 변환 -> 문자열 변환 
    # 앞에 0 붙거나 비정상 정수때매
    return str(int(''.join(numbers)))
