def main(n):
    # Generate a deterministic string s of length n consisting of 'H' and 'T'
    # Pattern: even indices -> 'H', odd indices -> 'T'
    s = ''.join('H' if i % 2 == 0 else 'T' for i in range(n))

    hc, tc = s.count('H'), s.count('T')

    # Edge cases: if no 'H' or no 'T', the replacement cost is 0
    if hc == 0 or tc == 0:
        print(0)
        return

    hr = min(s[i:i + hc].count('T') for i in range(n - hc + 1))
    tr = min(s[i:i + tc].count('H') for i in range(n - tc + 1))
    print(min(hr, tr))


if __name__ == "__main__":
    # Example call with a specific n for reproducible experiment
    main(10)