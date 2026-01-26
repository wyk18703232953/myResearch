def main(n):
    # Generate a deterministic string of length n over a small alphabet
    # Example pattern: repeating "abc"
    base = "abc"
    s = "".join(base[i % len(base)] for i in range(n))
    n = len(s)
    m = n - 1
    while m > 0:
        find = False
        for i in range(0, n - m):
            for j in range(i + 1, n - m + 1):
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
    # Example deterministic call; adjust n as needed for experiments
    main(1000)