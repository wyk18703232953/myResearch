import random

def main(n):
    # 生成测试数据
    # 随机生成查询次数 q（至少 1，至多 n）
    q = max(1, n // 3)
    results = []

    for _ in range(q):
        # 随机生成 k，1 <= k <= n
        k = random.randint(1, n)
        # 随机生成长度为 n 的字符串 l，由 'R','G','B' 组成
        l = ''.join(random.choice('RGB') for _ in range(n))

        # 以下为原逻辑的封装
        k1 = 'R'
        k2 = 'G'
        k3 = 'B'
        for i in range(1, k):
            if k1[i - 1] == 'R':
                k1 = k1 + 'G'
            if k1[i - 1] == 'G':
                k1 = k1 + 'B'
            if k1[i - 1] == 'B':
                k1 = k1 + 'R'
            if k2[i - 1] == 'R':
                k2 = k2 + 'G'
            if k2[i - 1] == 'G':
                k2 = k2 + 'B'
            if k2[i - 1] == 'B':
                k2 = k2 + 'R'
            if k3[i - 1] == 'R':
                k3 = k3 + 'G'
            if k3[i - 1] == 'G':
                k3 = k3 + 'B'
            if k3[i - 1] == 'B':
                k3 = k3 + 'R'

        minn = n

        for i in range(n - k + 1):
            tec = 0
            for j in range(k):
                if l[i + j] != k1[j]:
                    tec += 1
            if tec < minn:
                minn = tec

        for i in range(n - k + 1):
            tec = 0
            for j in range(k):
                if l[i + j] != k2[j]:
                    tec += 1
            if tec < minn:
                minn = tec

        for i in range(n - k + 1):
            tec = 0
            for j in range(k):
                if l[i + j] != k3[j]:
                    tec += 1
            if tec < minn:
                minn = tec

        results.append(minn)

    # 按原程序风格输出
    for ans in results:
        print(ans)


if __name__ == "__main__":
    # 你可以在这里修改规模 n 进行测试
    main(10)