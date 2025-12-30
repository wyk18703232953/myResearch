def digs(k: int) -> int:
    r = k
    while k:
        r -= k % 10
        k //= 10
    return r

def main(n: int):
    # 按规模 n 生成测试数据：
    # 令 s 为 n 的一半（可根据需要调整生成策略）
    s = n // 2

    x = s + 19 * 9
    while digs(x - 1) >= s:
        x -= 1
    result = max(n - x + 1, 0)
    print(result)


if __name__ == "__main__":
    # 示例：使用某个规模 n 运行
    main(1000)