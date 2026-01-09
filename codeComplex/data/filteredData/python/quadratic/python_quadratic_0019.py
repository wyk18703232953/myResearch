def main(n):
    mod_v = 1000000007

    # Precompute Pascal triangle (binomial coefficients modulo mod_v)
    temp_arr = [[1]]
    for i in range(1, 1010):
        a = [1]
        for k in range(1, i):
            a.append((temp_arr[i - 1][k - 1] + temp_arr[i - 1][k]) % mod_v)
        a.append(1)
        temp_arr.append(a)

    # Precompute ans_arr using given recurrence
    ans_arr = [1]
    for i in range(1, 1010):
        res = 0
        for j in range(i):
            res += ans_arr[j] * temp_arr[i - 1][j]
            res %= mod_v
        ans_arr.append(res)

    # Deterministic data generation
    # Interpret n as the number of columns (original `n`)
    # and set number of "lines" proportional to n but capped by 30 for bit operations
    cols = n
    if cols <= 0:
        # print(1)
        pass
        return

    lines = min(30, max(1, n))

    # Generate a deterministic binary matrix of size lines x cols
    # Each entry is either 0 or 1, defined deterministically by (i + 3 * k) % 2
    new_list = [0 for _ in range(cols)]
    for i in range(lines):
        row = [((i + 3 * k) % 2) for k in range(cols)]
        for k in range(cols):
            new_list[k] |= row[k] << i

    from collections import defaultdict
    default_d = defaultdict(int)
    for k in new_list:
        default_d[k] += 1

    answer = 1
    for cnt in default_d.values():
        if cnt < len(ans_arr):
            answer = answer * ans_arr[cnt] % mod_v

        else:
            # Extend ans_arr deterministically if needed (rare for small n)
            # though with our settings cnt will never exceed 1010
            res = 0
            i = len(ans_arr)
            while i <= cnt:
                res = 0
                for j in range(i):
                    res += ans_arr[j] * temp_arr[i - 1][j]
                    res %= mod_v
                ans_arr.append(res)
                i += 1
            answer = answer * ans_arr[cnt] % mod_v

    # print(answer)
    pass
if __name__ == "__main__":
    main(10)