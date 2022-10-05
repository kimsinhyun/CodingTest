def length_no_problem(word):
    return (len(word) >= 2) and (len(word) <= 50)

def solution(n, words):
    answer = [0,0]
    already_words = [words[0]]
    lastChar = words[0][-1]
    for i in range(1, len(words)):
        if(lastChar != words[i][0]) or (words[i] in already_words) or (len(words[i]) < 2) or (len(words[i]) > 50):
            return [i%n+1, int(i/n)+1]
        already_words.append(words[i])
        lastChar = words[i][-1]
    return [0, 0]