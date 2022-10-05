answer = []
words = ["A","E","I","O","U"]
def all_words(cnt, w):
    if cnt == 5:
        return 
    for i in range(len(words)):
        answer.append(w + words[i])
        all_words(cnt+1, w + words[i])

def solution(word):
    all_words(0,"")
    return answer.index(word)+1