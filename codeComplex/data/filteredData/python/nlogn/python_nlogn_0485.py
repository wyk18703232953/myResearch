def isValid(k, a, n, m):
    last = a[0]
    count = 1
    step = 0
    i = 1
    if count == k and step + 1 == n:
        return True
    elif count == k:
        step += 1
        count = 1
    while i < m:
        if step == n:
            return True
        if count == k:
            step += 1
            count = 1
            if step == n:
                return True
            last = a[i]
        elif a[i] == last:
            count += 1
            if count == k and step + 1 == n:
                return True
        elif a[i] != last:
            last = a[i]
            count = 1
        i += 1
    return False


def main(n):
    # n 作为输入规模，这里映射为数组长度 m = n
    # 同时令模式长度参数 n_param 与原来的 n 含义相同
    m = n if n > 0 else 1
    n_param = max(1, n // 3)

    # 确定性数据构造：a 为长度 m 的整数数组
    # 构造有重复元素的序列，方便触发 isValid 的分组逻辑
    a = [(i // 2 + i // 3) % (max(1, n_param)) for i in range(m)]
    a.sort()

    l = 1
    h = m
    ans = 0
    while l <= h:
        mid = (l + h) // 2
        if isValid(mid, a, n_param, m):
            ans = mid
            l = mid + 1
        else:
            h = mid - 1
    print(ans)


if __name__ == "__main__":
    main(1000)