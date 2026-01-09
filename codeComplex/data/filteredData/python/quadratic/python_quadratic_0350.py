def main(n):
    # Generate deterministic test data
    # s and t are anagrams of each other to avoid early -1 termination
    # s: sequence of first n lowercase letters modulo 26
    # t: s rotated by 1 position to keep complexity similar to original algorithm
    import string

    letters = string.ascii_lowercase
    s = [letters[i % 26] for i in range(n)]
    t = s[1:] + s[:1] if n > 0 else []

    # Core logic from original program (adapted to generated s, t)
    if sorted(s) != sorted(t):
        # print(-1)
        pass
        return

    s = list(s)
    t = list(t)
    ans = []
    for i in range(n):
        for j in range(i, n - 1):
            if s[j + 1] == t[i]:
                for k in range(j, i - 1, -1):
                    ans.append(k + 1)
                    s[k + 1], s[k] = s[k], s[k + 1]
                break

    # print(len(ans))
    pass

    if ans:
        # print(*ans)
        pass
if __name__ == "__main__":
    # Example deterministic call for time complexity experiments
    main(10)