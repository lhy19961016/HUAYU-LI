def phoneLetter(digs):
    if not digs:
        return []
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    if len(digs) == 0:
        return []
    if len(digs) == 1:
        return keyboard[digs]
    result = phoneLetter(digs[1:])
    for i in result:
        for j in keyboard[digs[0]]:
            res.append((j + i))
    return res

if __name__ =='__main__':
    print(phoneLetter("23"))
