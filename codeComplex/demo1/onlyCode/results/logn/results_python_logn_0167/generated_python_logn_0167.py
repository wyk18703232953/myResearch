def prod(n):
    if n % 2:
        return n * ((n + 1) // 2)
    else:
        return (n // 2) * (n + 1)


def total_count(n, k):
    if k >= n:
        return (0, 0, 1)
    else:
        count = 0
        l = 1
        r = k
        s = prod(k)
        while l <= r:
            mid = (l + r) // 2
            if n > s - prod(mid) + mid:
                r = mid - 1
            else:
                l = mid + 1

        n = n - (s - prod(l) + l)
        count += (k - l + 1)
        k = l - 1
        return (n, k, count)


def main(n):
    # 生成与规模 n 相匹配的一组 (n, k) 测试数据
    # 这里简单设定 k = max(1, n // 2) 作为示例
    k = max(1, n // 2)

    if prod(k) - (k - 1) < n:
        return -1
    elif n == 1:
        return 0
    elif k >= n:
        return 1
    else:
        n = n - k
        k = k - 2
        count = 1
        while n > 0 and k > 0:
            n, k, temp = total_count(n, k)
            count += temp
        return count


if __name__ == "__main__":
    # 示例调用：可根据需要修改测试规模
    test_n = 10
    print(main(test_n))