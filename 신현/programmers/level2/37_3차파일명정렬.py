def h_n(f):
    head,num,tail = "","",""
    num_checked = False
    for i in range(len(f)):
        if f[i].isdigit():
            num+=f[i]
            num_checked = True
        elif not num_checked:
            head += f[i]
        else:
            tail=f[i:]
            break
    return head,num, tail
def solution(files):
    order_dic = []
    for i,f in enumerate(files):
        head,num,tail = h_n(f)
        order_dic.append((head,num,tail,i,f))
    order_dic = sorted(order_dic, key=lambda x: (x[0].lower(), int(x[1]), x[3]))
    answer = []
    for dic in order_dic:
        # answer.append("".join(dic))
        answer.append(dic[4])
    return answer