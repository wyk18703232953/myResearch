def main(n):
    # Interpret n as original input parameter n; fix d and k as deterministic functions of n
    # to provide a scalable input size. This preserves the original algorithm structure.
    #
    # You can adjust these mappings if you want different scaling behavior, but they must
    # remain deterministic and only depend on n.
    orig_n = max(1, n)                # ensure positive
    d = max(1, orig_n // 2)           # example: diameter-like parameter
    k = max(1, min(10, orig_n // 3))  # example: branching factor, capped

    n_val, d_val, k_val = orig_n, d, k

    l = []
    i = 1
    if n_val <= d_val:
        # print("NO")
        pass
    elif k_val == 1:
        if n_val > 2:
            # print("NO")
            pass
        elif n_val == 2:
            # print("YES")
            pass
            # print(1, 2)
            pass

    else:
        n_val += 1
        flag = False
        while i < min(d_val + 1, n_val):
            l.append(str(i) + " " + str(i + 1))
            i += 1
        i += 1
        cnt1 = 0
        cnt2 = 1
        se = [[2, d_val + 1, 1]]
        while cnt1 < cnt2:
            start = se[cnt1][0]
            end = se[cnt1][1]
            mode = se[cnt1][2]
            kk = 3
            while (i < n_val) and (kk <= k_val):
                if i < n_val and not flag:
                    j = start
                    while i < n_val and j < end:
                        if mode == 1:
                            c = min(j - start + 1, end - j)

                        else:
                            c = min(end - j, d_val - end + j)
                        if c > 1:
                            se.append([i, i + c - 1, 2])
                            cnt2 += 1
                        ki = j
                        while i < n_val and c > 0:
                            l.append(str(ki) + " " + str(i))
                            c -= 1
                            ki = i
                            i += 1
                        j += 1

                else:
                    flag = True
                    break
                kk += 1
            cnt1 += 1
        if i < n_val or flag:
            # print("NO")
            pass

        else:
            # print("YES")
            pass
            # print('\n'.join(l))
            pass
if __name__ == "__main__":
    # Example deterministic calls for experimentation
    main(5)
    main(10)
    main(20)