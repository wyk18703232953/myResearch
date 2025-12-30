import random

def main(n):
    # 生成测试数据：
    # 1. 生成 n 个不同的正整数
    w = random.sample(range(1, 10 * n + 1), n)
    # 2. 生成一个长度为 2n 的 0/1 字符串，满足：
    #    - 恰好有 n 个 '0' 和 n 个 '1'
    #    - 任意前缀中 '1' 的数量不超过 '0' 的数量（栈操作合法）
    zeros = n
    ones = n
    ent = []
    balance = 0  # 当前 0 的个数 - 1 的个数

    for _ in range(2 * n):
        if zeros == 0:
            ent.append('1')
            ones -= 1
            balance -= 1
        elif ones == 0:
            ent.append('0')
            zeros -= 1
            balance += 1
        else:
            # 随机决定放 0 或 1，但不能让 balance 变为负
            if balance == 0:
                ent.append('0')
                zeros -= 1
                balance += 1
            else:
                # 在可以的情况下随机
                if random.random() < 0.5:
                    ent.append('0')
                    zeros -= 1
                    balance += 1
                else:
                    ent.append('1')
                    ones -= 1
                    balance -= 1

    ent = ''.join(ent)

    # 原始逻辑
    mp = {w[i]: i + 1 for i in range(n)}
    w.sort()
    ptr = 0
    stk = []
    out = []

    for i in range(2 * n):
        if ent[i] == "0":
            out.append(str(mp[w[ptr]]))
            stk.append(mp[w[ptr]])
            ptr += 1
        else:
            out.append(str(stk.pop()))

    print(" ".join(out))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)