def main(n):
    # 映射规则：
    # n: 数组长度
    # m: 使用 n//2 作为限制值
    global a, m
    if n < 3:
        # 原逻辑在长度不足时不会进入主循环，直接输出 -1
        # print(-1)
        pass
        return

    m = n // 2
    # 构造严格递增数组 a，满足 a[i+1] > a[i]
    # 使用确定性构造：a[i] = i + i//2
    a = [i + (i // 2) for i in range(n)]

    def sss(l, r, tt):
        f = -1
        while l <= r:
            mid = (l + r) >> 1
            if a[mid] - a[tt] <= m:
                f = mid
                l = mid + 1

            else:
                r = mid - 1
        return f

    Maxx = -1.0
    length = len(a)
    for i in range(0, length - 2):
        if a[i + 2] - a[i] <= m:
            k = sss(i + 2, length - 1, i)
            if k != -1:
                val = (a[k] - a[i + 1]) / (a[k] - a[i])
                if val > Maxx:
                    Maxx = val

    if Maxx == -1:
        # print(-1)
        pass

    else:
        # print("%.15f" % Maxx)
        pass
if __name__ == "__main__":
    main(1000)