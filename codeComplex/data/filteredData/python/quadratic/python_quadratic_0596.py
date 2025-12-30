import random

def main(n):
    # 生成参数 m, k（可根据需要调整生成策略）
    # 这里让 m 在 [1, n] 内，k 在 [1, 10] 内
    if n <= 0:
        return

    m = random.randint(1, n)
    k = random.randint(1, 10)

    # 生成长度为 n 的数组 a，元素在 [-10, 10] 内
    a = [random.randint(-10, 10) for _ in range(n)]

    def f(o):
        r = e = 0
        for i, x in enumerate(a):
            if i < o:
                continue
            if i % m == o:
                e -= k
                if e < -k:
                    e = -k
            e += x
            if e > r:
                r = e
        return r

    ans = max(f(o) for o in range(m))
    print(ans)

if __name__ == "__main__":
    # 示例：规模设为 10，可根据需要修改
    main(10)