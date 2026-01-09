def main(n):
    # Deterministically generate a string of length n over lowercase letters
    s = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    ans = 0
    sLen = len(s)

    for i in range(sLen):
        for till1 in range(i + 1, sLen + 1):
            till2 = till1 + 1
            for j in range(i + 1, sLen + 1):
                if till2 > sLen:
                    break
                sub1 = s[i:till1]
                sub2 = s[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                till2 += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)