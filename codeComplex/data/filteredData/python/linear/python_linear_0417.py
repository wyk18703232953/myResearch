import random

def main(n):
    # 随机生成 x（假设范围与原题类似，这里取 0~(2*n)）
    x = random.randint(0, 2 * n if n > 0 else 1)
    # 随机生成集合 a，元素范围可调，这里取 0~(4*n)
    # 为了尽量让 |a| 接近 n，这里生成 n 个随机数再取 set
    a = set(random.randint(0, 4 * n if n > 0 else 1) for _ in range(n))

    if len(a) < n:
        print(0)
    else:
        d = set()
        p = 0
        for i in a:
            t = i & x
            d.add(t)
            if t != i and t in a:
                print(1)
                p = 1
                break
        if len(d) < n and p == 0:
            print(2)
        elif p != 1:
            print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)