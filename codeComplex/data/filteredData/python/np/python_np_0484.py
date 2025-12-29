import collections
import random
import string


def main(n):
    """
    将原逻辑封装为 main(n)，使用随机方式生成测试数据：
    - K 随机选择 [1, max(1, min(5, n))]，保证 2^K 不至于过大
    - 生成 n 个长度为 K 的字符串 A[i]（字符集为小写字母和 '_'）
    - 随机生成 m 条模式 B[i]（保证匹配条件尽量有解）
    """

    # 随机种子可根据需要固定，便于调试
    random.seed(0)

    # 1. 随机生成 K（长度）
    K = random.randint(1, max(1, min(5, n)))  # 控制 2^K 不太大

    # 2. 生成 n 个模式字符串 A（长度为 K）
    #   为了让题目更容易有解，使用较小的字符集
    charset = string.ascii_lowercase[:3] + "_"  # 'a','b','c','_'
    A = [''.join(random.choice(charset) for _ in range(K)) for _ in range(n)]

    # 3. 生成 m 和 B
    #   为了尽量保证可行性，这里构造 B 时：
    #   - 从 A 中随机选一个字符串 a = A[idx]
    #   - 随机选一个 b（1-based index）
    #   - 这样构造的样本较可能满足 “存在模式匹配到 b”
    m = max(1, n * 2)
    B = []
    for _ in range(m):
        idx = random.randrange(n)
        a = A[idx]
        b = random.randrange(1, n + 1)  # 1-based
        B.append([a, str(b)])

    # ========= 以下为原逻辑，去掉 input，使用 A, B, n, m, K =========

    D = {x: i for i, x in enumerate(A)}

    G = [set() for _ in range(n)]
    X = [set() for _ in range(n)]

    for i in range(m):
        a, b = B[i]
        b = int(b)
        flag = False
        for j in range(2 ** K):
            x = []
            for k in range(K):
                if (j >> k) & 1:
                    x.append('_')
                else:
                    x.append(a[k])
            x = ''.join(x)
            if x in D:
                if D[x] == b - 1:
                    flag = True
                    continue
                else:
                    G[b - 1].add(D[x])
                    X[D[x]].add(b - 1)
        if not flag:
            print("NO")
            return

    X = [len(X[i]) for i in range(n)]
    ANS = []
    q = collections.deque()
    for i in range(n):
        if X[i] == 0:
            q.append(i)

    while q:
        if len(ANS) == n:
            print("NO")
            return
        x = q.popleft()
        ANS.append(x + 1)
        for y in G[x]:
            if X[y] == 0:
                continue
            X[y] -= 1
            if X[y] == 0:
                q.append(y)

    if len(ANS) == n:
        print("YES")
        print(*ANS)
    else:
        print("NO")


if __name__ == "__main__":
    # 示例运行：n = 5
    main(5)