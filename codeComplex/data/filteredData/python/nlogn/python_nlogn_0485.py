import random

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
        else:
            last = a[i]
            count = 1
        i += 1
    return False


def main(n):
    # 生成规模为 n 的测试数据
    # 设 m 为元素个数，取 m = n * 5（可根据需要调整）
    m = n * 5
    # 随机生成若干整数，范围 1~n
    a = [random.randint(1, n) for _ in range(m)]

    a.sort()
    l = 1
    h = m
    ans = 0

    while l <= h:
        mid = (l + h) // 2
        if isValid(mid, a, n, m):
            ans = mid
            l = mid + 1
        else:
            h = mid - 1

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    main(10)