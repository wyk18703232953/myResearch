def main(n):
    # Generate a deterministic string of length n based on simple arithmetic pattern
    # Pattern: cyclic lowercase letters 'a' to 'z'
    inputS = ''.join(chr(ord('a') + (i % 26)) for i in range(n))

    ans = 0
    length = len(inputS)

    for i in range(0, length - 1):
        for count in range(1, length):
            for j in range(i + 1, length - count + 1):
                A = inputS[i: i + count]
                B = inputS[j: j + count]
                if A == B:
                    ans = count if count > ans else ans

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)