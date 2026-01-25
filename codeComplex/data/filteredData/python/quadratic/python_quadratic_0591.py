def main(n):
    # Interpret n as the length of the string s; keep a fixed k relative to n.
    if n <= 0:
        return
    # Choose k as max(1, n // 2) to ensure 1 <= k <= n
    k = max(1, n // 2)

    # Deterministically build a string of length n over 'R', 'G', 'B'
    chars = ['R', 'G', 'B']
    s = ''.join(chars[i % 3] for i in range(n))

    a = k
    for j in range(n - k + 1):
        a1, a2, a3 = 0, 0, 0
        for jj in range(k):
            ch = s[j + jj]
            mod = jj % 3
            if mod == 0:
                if ch == "R":
                    a2 += 1
                    a3 += 1
                elif ch == "G":
                    a1 += 1
                    a3 += 1
                else:
                    a1 += 1
                    a2 += 1
            elif mod == 1:
                if ch == "R":
                    a1 += 1
                    a2 += 1
                elif ch == "G":
                    a2 += 1
                    a3 += 1
                else:
                    a3 += 1
                    a1 += 1
            else:
                if ch == "R":
                    a1 += 1
                    a3 += 1
                elif ch == "G":
                    a1 += 1
                    a2 += 1
                else:
                    a3 += 1
                    a2 += 1
        a = min(a, a1, a2, a3)
    print(a)


if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(20)