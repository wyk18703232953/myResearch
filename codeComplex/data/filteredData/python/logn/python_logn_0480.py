def main(n):
    from bisect import bisect_left as bsl

    # Precompute arrays as in original code
    cur = 9
    count = 1
    tot = 0
    num = []
    cc = []
    for _ in range(11):
        num.append(cur * count)
        tot += cur
        cc.append(tot)
        cur *= 10
        count += 1

    ans = [num[0]]
    for s in range(1, 11):
        ans.append(ans[-1] + num[s])

    # Deterministically generate k from n (scale with n)
    # Ensure k >= 1
    if n <= 0:
        k = 1

    else:
        # Make k grow roughly linearly with n but stay within a reasonable bound
        k = n * 10

    ind = min(bsl(ans, k), 10)
    left = k
    if ind > 0:
        left -= ans[ind - 1]

    nums = left // (ind + 1)
    rem = left % (ind + 1)
    if left % (ind + 1) != 0:
        nums += 1
    if ind > 0:
        nums += cc[ind - 1]

    answer = [int(ch) for ch in str(nums)]
    # For rem == 0 in original logic, it would index answer[-1]
    # Maintain same behavior:
    if rem == 0:
        idx = -1

    else:
        idx = rem - 1

    # print(answer[idx])
    pass
if __name__ == "__main__":
    main(100000)