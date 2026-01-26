def main(n):
    # Generate a deterministic string of length n using a simple pattern
    if n <= 0:
        # print(0)
        pass
        return
    s = ['b' if i % 2 == 0 else 'w' for i in range(n)]

    ans = 0
    far = 0
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            far += 1
            continue
        if s[0] != s[-1]:
            s[:i + 1] = s[:i + 1][::-1]
            s[i + 1:] = s[i + 1:][::-1]
            far += 1

        else:
            ans = max(ans, far + 1)
            far = 0
    # print(max(far + 1, ans))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)