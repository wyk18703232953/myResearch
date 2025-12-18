def palin(s):
    global ans
    if (s[::-1] != s or len(s) == 0):
        return len(s)
    else:
        return palin(s[1:])
s = input()
print(palin(s))