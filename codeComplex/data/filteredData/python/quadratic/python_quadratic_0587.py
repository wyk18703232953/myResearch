import random

def main(n):
    """
    n: 规模，用来生成测试数据的字符串长度
    程序内部会构造一组 (T, n, k, s) 测试数据并打印对应答案。
    """

    # 生成测试数据
    T = 1                            # 测试组数，可按需调整
    k = max(1, n // 2)               # 窗口大小，示例设为 n//2，至少为 1
    chars = ['R', 'G', 'B']
    s = ''.join(random.choice(chars) for _ in range(n))

    print("T =", T)
    print("n =", n, "k =", k)
    print("s =", s)

    # 以下为原逻辑封装
    for _ in range(T):
        rq1 = ''
        rq2 = ''
        rq3 = ''

        for i in range(k):
            if i % 3 == 0:
                rq1 = rq1 + 'R'
                rq2 = rq2 + 'G'
                rq3 = rq3 + 'B'
            elif i % 3 == 1:
                rq1 = rq1 + 'G'
                rq2 = rq2 + 'B'
                rq3 = rq3 + 'R'
            elif i % 3 == 2:
                rq1 = rq1 + 'B'
                rq2 = rq2 + 'R'
                rq3 = rq3 + 'G'

        ans = 10**18

        for i in range(0, len(s) - k + 1):
            a1 = 0
            a2 = 0
            a3 = 0

            for j in range(i, i + k):
                if s[j] != rq1[j - i]:
                    a1 += 1
                if s[j] != rq2[j - i]:
                    a2 += 1
                if s[j] != rq3[j - i]:
                    a3 += 1

            ans = min(ans, min(a1, a2, a3))

        print("answer =", ans)


if __name__ == "__main__":
    # 示例调用，可按需修改 n
    main(10)