def main(n):
    # Generate a deterministic string of length n
    # Pattern: repeating lowercase letters 'a' to 'z'
    chars = [chr(ord('a') + (i % 26)) for i in range(n)]
    s = "".join(chars)

    n_len = len(s)
    m = n_len - 1
    while m > 0:
        find = False
        for i in range(0, n_len - m):
            for j in range(i + 1, n_len - m + 1):
                match = True
                for k in range(0, m):
                    if s[i + k] != s[j + k]:
                        match = False
                        break
                if match:
                    find = True
                    break
            if find:
                break
        if find:
            break
        m -= 1
    # print(m)
    pass
if __name__ == "__main__":
    main(1000)