def main(n):
    rgb = "RGB"
    # Interpret n as the length of string s; use a fixed k pattern based on n
    # Ensure k >=1 and <= n for meaningful computation
    if n <= 0:
        return
    k = max(1, n // 2)
    s = ''.join(rgb[i % 3] for i in range(n))

    q = 1  # single test case for scalability on n
    for _ in range(q):
        ans = n
        for i in range(3):
            r = [0]
            l = i
            for c in s:
                r.append(r[-1] + (1 if c != rgb[l] else 0))
                l = (l + 1) % 3
                if len(r) > k:
                    ans = min(ans, r[-1] - r[len(r) - 1 - k])
        # print(ans)
        pass
if __name__ == "__main__":
    main(10)