import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数列表，元素在 [1, 100] 范围内
    p = [random.randint(1, 100) for _ in range(n)]

    x = max(p)
    idx = p.index(x)
    if p[idx] == 1:
        p[idx] = 2
    else:
        p[idx] = 1
    p.sort()
    print(' '.join(str(i) for i in p))


if __name__ == "__main__":
    # 示例：n = 10
    main(10)