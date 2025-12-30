import random

def main(n):
    # 生成测试数据：随机生成 n 个在 [0, 2n] 范围内的整数
    l = [random.randint(0, 2 * n) for _ in range(n)]
    l.sort()

    def f():
        dou = False
        for k in range(1, n):
            if l[k] == l[k - 1]:
                if (
                    dou
                    or l[k] == 0
                    or (k >= 2 and l[k] == l[k - 2] and n != 2)
                    or (k >= 2 and l[k] == l[k - 2] + 1)
                ):
                    return False
                else:
                    dou = True
        return (sum(l) - (n * (n - 1)) // 2) % 2

    if f():
        print("sjfnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)