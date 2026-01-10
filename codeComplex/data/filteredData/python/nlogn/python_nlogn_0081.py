def main(n):
    # 映射含义：
    # n: 数组长度
    # k: 固定选择为 n // 2（中间位置），保证 1 <= k <= n
    if n <= 0:
        return

    k = max(1, n // 2)

    # 生成确定性数据：
    # A 中每个元素是一个二元组 (x, y)
    # x 从 n 到 1 递减，y 为 i % 3，制造部分重复
    A = [(n - i, i % 3) for i in range(n)]

    # 保持原排序逻辑：按 x 降序，y 升序
    A_sorted = sorted(A, key=lambda x: (-x[0], x[1]))

    # 保持原逻辑：统计第 k-1 个元素出现次数
    target = A_sorted[k - 1]
    result = A_sorted.count(target)

    print(result)


if __name__ == "__main__":
    main(10)