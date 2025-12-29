import random

def main(n):
    # 预生成 2 的幂列表
    ans = [1 << i for i in range(32)]  # 2**i

    # 生成规模为 n 的测试数据：整数列表 l
    # 这里假设数据范围在 [1, 10^5]，可根据需求调整
    max_val = 10**5
    l = [random.randint(1, max_val) for _ in range(n)]

    # 统计频次
    d = {}
    for x in l:
        d[x] = d.get(x, 0) + 1

    # 按原逻辑计算答案
    c = 0
    for x in d.keys():
        for s in ans:
            need = s - x
            if need in d and (need != x or d[need] > 1):
                break
        else:
            c += d[x]

    print(c)


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)