import random

def main(n: int):
    # 原逻辑：在无限的正整数序列 123456789101112... 中
    # 找到第 n 个数字（1-based），并输出。
    s = 0
    pred = 0
    for i in range(1, 20):
        m = 9 * pow(10, i - 1) * i
        s += m
        if n <= s:
            nd = pow(10, i - 1)
            sme = n - pred
            num = sme // i
            ost = sme % i
            if ost == 0:
                dig = nd + num - 1
            else:
                dig = nd + num
            d = i
            rez = []
            ddig = dig
            while d > 0:
                o = ddig % 10
                a = ddig // 10
                rez.append(o)
                d -= 1
                ddig = a
            print(str(rez[-ost]))
            return
        pred = s

if __name__ == "__main__":
    # 根据 n 生成测试数据：这里简单地随机选取一个 1 到 10^6 之间的 n
    test_n = random.randint(1, 10**6)
    main(test_n)