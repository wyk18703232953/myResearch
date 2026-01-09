def main(n):
    # Generate n triplets of strings (t1, t2, t3) deterministically
    # Each token is of form "<digit><char>", digit in 0-9, char in ['a','b','c']
    chars = ['a', 'b', 'c']
    results = []

    # Precompute aaa once since it does not depend on input
    aaa = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                if k - j == j - i == 1:
                    aaa.append({i, j, k})

    for case_idx in range(n):
        # Deterministically construct three tokens
        # Vary digits and chars with simple arithmetic on case_idx
        d1 = case_idx % 10
        d2 = (case_idx // 2) % 10
        d3 = (case_idx // 3) % 10

        c1 = chars[case_idx % 3]
        c2 = chars[(case_idx // 2) % 3]
        c3 = chars[(case_idx // 3) % 3]

        t1 = str(d1) + c1
        t2 = str(d2) + c2
        t3 = str(d3) + c3

        ans = 2
        if t1 == t2 or t2 == t3 or t3 == t1:
            if t1 == t2 == t3:
                ans = 0

            else:
                ans = 1

        if t1[1] == t2[1] == t3[1] and {int(t1[0]), int(t2[0]), int(t3[0])} in aaa:
            ans = 0
        elif (
            (t1[1] == t2[1] and (abs(int(t1[0]) - int(t2[0])) == 1 or abs(int(t1[0]) - int(t2[0])) == 2))
            or (t1[1] == t3[1] and (abs(int(t1[0]) - int(t3[0])) == 1 or abs(int(t1[0]) - int(t3[0])) == 2))
            or (t3[1] == t2[1] and (abs(int(t3[0]) - int(t2[0])) == 1 or abs(int(t3[0]) - int(t2[0])) == 2))
        ):
            ans = min(1, ans)

        results.append(ans)

    # For time-complexity experiments, we ensure some output that depends on work
    # Print the last result (or 0 if n == 0)
    # print(results[-1] if results else 0)
    pass
if __name__ == "__main__":
    # Example fixed-scale call; adjust n for experiments
    main(1000)