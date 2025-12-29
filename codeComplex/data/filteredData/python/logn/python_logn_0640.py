import random

def main(n: int):
    # 生成测试数据：
    # data[0]：循环规模，至少为 1
    # data[1]：阈值，范围 [0, n]
    a = max(1, n)              # 保证至少循环 1 次
    b = random.randint(0, n)   # 阈值
    data = [a, b]

    total = 0
    cont = 0
    res = 0
    con2 = 0

    for _ in range(data[0]):
        total = total + con2
        con2 += 1
        res = data[0] - con2

        if data[1] == 0:
            if total >= res:
                cont += 1
        else:
            if total > data[1]:
                if res + 1 == total - data[1]:
                    cont = res + 1
                    break
    print(cont)


if __name__ == "__main__":
    # 示例：以 n = 10 作为规模运行
    main(10)