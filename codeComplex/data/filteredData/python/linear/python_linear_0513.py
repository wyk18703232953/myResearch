import random

def main(n: int):
    # 生成测试数据：长度为 n 的 0/1 序列
    a = [random.randint(0, 1) for _ in range(n)]
    b = [random.randint(0, 1) for _ in range(n)]

    ans = sum(q != w for q, w in zip(a, b))
    i = 1
    while i < n:
        aii = a[i - 1]
        ai = a[i]
        bii = b[i - 1]
        bi = b[i]
        if aii + ai == 1 and bii + bi == 1 and aii != bii and ai != bi:
            ans -= 1
            i += 1
        i += 1

    print(ans)


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)