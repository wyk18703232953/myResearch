from random import randint

mod = (10 ** 9) + 7
mod1 = mod - 1

def modinv(n, p):
    return pow(n, p - 2, p)

def ncr(n, r, p):
    t = (fact[n] * modinv(fact[r], p) % p * modinv(fact[n - r], p) % p) % p
    return t

def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

def main(n):
    """
    n: 规模参数，用来控制测试数据大小。
       这里我们约定：
       - 测试用例个数 T = max(1, min(10, n))
       - 每个数组长度 a 在 [2, max(2, n)] 之间随机生成
       - 数组元素为 [1, max(2, n)] 间的随机整数
    """
    q = []
    T = max(1, min(10, n))  # 测试用例个数

    for _ in range(T):
        # 生成测试数据
        a = randint(2, max(2, n))
        max_val = max(2, n)
        b = [randint(1, max_val) for _ in range(a)]

        # 原逻辑开始
        w = {}
        for x in b:
            if x in w:
                w[x] += 1
            else:
                w[x] = 1

        s = -1
        l = 0
        mi = 2325234324324234.0
        d = []
        # 找到出现次数>=4的数或者收集出现>=2次的数
        for key in w:
            if w[key] >= 4:
                t = [str(key), str(key), str(key), str(key)]
                q.append(" ".join(t))
                l = 1
                break
            if w[key] >= 2:
                d.append(key)
        if l == 1:
            continue

        d.sort()
        p = None
        for i in range(len(d)):
            if s == -1:
                s = d[i]
            else:
                r = float(s) / float(d[i]) + float(d[i]) / float(s)
                if r < mi:
                    p = [str(d[i]), str(s)]
                    mi = r
                s = d[i]
        if p is None:
            # 若没有任何数出现至少两次，构造一个退化输出（原代码未显式处理此情况）
            if len(b) >= 2:
                p = [str(b[0]), str(b[1])]
            else:
                p = ["1", "1"]
        p = p * 2
        q.append(" ".join(p))

    # 输出结果到标准输出
    print("\n".join(q))


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)