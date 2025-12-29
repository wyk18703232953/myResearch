import random

def main(n: int):
    # 生成测试数据：根据规模 n 随机生成 a, b
    # 这里设定 a, b 为 [0, 2^n) 内的整数
    if n <= 0:
        # 规模太小则直接返回
        return

    max_val = 2 ** n
    a = random.randrange(max_val)
    b = random.randrange(max_val)

    if a == b:
        print(0)
        return

    e1 = bin(a)[2:]
    e2 = bin(b)[2:]
    diff = len(e2) - len(e1)
    e1 = ("0" * diff) + e1
    e1 = e1[::-1]
    e2 = e2[::-1]
    ans = ["0"] * len(e2)

    for i in range(len(e2)):
        if b - a >= 2 ** i:
            ans[i] = "1"
        else:
            if int(e1[i]) ^ int(e2[i]) == 1:
                ans[i] = "1"

    print(int("".join(ans[::-1]), 2))


if __name__ == "__main__":
    # 示例：使用 n = 10 作为规模
    main(10)