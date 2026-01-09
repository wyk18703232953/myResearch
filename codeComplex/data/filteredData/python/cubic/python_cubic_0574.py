def main(n):
    # Generate two digit sequences a and b based on n.
    # a and b are lists of digits (0-9). Lengths depend on n.
    # This generation is fully deterministic and uses no external input.
    if n <= 0:
        return

    # Define lengths of a and b from n
    len_a = n
    len_b = n

    # Deterministically generate digits for a and b
    a = [((i * 3 + 1) % 10) for i in range(len_a)]
    b = [((i * 5 + 2) % 10) for i in range(len_b)]

    # Core logic from original program (unchanged except for using generated a, b)
    if len(a) < len(b):
        a.sort(reverse=True)
        ans = 0
        for i in range(len(a)):
            ans = ans * 10 + a[i]
        # print(ans)
        pass

    else:
        ans = 0
        n_len = len(a)
        count = [0] * 10
        for i in range(n_len):
            count[a[i]] += 1
        i = 0
        while i < n_len:
            x = b[i]
            if count[x] > 0:
                ans = ans * 10 + x
                count[x] -= 1
                i += 1

            else:
                break
        if i == n_len:
            # print(ans)
            pass
            return
        x = b[i]
        flag = False
        for j in range(x - 1, -1, -1):
            if count[j] > 0:
                ans = ans * 10 + j
                count[j] -= 1
                flag = True
                break
        if flag:
            for j in range(9, -1, -1):
                while count[j] > 0:
                    ans = ans * 10 + j
                    count[j] -= 1

        else:
            while not flag:
                t = ans % 10
                ans = ans // 10
                count[t] += 1
                for k in range(t - 1, -1, -1):
                    if count[k] > 0:
                        count[k] -= 1
                        flag = True
                        ans = ans * 10 + k
                        break
            for j in range(9, -1, -1):
                while count[j] > 0:
                    ans = ans * 10 + j
                    count[j] -= 1
        # print(ans)
        pass
if __name__ == "__main__":
    # Example deterministic call; adjust n for different input scales
    main(10)