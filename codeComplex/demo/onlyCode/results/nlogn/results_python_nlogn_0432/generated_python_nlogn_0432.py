def main(n):
    import math
    s = [i % 1000 for i in range(n)]
    d = dict()
    for i in range(n):
        d[s[i]] = d.get(s[i], 0) + 1
    rem = 0
    for i in range(n):
        ok = False
        for j in range(31):
            x = 2 ** j - s[i]
            c = d.get(x, 0)
            if c > 1 or (c == 1 and s[i] != x):
                ok = True
                break
        if ok == False:
            rem += 1
    return rem

if __name__ == "__main__":
    print(main(10))