import math

def main(n):
    # 解释规模含义：
    # N 使用接近 2^m - 1 的规模，以便原算法中的 log 运算有意义
    # q = n，表示有 n 组查询
    # u 和 S 的构造均为确定性，与 i 和 N 的简单算术关系

    if n <= 0:
        return

    # 构造 N：略大于 n 的最接近形如 (2^m - 1) 的数
    # 保证 N 足够大，使得 log2(N+1) 有意义
    m = max(1, int(math.log2(n + 1)))
    N = (1 << m) - 1

    q = n

    for j in range(q):
        # 确定性构造 u：
        # 在区间 [1, N] 中循环取值
        u = (j * 7 + 3) % N + 1

        # 确定性构造操作串 S，长度随 n 变化
        # 字符从 'L','R','U' 中按下标循环选取
        ops_len = max(1, (j % (m + 3)) + 1)
        ops = ['L', 'R', 'U']
        S = ''.join(ops[(j + i) % 3] for i in range(ops_len))

        k = (N + 1) // 2
        n_level = int(math.log((N + 1), 10) / math.log(2, 10)) - 1
        dup_n = n_level
        store = [k]

        # 原始逻辑：根据 u 定位，再根据 S 操作
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
            else:  # 'U' 的情况，对应原来的其他字符分支
                if n_level == dup_n:
                    continue
                store.pop()
                k = store[-1]
                n_level += 1
                continue
            store.append(k)

        print(k)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的大小做规模实验
    main(10)