import random

def main(n):
    # 生成规模为 n 的测试数据，这里用 1..n 范围内的随机整数
    # 为保证不会出现除以 0 的错误，k1, k2, k3 从 1 开始取值
    k1 = random.randint(1, max(1, n))
    k2 = random.randint(1, max(1, n))
    k3 = random.randint(1, max(1, n))

    fl = 0
    for i1 in range(5):
        for i2 in range(5):
            for i3 in range(5):
                flak = 1
                for i in range(8):
                    if (i - i1) % k1 == 0 or (i - i2) % k2 == 0 or (i - i3) % k3 == 0:
                        continue
                    else:
                        flak = 0
                if flak == 1:
                    fl = 1
    if fl == 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)