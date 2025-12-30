import random

def main(n):
    # 生成测试数据：t 组测试，每组长度为 n
    t = 5  # 可以根据需要调整测试组数
    results = []

    for _ in range(t):
        # 生成一组长度为 n 的随机整数，范围可根据需求调整
        lens = [random.randint(-n, n) for _ in range(n)]
        lens.sort()

        cnt = len(list(filter(lambda x: x > 0, lens[:-2]))) if n > 2 else 0
        if n > 1:
            res = min(cnt, lens[-2] - 1)
        else:
            res = 0
        results.append(res)

    # 输出所有结果
    for r in results:
        print(r)


if __name__ == "__main__":
    # 示例：规模设为 10
    main(10)