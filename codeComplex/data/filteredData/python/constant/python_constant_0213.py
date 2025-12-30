import random

def main(n: int):
    # 生成规模为 n 的测试数据：这里理解为生成 n 组三元组 (k1, k2, k3)
    # 若你希望 n 直接代表值域上限，可改为相应逻辑
    results = []
    for _ in range(n):
        # 根据题意，k1, k2, k3 是整数，这里随机构造一些适当范围内的值
        k1 = random.randint(1, 5)
        k2 = random.randint(1, 5)
        k3 = random.randint(1, 5)
        l = [k1, k2, k3]

        if min(k1, k2, k3) == 1:
            results.append('yes')
        elif l.count(2) >= 2:
            results.append('yes')
        elif l.count(3) == 3:
            results.append('yes')
        elif l.count(4) == 2 and l.count(2) == 1:
            results.append('yes')
        else:
            results.append('no')

    # 输出每组对应结果（如需只跑一次，可改为仅生成一组并打印）
    for res in results:
        print(res)


if __name__ == "__main__":
    # 示例：运行规模 n=5
    main(5)