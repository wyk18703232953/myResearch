def main(n):
    if n <= 0:
        # print(0)
        pass
        return
    base = "abc"
    s = "".join(base[i % len(base)] for i in range(n))
    length = len(s)
    Ans = 0
    for i in range(length):
        for j in range(i + 1, length):
            L = i
            R = j
            while L < R and s[L] == s[R]:
                L += 1
                R -= 1
            if L < R and Ans < j - i + 1:
                Ans = j - i + 1
    # print(Ans)
    pass
if __name__ == "__main__":
    main(10)