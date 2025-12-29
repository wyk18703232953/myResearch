def main(n):
    # 生成测试数据：
    # 1 <= l <= r <= n
    # 1 <= pos <= n
    # 这里给出一种简单的测试数据生成方式，你可按需修改
    pos = n // 2 if n >= 2 else 1
    l = 1
    r = n if n >= 2 else 1

    # 如果你想测试一般情况（l 和 r 不在边界），可以改用如下逻辑：
    # if n >= 4:
    #     l = 2
    #     r = n - 1
    #     pos = n // 2
    # else:
    #     l = 1
    #     r = n
    #     pos = 1

    if l == 1 and r == n:
        ans = 0
    elif l == 1 and r != n:
        ans = abs(pos - r) + 1
    elif l != 1 and r == n:
        ans = abs(pos - l) + 1
    else:
        ans = r - l + 2 + min(abs(pos - l), abs(pos - r))

    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)