def repeat(s):
    prefix_array=[]
    for i in range(len(s)):
        prefix_array.append(s[:i])
    #see what it holds to give you a better picture
    print(prefix_array)

    #stop at 1st element to avoid checking for the ' ' char
    for i in prefix_array[:1:-1]:
        if s.count(i) > 1 :
            #find where the next repetition starts
            offset = s[len(i):].find(i)

            return s[:len(i)+offset]
            break

    return s


print (repeat("aabcba"))