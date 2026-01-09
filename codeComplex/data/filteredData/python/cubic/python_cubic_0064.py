def main(n):
    # deterministically generate a string of length n over a small alphabet
    alphabet = "abc"
    s = ''.join(alphabet[i % len(alphabet)] for i in range(n))

    ans = 0
    m = set()
    for i in range(len(s)):
        for j in range(i, -1, -1):
            substr = s[j:i+1]
            if substr in m:
                if i - j + 1 > ans:
                    ans = i - j + 1

            else:
                m.add(substr)
    # print(ans)
    pass
if __name__ == "__main__":
    main(1000)