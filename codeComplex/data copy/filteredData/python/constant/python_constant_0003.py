def t_from_s_a_u(s, a, u):
    from math import sqrt
    return (-2 * u + sqrt(4 * u * u + 8 * s * a)) / (2 * a)


def solve(A, V, L, D, W):
    from math import sqrt
    if V <= W or W ** 2 >= 2 * A * D:
        if V ** 2 >= 2 * A * L:
            return sqrt(2 * L / A)

        else:
            dist_1 = (V ** 2) / (2 * A)
            T1 = 2 * dist_1 / V
            dist_2 = L - dist_1
            T2 = dist_2 / V
            return T1 + T2

    else:
        dist_1 = (W ** 2) / (2 * A)
        T1 = sqrt(2 * dist_1 / A)
        rem_dist = D - dist_1
        dist_A = (V ** 2 - W ** 2) / (2 * A)
        if 2 * dist_A >= rem_dist:
            TA = 2 * t_from_s_a_u(rem_dist / 2, A, W)

        else:
            TA1 = 2 * (V - W) / A
            SA1 = (V + W) * (V - W) / A
            SA2 = rem_dist - SA1
            TA2 = SA2 / V
            TA = TA1 + TA2
        T1 += TA
        if V ** 2 - W ** 2 >= 2 * A * (L - D):
            return T1 + t_from_s_a_u(L - D, A, W)

        else:
            dist_2 = (V ** 2 - W ** 2) / (2 * A)
            T2 = 2 * dist_2 / (V + W)
            dist_3 = L - D - dist_2
            T3 = dist_3 / V
            return T1 + T2 + T3


def main(n):
    # Interpret n as number of test cases.
    # For each test i (1-based), deterministically construct parameters:
    # A, V, L, D, W as simple functions of i and n.
    results = []
    for i in range(1, n + 1):
        # Ensure positive acceleration and distances/speeds
        A = (i % 5) + 1          # 1..5
        V = (i % 7) + 5          # 5..11
        L = (i * 10) + 50        # grows linearly with i
        D = max(1, (i * 7) % L)  # < L, at least 1
        W = (i % 9) + 3          # 3..11
        res = solve(A, V, L, D, W)
        results.append(res)
    # Aggregate to avoid huge output; print sum to keep work proportional to n
    total = 0.0
    for x in results:
        total += x
    # print(total)
    pass
if __name__ == "__main__":
    main(10)