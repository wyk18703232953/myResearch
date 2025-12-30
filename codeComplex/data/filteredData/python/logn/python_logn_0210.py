def getval(x: int) -> int:
    cur, ans = 0, 0
    while x:
        dig = x % 10
        ans += dig * cur
        cur *= 10
        cur += 9
        x //= 10
    return ans


def main(n: int):
    # 根据 n 生成测试数据，这里设定 s 为 n 的平方作为示例
    s = n * n

    low = 1
    high = n
    for _ in range(64):
        mid = (low + high) // 2
        if getval(mid) < s:
            low = mid + 1
        else:
            high = mid

    if low > high:
        print(0)
    elif getval(low) >= s:
        print(n - low + 1)
    else:
        print(n - high + 1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小
    main(10**6)