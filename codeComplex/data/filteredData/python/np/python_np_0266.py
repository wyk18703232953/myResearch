import math
import random

def main(n):
    # n 作为规模：构造一个完全二叉树，节点数 N = 2^n - 1
    # 查询次数 q 与 n 相关（例如 q = n），可按需要调整
    N = 2 ** n - 1
    q = n

    for _ in range(q):
        # 生成测试数据：u 在 [1, N] 范围内
        u = random.randint(1, N)
        # 生成测试数据：随机长度的操作串 S，字符为 'L','R','U'
        # 长度不超过 n，防止过长
        length_S = random.randint(0, n)
        S = ''.join(random.choice(['L', 'R', 'U']) for _ in range(length_S))

        # 以下是原逻辑，去除 input，使用生成的 u 和 S
        k = (N + 1) // 2
        # N = 2^n - 1 ⇒ N+1 = 2^n ⇒ log2(N+1) = n
        # 原代码：n = int(log10(N+1)/log10(2)) - 1
        n_level = int(math.log((N + 1), 10) / math.log(2, 10)) - 1
        dup_n = n_level
        store = [k]
        while u != k:
            n_level -= 1
            if u > k:
                k += 2 ** n_level
            else:
                k -= 2 ** n_level
            store.append(k)

        for ch in S:
            if ch == 'R':
                n_level -= 1
                if n_level == -1:
                    n_level = 0
                    continue
                k += 2 ** n_level
            elif ch == 'L':
                n_level -= 1
                if n_level == -1:
                    n_level = 0
                    continue
                k -= 2 ** n_level
            else:  # 'U'
                if n_level == dup_n:
                    continue
                store.pop()
                k = store[-1]
                n_level += 1
                continue
            store.append(k)

        print(k)


if __name__ == "__main__":
    # 示例：调用 main(20)，可自行修改 n
    main(20)