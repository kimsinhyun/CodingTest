word_list = []
dic = "AEIOU"
def all_words(cnt, w):
    global word_list
    if cnt == 5:
        return
    for i in range(len(dic)):
        word_list.append(w + dic[i])
        all_words(cnt+1,w+dic[i])
def solution(word):
    all_words(0,"")
    return word_list.index(word)+1
