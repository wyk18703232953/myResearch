def main(n: int) -> int:
    """
    n: 问题规模，同时作为原程序中的输入值
    返回值: 计算结果（原程序的输出）
    """
    # 原逻辑：n=int(input());print(sum(i for i in range(1+n%2!=1,n+1,2)))
    # 其中 1 + n%2 != 1 为布尔值 False/True，在 range 起点位置会被当作 0/1
    # 等价于从 (n 为偶数则 0，否则 1) 开始，到 n，步长为 2 的所有数之和
    result = sum(i for i in range(1 + (n % 2 != 1), n + 1, 2))
    return result


if __name__ == "__main__":
    # 根据 n 生成测试数据：此处直接用若干典型规模进行测试
    test_ns = [1, 2, 5, 10, 11, 20]
    for n in test_ns:
        print(f"n = {n}, result = {main(n)}")