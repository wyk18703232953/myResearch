def main(n):
    v = n // 2 + 1  # 确定性生成：给定 n，v 与 n 成固定关系

    res = 0
    fuel = 0
    for i in range(1, n):
        miss = min(v - fuel, n - i - fuel)
        res += i * miss
        fuel += miss - 1
        if v - fuel == 0:
            print(res)
            return
    print(res)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的规模
    main(10)