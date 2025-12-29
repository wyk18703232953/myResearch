def main(n: int):
    """
    根据规模 n 生成测试数据并执行原逻辑。
    测试数据生成规则（可按需修改）：
      - 固定 l = 1
      - 固定 r = n
      - cur 在 [1, n] 中取一个中间位置
    """
    if n <= 0:
        return

    # 生成一组测试数据 (n, cur, l, r)
    l = 1
    r = n
    cur = (n + 1) // 2  # 中间位置

    # 原逻辑
    if l == 1 and r == n:
        print(0)
    elif l == 1 and r != n:
        print(abs(r - cur) + 1)
    elif r == n and l != 1:
        print(abs(cur - l) + 1)
    else:
        disa = abs(l - cur)
        disb = abs(r - cur)
        ans = min(disa, disb) + (r - l) + 2
        print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)