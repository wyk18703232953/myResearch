import random

def main(n):
    """
    n 为测试规模，这里用来生成 n 组测试数据，
    每组数据是一个长度为 3 的整数数组 k，元素范围可自行调整。
    函数将返回一个长度为 n 的结果列表，每个元素为 "YES" 或 "NO"。
    """
    results = []

    for _ in range(n):
        # 生成一组测试数据：长度固定为 3，数值范围 1~5
        k = [random.randint(1, 5) for _ in range(3)]
        k.sort()

        # 原逻辑判断
        if min(k) == 1:
            res = "YES"
        elif k.count(2) >= 2:
            res = "YES"
        elif k.count(3) == 3:
            res = "YES"
        elif k == [2, 4, 4]:
            res = "YES"
        else:
            res = "NO"

        results.append((k, res))

    return results


if __name__ == "__main__":
    # 示例：跑 10 组随机测试
    ans = main(10)
    for k, res in ans:
        print(k, res)