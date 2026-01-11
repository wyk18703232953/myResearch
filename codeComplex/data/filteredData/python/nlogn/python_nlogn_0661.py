def main(n):
    # Deterministic data generation based on n
    # Generate L of length n with values in range [-n, n]
    # Ensure mix of positives and non-positives
    L = [((i * 37) % (2 * n + 1)) - n for i in range(1, n + 1)]

    D = {}
    J = []
    S = []
    T = [0] * (n + 1)
    for i in range(n):
        if L[i] > 0:
            D[L[i]] = i
            J.append(L[i])
            T[i + 1] = T[i]

        else:
            T[i + 1] = T[i] + 1

    def I(J_list):
        if len(J_list) <= 1:
            return J_list, 0

        else:
            a = J_list[: len(J_list) // 2]
            b = J_list[len(J_list) // 2 :]
            a, ai = I(a)
            b, bi = I(b)
            c = []
            i = 0
            j = 0
            inversions = ai + bi
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    c.append(a[i])
                    i += 1

                else:
                    c.append(b[j])
                    j += 1
                    inversions += len(a) - i
            c += a[i:]
            c += b[j:]
            return c, inversions

    for i in range(1, n + 1):
        if i not in D:
            S.append(i)

    total = len(S)
    num = 1
    denom = 1
    if total > 0:
        themostimportantsum = 0
        for val in J:
            low = 0
            high = total - 1
            while high - low > 1:
                guess = (high + low) // 2
                if S[guess] > val:
                    high = guess

                else:
                    low = guess
            if S[low] > val:
                smaller = low
            elif S[high] > val:
                smaller = high

            else:
                smaller = high + 1
            themostimportantsum += (
                T[D[val]] * (total - smaller)
                + (total - T[D[val]]) * (smaller)
            )
            num = themostimportantsum + total
            denom = total

    num = (denom * (((total) * (total - 1)) // 2) + 2 * num) % 998244353
    denom *= 2
    if num == denom:
        if I(J)[1] == 0:
            # print(0)
            pass

        else:
            # print(I(J)[1] % 998244353)
            pass

    else:
        num += denom * I(J)[1]
        print(
            ((num - denom) * pow(denom % 998244353, 998244351, 998244353))
            % 998244353
        )


if __name__ == "__main__":
    main(1000)