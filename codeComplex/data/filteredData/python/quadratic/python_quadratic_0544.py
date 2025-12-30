def main(n: int) -> int:
    # 根据规模 n 生成测试数据，这里简单设定 v 为 n 的中点
    # 你可以按需要调整生成规则
    v = max(1, n // 2)

    cur = 0
    total = 0
    for i in range(n):
        while cur < n - i - 1:
            cur += 1
            total += (i + 1)
            if cur == v:
                break
        cur -= 1
    return total


if __name__ == "__main__":
    # 示例：自行指定 n 来测试
    n = 10
    print(main(n))