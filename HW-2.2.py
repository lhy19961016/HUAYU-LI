def Mostpopular(artical):
    n = 0
    res = []
    for i in range(len(artical)-1):
        if (not (ord(artical[i])>= 97 and ord(artical[i]) <= 122)or (ord(artical[i]) >= 65 and ord(artical[i]) <= 90)):
            if i > n:
                res.append(artical[n:i])
            n = i+1

    if ((ord(artical[-1]) >= 97 and ord(artical[-1]) <= 122) or (ord(artical[-1]) >=65 and ord(artical[-1]) <=90)):
        res.append(artical[n:])

        for j in range(len(res) - 1):
            for k in range(len(res)-j-1):
                if(res.count(res[k]) < res.count(res[k+1])):
                    temp = res[k]
                    res[k] = res[k+1]
                    res[k+1] = temp
    return res[0]

if __name__ == "__main__":
    artical=" cccccccccccccccccccccccccccccccccc can can but can not can things can't be canned"
    print(Mostpopular(artical))
