def main(n):
    """
    规模 n：同时生成一个 m，并按照原逻辑输出坐标。
    这里假设 m = n，可按需要修改生成规则。
    """
    import sys

    m = n  # 生成测试数据：示例中令 m = n，可按需要调整

    up, down = 1, n
    count = 0
    total = n * m

    # 仿照原程序逻辑输出
    while up <= down:
        left, right = 1, m
        while left <= m and count < total:
            if count < total:
                sys.stdout.write(f"{up} {left}\n")
            count += 1
            left += 1

            if count < total:
                sys.stdout.write(f"{down} {right}\n")
            count += 1
            right -= 1
        up += 1
        down -= 1


if __name__ == "__main__":
    # 示例：调用 main(3) 以生成测试数据并输出
    main(3)