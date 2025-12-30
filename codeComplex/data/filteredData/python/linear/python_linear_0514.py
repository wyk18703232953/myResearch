import random

def main(n: int) -> int:
    """
    n: 序列长度（规模）
    返回：按照原逻辑计算得到的 count
    """

    # 3. 生成测试数据：随机由 '0' 和 '1' 组成的两个长度为 n 的字符串
    # 你可以根据需要改成别的字符集或模式
    a = [random.choice(['0', '1']) for _ in range(n)]
    b = [random.choice(['0', '1']) for _ in range(n)]

    count = 0
    skip_next = False

    # 保留原逻辑
    for idx in range(n - 1):
        if skip_next:
            skip_next = False
            continue
        if a[idx] != b[idx] and a[idx] == b[idx + 1] and a[idx + 1] == b[idx]:
            count += 1
            a[idx] = b[idx]
            a[idx + 1] = b[idx + 1]
            skip_next = True

    for idx in range(n):
        if a[idx] != b[idx]:
            count += 1

    print(count)
    return count


if __name__ == "__main__":
    # 示例调用：可以修改 n 测试不同规模
    main(10)