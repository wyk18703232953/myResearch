def main(n: int):
    """
    规模 n 用来生成一组 (a,b) 测试数据并执行原逻辑。
    这里约定：
      a = n
      b = max(1, n // 2)
    可按需要修改生成规则。
    """
    a = n
    b = max(1, n // 2)

    c = 2 * (a - 1) - b * (b - 1)
    if c > 0:
        print(-1)
    else:
        d = int((1 + (1 - 4 * c) ** 0.5) / 2)
        if d * (d - 1) + c > 0:
            d -= 1
        print(b - d)


if __name__ == "__main__":
    # 示例：可修改为任意规模 n
    main(10)