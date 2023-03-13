import sys

def main():
    #find the most frequent letters in the solution set
    sys.stdin = open('accepted_answers.txt', 'r')
    d = {i:0 for i in list('abcdefghijklmnopqrstuvwxyz')}
    pw = []
    for word in sys.stdin:
        word = word.rstrip().lower()
        pw.append(word)
        for letter in list(word):
            d[letter] += 1
    sols = []
    for i in pw:
        l = list(i)
        if 'h' == l[1] and 'a' == l[2] and l[4] == 'e':
            sols.append(i)
    print(sols)
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    ff = list(d)[:15]
    
    
    #finds a combination of 3 words accepted by wodle which together contain the 15 most common letters
    sys.stdin = open('all_words.txt', 'r')
    wds = []
    for word in sys.stdin:
        word = word.rstrip().lower()
        wds.append(word)

    tw = []
    for w in wds:
        if len(list(set(w))) != 5:
            continue
        else:
            tw.append(w)

    wds = tw
    par = []
    arr = []
    found = False
    for i in wds:
        #print(ff)
        cw = list(set(i))
        if len(set(ff).difference(set(cw))) != (len(ff) - 5):
            continue
        else:
            arr.append(i)
            ff = list(set(ff).difference(set(cw)))

        for j in wds:
            #print(ff)
            cw = list(set(j))
            if j == wds[-1] and len(set(ff).difference(set(cw))) != (len(ff) - 5):
                ff += list(arr[-1])
                arr.pop()
                break
            elif len(set(ff).difference(set(cw))) != (len(ff) - 5):
                continue
            else:
                arr.append(j)
                ff = list(set(ff).difference(set(cw)))

            for k in wds:
                #print(ff)
                cw = list(set(k))
                if k == wds[-1] and len(set(ff).difference(set(cw))) != (len(ff) - 5):
                    ff += list(arr[-1])
                    arr.pop()
                    break
                elif len(set(ff).difference(set(cw))) != (len(ff) - 5):
                    continue
                else:
                    arr.append(k)
                    ff = list(set(ff).difference(set(cw)))
                    found = True
                    break
            if found == True:
                break
        if found == True:
            break
    return arr
main()

