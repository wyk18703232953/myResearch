import random

def main(n: int):
    mod = 10**9 + 7

    # 生成测试数据：a 为长度为 n 的数组，元素范围 [0, 2^20 - 1]
    a = [random.randint(0, (1 << 20) - 1) for _ in range(n)]

    b = [0] * (1 << 20)
    for x in a:
        b[x] += 1

    # SOS DP 子集和
    for i in range(20):
        step = 1 << i
        for j in range(1 << 20):
            if (j & step) == 0:
                b[j] += b[j | step]

    ans = 0
    for i in range(1 << 20):
        cnt = bin(i).count("1")
        val = pow(2, b[i], mod) - 1
        if cnt % 2 == 0:
            ans += val
        else:
            ans -= val
        ans %= mod

    print(ans)


if __name__ == "__main__":
    # 示例：可在此处指定规模 n
    main(5)