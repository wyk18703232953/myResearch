def f(l):
    n, m = l  # 保留原有解构，虽然未使用
    return ['5' * 282, '4' * 281 + '5']


def main(n):
    """
    n: 规模参数，这里用于生成测试数据。
       按原程序逻辑，只需要两个整数，这里生成 [n, 2n]。
    """
    l = [n, 2 * n]  # 根据 n 构造测试数据
    results = f(l)
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # 示例：以 n = 10 运行，可按需修改
    main(10)