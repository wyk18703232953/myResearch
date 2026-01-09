def main(n):
    # Deterministic data generation based on n
    # We'll construct ans as a simple sequence, then generate l and r from ans
    ans = [i % (n // 2 + 1) for i in range(n)]

    l = [0] * n
    r = [0] * n

    # Compute l[i]: number of elements greater than ans[i] on the left
    for i in range(n):
        count = 0
        for j in range(i - 1, -1, -1):
            if ans[i] < ans[j]:
                count += 1
        l[i] = count

    # Compute r[i]: number of elements greater than ans[i] on the right
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if ans[i] < ans[j]:
                count += 1
        r[i] = count

    # Now run the original logic using generated l, r, n
    slr = [l[i] + r[i] for i in range(n)]
    ans_calc = [n - slr[i] for i in range(n)]

    flag = True
    if l[0] != 0 or r[n - 1] != 0:
        flag = False

    for i in range(n):
        great = 0
        for j in range(i + 1, n):
            if ans_calc[i] < ans_calc[j]:
                great = great + 1
        if r[i] != great:
            flag = False
            break

    for i in range(n - 1, -1, -1):
        great = 0
        for j in range(i - 1, -1, -1):
            if ans_calc[i] < ans_calc[j]:
                great = great + 1
        if l[i] != great:
            flag = False
            break

    if flag:
        # print("YES")
        pass

        if n > 0:
            for i in range(0, n - 1):
                # print(ans_calc[i], end=" ")
                pass
            # print(ans_calc[n - 1])
            pass

        else:
            # print()
            pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(10)