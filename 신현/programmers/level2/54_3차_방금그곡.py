def chkPlayTimeSame(lst):
    return len(set(lst)) == 1
def get_time(start, end):
    hs, ms = list(map(int, start.split(":")))
    he, me = list(map(int, end.split(":")))
    h, m = he-hs, me-ms
    return (h*60 + m)
def preprocess_sound(sound, time, is_input=True):
    result = []
    idx = 0
    while idx < len(sound):
        if idx < len(sound)-1:
            if sound[idx+1] != "#":
                result.append(sound[idx])
                idx += 1 
            else:
                result.append(sound[idx:idx+2])
                idx += 2
        else:
            result.append(sound[idx])
            idx+=1
    if is_input:
        return result
    times = time // len(result) 
    left  = time % len(result)
    result = result * times + result[:left]
    return result

def m_in_sound(m,sound):
    for i in range(len(sound)-len(m)+1):
        # print("i", i)
        # print(f"test m={m} sound[i:i+len(m)]={sound[i:i+len(m)]}")
        if sound[i:i+len(m)] == m:
            return True
    return False
def solution(m, musicinfos):
    # 1. 멜로디는 음악 끝부분과 처음 부분이 이어서 재생된 멜로디일 수도 있다. 
    # 2. 반대로, 한 음악을 중간에 끊을 경우 원본 음악에는 네오가 기억한 멜로디가 들어있다 해도 그 곡이 네오가 들은 곡이 아닐 수도 있다.
    answer = []
    for info in musicinfos:
        start, end, title, sound = info.split(",")
        time = get_time(start, end)
        m = preprocess_sound(m, time,is_input=True)
        sound = preprocess_sound(sound, time,is_input=False)
        # print(f"m={m}")
        # print(f"sound={sound}")
        if m_in_sound(m,sound) == True:
            answer.append([title, time])
    if answer:
        temp = sorted(answer, key=lambda x: (x[1]) , reverse=True)
        test = [y for x,y in temp]
        if chkPlayTimeSame(test):
            return answer[0][0]
        return temp[0][0]
    if not answer:
        return "(None)"
        
    
# m ="CC#BCC#BCC#"
# musicinfos = ["03:00,03:08,FOO,CC#B"]
# test = solution(m,musicinfos)
# print(test)