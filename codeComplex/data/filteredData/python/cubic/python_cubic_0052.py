def main(n):
    # Deterministically generate input string S of length n
    # Pattern: repeating lowercase letters 'a' to 'z'
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    S = "".join(alphabet[i % 26] for i in range(n))

    sLen, ans = len(S), 0
    for i in range(sLen):
        for till1 in range(i + 1, sLen):
            till2 = till1 + 1
            for j in range(i + 1, sLen):
                if till2 > sLen:
                    break
                sub1 = S[i:till1]
                sub2 = S[j:till2]
                subLen = len(sub1)
                if sub1 == sub2 and ans < subLen:
                    ans = subLen
                till2 += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)