import random

def main(n: int):
    # 生成测试数据：长度为 n 的01串
    # 为了保证原程序中索引访问始终合法，让 a 与 b 等长
    a = ''.join(random.choice('01') for _ in range(n))
    b = ''.join(random.choice('01') for _ in range(n))

    o = []
    z = []
    c0 = 0
    c1 = 0
    for i in b:
        if i == "0":
            c0 += 1
        else:
            c1 += 1
        o.append(c1)
        z.append(c0)

    n_b = len(b) - 1
    m_a = len(a) - 1
    ans = 0
    for i in range(len(a)):
        x = a[i]
        if x == "1":
            ans += z[(n_b - (m_a - i))] - z[i]
            if b[i] == "0":
                ans += 1
        else:
            ans += o[(n_b - (m_a - i))] - o[i]
            if b[i] == "1":
                ans += 1

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)