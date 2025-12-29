import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数列表，元素范围 [1, n]
    E = [random.randint(1, n) for _ in range(n)]

    # 原逻辑：统计每个元素出现次数，并按原顺序输出其出现次数
    D = {}
    for e in E:
        D[e] = D.get(e, 0) + 1
    for e in E:
        print(D[e])

if __name__ == "__main__":
    # 示例：可在此处指定规模 n 进行测试
    main(10)