def solution(s):
    result = ''
    
    # 공백 한 칸을 기준으로 split
    # 공백이 2개 이상 연속으로 나올 경우 나머지 공백은 i가 될 수 있음
    for i in s.split(' '):
        
        # i가 공백일 때 공백 추가
        if len(i) == 0:
            result += ' '
        
        # i의 첫 문자가 숫자일 때, i를 모두 소문자로 변환 후 구분 공백 추가
        elif i[0].isdigit():
            result += i.lower()
            result += ' '
        
        # i의 첫 문자가 알파벳일 때, 첫 문자는 대문자로 그 이후는 소문자로 변환 후 구분 공백 추가
        else:
            result += (i[0].upper() + i[1:].lower())
            result += ' '

    return result[:-1]