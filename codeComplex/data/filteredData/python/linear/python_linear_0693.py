def main(n):
    # 根据原程序输入结构，构造确定性数据：
    # 原输入: n, v
    # 这里令 v = n // 2，保证 0 <= v <= n
    v = n // 2

    ans = min(v, n - 1)
    # 原循环: for i in range(n - v - 1):
    loop_count = n - v - 1
    if loop_count > 0:
        for i in range(loop_count):
            ans += i + 2
    print(ans)


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 的规模
    main(10)