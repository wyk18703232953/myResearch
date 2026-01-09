def main(n):
    # Generate a deterministic string s mimicking the original expected format "dX dX dX"
    # where d is a digit and X is a lowercase letter.
    # Length is fixed at 8: "a1 b2 c3" style, but deterministically from n.
    # To make it scalable in terms of processing, we will call func multiple times.
    digits = [(n + i) % 10 for i in range(3)]
    chars = [chr(ord('a') + (n + i) % 26) for i in range(3)]
    # construct s as "d0c0 d1c1 d2c2"
    s = "{}{} {}{} {}{}".format(digits[0], chars[0], digits[1], chars[1], digits[2], chars[2])

    s1 = s[0:2]
    s2 = s[3:5]
    s3 = s[6:8]

    def func(inp, s_local):
        ans_local = 2
        num = int(inp[0])
        c = inp[1]
        ans_local = min(
            ans_local,
            2
            - int(s_local.find(str(num + 1) + c) != -1)
            - int(s_local.find(str(num + 2) + c) != -1),
        )
        ans_local = min(
            ans_local,
            2
            - int(s_local.find(str(num + 1) + c) != -1)
            - int(s_local.find(str(num - 1) + c) != -1),
        )
        ans_local = min(
            ans_local,
            2
            - int(s_local.find(str(num - 1) + c) != -1)
            - int(s_local.find(str(num - 2) + c) != -1),
        )
        ans_local = min(ans_local, 3 - s_local.count(inp))
        return ans_local

    # To scale with n, repeat the core logic n times and aggregate.
    # This keeps the algorithm intact but increases work proportionally to n.
    ans = 2
    for _ in range(max(1, n)):
        ans = min(ans, func(s1, s))
        ans = min(ans, func(s2, s))
        ans = min(ans, func(s3, s))

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)