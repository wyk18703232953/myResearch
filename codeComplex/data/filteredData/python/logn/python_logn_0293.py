modulo = 10 ** 9 + 7

def main(n: int):
    """
    n 为规模参数，这里用来生成测试数据 (x, k)。
    你可以根据需要修改生成策略。
    例如：
    - x 随 n 变化
    - k 随 n 变化
    """
    # 简单的测试数据生成策略：
    # 让 x = n，k = n（至少为 0）
    x = n
    k = n

    if x == 0:
        # print(0)
        pass
        return

    k2 = pow(2, k, modulo)
    ans = (x * k2 * 2 - k2 + 1) % modulo
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)