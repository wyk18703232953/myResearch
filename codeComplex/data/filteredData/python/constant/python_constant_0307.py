import random

def main(n: int):
    # 根据规模 n 生成测试数据
    # 这里简单设定：
    # k 与 n 同级别，s 与 p 在 1..n 范围内
    if n <= 0:
        return

    k = max(1, n)                 # 至少为 1
    s = random.randint(1, max(1, n))
    p = random.randint(1, max(1, n))

    # 原逻辑开始
    if (1 * n) % s == 0:
        need = (1 * n) // s
        if need == 0 and k % p == 0:
            print(k // p)
        elif (k * need) % p == 0:
            print((k * need) // p)
        else:
            print(((k * need) // p) + 1)
    else:
        need = ((1 * n) // s) + 1
        if need == 0 and k % p == 0:
            print(k // p)
        elif (k * need) % p == 0:
            print((k * need) // p)
        else:
            print(((k * need) // p) + 1)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)