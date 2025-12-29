import random

def main(n):
    # 根据规模 n 生成测试数据：生成两个 1~n 的随机整数 x, y，保证 x <= y
    x = random.randint(1, n)
    y = random.randint(1, n)
    if x > y:
        x, y = y, x

    if abs(x - y) < 2:
        print(-1)
    else:
        k = []
        for i in range(x, y + 1):
            if i % 2 == 0:
                k.append(i)
                if i + 1 < y:
                    k.append(i + 1)
                    k.append(i + 2)
                    break
        if len(k) == 3:
            print(" ".join(str(t) for t in k))
        else:
            print(-1)


if __name__ == "__main__":
    # 示例：规模 n = 100
    main(100)