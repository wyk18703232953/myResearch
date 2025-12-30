import random

def main(n: int):
    # 生成随机 k，范围 [1, n]
    k = random.randint(1, n)

    # 生成测试数据 t，共 n 行，每行两个整数
    # 这里生成范围在 [1, 100] 的随机整数，可按需要调整
    t = []
    for _ in range(n):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        t.append([a, b])

    # 按原逻辑排序：先按第一个元素降序，再按第二个元素升序
    t.sort(key=lambda x: (-x[0], x[1]))

    # 找到第 k-1 个元素
    pt = t[k - 1]

    # 输出与该元素相同的个数
    print(t.count(pt))


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)