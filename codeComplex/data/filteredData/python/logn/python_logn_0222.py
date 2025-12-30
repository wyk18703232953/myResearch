import random

def main(n):
    # 根据 n 生成测试数据：随机生成 s，保证 0 <= s <= n
    if n < 0:
        raise ValueError("n must be non-negative")
    s = random.randint(0, n)

    if s >= n:
        print(0)
        return

    ans = 0

    def sod(x):
        s_ = str(x)
        ret = 0
        for ch in s_:
            ret += int(ch)
        return ret

    for nd in range(s, s + 1000):
        if nd - sod(nd) >= s:
            ans += 1
        if nd == n:
            break
        if nd == (s + 369):
            ans += (n - nd)
            break
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(100000)
    main(100000)