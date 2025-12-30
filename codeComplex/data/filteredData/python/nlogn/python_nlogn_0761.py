import random

def main(n):
    # 生成 n 组测试数据
    for _ in range(n):
        # 随机生成 k，至少为 2
        k = random.randint(2, 10)
        # 生成长度为 k 的随机数组，元素为 1~100 的整数
        s = [random.randint(1, 100) for _ in range(k)]

        # 原逻辑
        s.sort()
        print(min(k - 2, s[k - 2] - 1))


if __name__ == "__main__":
    # 可在此处修改规模 n
    main(5)