def compress(s):
    temp = ""
    cnt = 0
    result = ""

    for c in s:
        if c != temp:
            temp = c
            if cnt:
                result += str(cnt)
            result += c
            cnt = 1
        else:
            cnt += 1
    result += str(cnt)
    return result

words = input("입력 :")
print("출력 : %s" % compress(words))