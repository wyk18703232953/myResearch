def main(n):
    # Generate a deterministic string of length n using lowercase letters
    if n <= 0:
        # print(0)
        pass
        return
    letters = "abcdefghijklmnopqrstuvwxyz"
    s = "".join(letters[i % len(letters)] for i in range(n))

    slen = len(s)
    ans = 0
    for st1 in range(slen - 1):
        for end1 in range(st1 + 1, slen):
            end2 = end1 + 1
            sub1 = s[st1:end1]
            for st2 in range(st1 + 1, slen):
                if end2 > slen:
                    break
                sub2 = s[st2:end2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                end2 += 1
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)