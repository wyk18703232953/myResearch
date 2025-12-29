import random

def main(n):
    # 生成测试数据
    # n 为数组长度，生成 l 中的元素范围和 k
    # 这里设定：
    #   k 在 [2, 10] 中随机
    #   l 中元素在 [1, 10 * n] 中随机
    k = random.randint(2, 10)
    l = sorted(random.randint(1, 10 * n) for _ in range(n))

    # 原逻辑
    res = set()
    for i in l:
        if i % k != 0 or i / k not in res:
            res.add(i)

    print(len(res))

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)