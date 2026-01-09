def main(n):
    # Deterministically generate input string x of length n
    # Pattern: repeating lowercase letters 'a' to 'z'
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    x = "".join(chars)

    l = len(x)
    m = 0
    for i in range(l - 1):
        f = i
        while True:
            idx = x[f + 1:].find(x[f])
            if idx == -1:
                break

            else:
                idx += f + 1
                c = 0
                ans = 0
                for j in range(idx, l):
                    if x[j] == x[i + c]:
                        ans += 1
                        c += 1

                    else:
                        break
                if m < ans:
                    m = ans
                f = idx
    # print(m)
    pass
if __name__ == "__main__":
    main(1000)