def solution(s):
    answer = []
    s_list = list(map(int,s.replace("{","").replace("}","").split(",")))
    temp_set = set(s_list)
    temp_dict = dict()
    for i in temp_set:
        temp_dict[i] = s_list.count(i)
    temp_dict = dict(sorted(temp_dict.items(), key=lambda x: x[1], reverse=True))
    # print(list(temp_dict.keys()))
    answer = list(temp_dict.keys())
    return answer