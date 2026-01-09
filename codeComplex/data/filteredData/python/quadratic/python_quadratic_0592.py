def main(n):
    rgb = 'RGB' * (n + 5)
    # Interpret n as number of test cases
    T = n
    results = []
    for t in range(1, T + 1):
        # Deterministically generate n_t and k_t for each test
        nt = t + 2  # length of string, at least 3
        kt = max(1, nt // 2)  # window size
        # Generate deterministic test string s of length nt
        # pattern based on index to be deterministic and non-trivial
        chars = ['R', 'G', 'B']
        s = ''.join(chars[(i + t) % 3] for i in range(nt))
        ans = 3000
        for w in range(3):
            if nt < kt:
                break
            for e in range(nt - kt + 1):
                temp = 0
                for i in range(kt):
                    if s[e + i] != rgb[w + i]:
                        temp += 1
                if temp < ans:
                    ans = temp
        results.append(ans)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    main(5)