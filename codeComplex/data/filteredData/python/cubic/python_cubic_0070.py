def main(n):
    # Deterministically generate a string S of length n
    # Pattern chosen so that repeated substrings exist for any n >= 2
    # Example pattern: 'abcabcabc...' truncated to length n
    base = "abc"
    repeats = (n // len(base)) + 1
    S = (base * repeats)[:n]

    best = 0
    for i in range(len(S)):
        for j in range(i + 1, len(S) + 1):
            s = S[i:j]
            c = 0
            for k in range(len(S)):
                if S[k:].startswith(s):
                    c += 1
            if c >= 2:
                best = max(best, len(s))
    # print(best)
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)