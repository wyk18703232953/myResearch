def main(n):
    # Deterministically generate s from n
    # Ensure s is within feasible range: [2*n-1, n*(n+1)//2]
    min_s = 2 * n - 1
    max_s = n * (n + 1) // 2
    if min_s > max_s:
        # print("NO")
        pass
        return
    # Choose a deterministic s in the valid range
    # Example: middle of the valid interval
    s = (min_s + max_s) // 2

    # Core logic from original code, without any input() or sys.exit()
    if 2 * s > n * (n + 1) or s < 2 * n - 1:
        # print('NO')
        pass
        return

    for i in range(n, -1, -1):
        if i == 0:
            branch = 1
            break
        tmp = 0
        tmpn = n
        j = 1
        while tmpn - i ** (j - 1) >= 0:
            tmp += j * (i ** (j - 1))
            tmpn -= i ** (j - 1)
            j += 1
        tmp += j * (tmpn)
        if tmp > s:
            branch = i + 1
            break

    tmp = 0
    tmpn = n
    j = 1
    i = branch
    dic = {}
    while tmpn - i ** (j - 1) >= 0:
        tmp += j * (i ** (j - 1))
        dic[j] = i ** (j - 1)
        tmpn -= i ** (j - 1)
        j += 1
    tmp += j * (tmpn)
    dic[j] = tmpn
    maxi = j
    while tmp < s:
        for j in range(maxi, -1, -1):
            while dic.get(j, 0) > 1:
                if s - tmp + j <= maxi:
                    dic[j] -= 1
                    dic[s - tmp + j] = dic.get(s - tmp + j, 0) + 1
                    tmp = s

                else:
                    dic[j] -= 1
                    dic[maxi + 1] = dic.get(maxi + 1, 0) + 1
                    tmp += maxi + 1 - j
                    maxi += 1
                if tmp == s:
                    break
            if tmp == s:
                break

    b = []
    for i in dic:
        for _ in range(dic[i]):
            b.append(i)
    b.sort()
    # print('YES')
    pass
    children = [0] * n
    ans = [-1] * n
    curr = 0
    pointer = 0
    for i in range(1, n):
        while b[i] > b[curr] + 1:
            curr += 1
        ans[i] = curr
        children[curr] += 1
        if children[curr] == branch:
            curr += 1
    finans = []
    for i in range(1, n):
        finans.append(ans[i] + 1)
    # print(' '.join(map(str, finans)))
    pass
if __name__ == "__main__":
    # Example deterministic call; adjust n as needed for experiments
    main(10)