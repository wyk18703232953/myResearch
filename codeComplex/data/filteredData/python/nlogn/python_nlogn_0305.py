import random

def main(n: int):
    # 1. 生成测试数据
    # 生成 n 个不同的正整数
    w = random.sample(range(1, 10 * n + 1), n)
    # 生成一个合法的长度为 2n 的入栈(0)/出栈(1)序列
    # 先生成 n 个 0 和 n 个 1，然后打乱，并校正为合法出栈序列
    seq = ['0'] * n + ['1'] * n
    random.shuffle(seq)

    # 校正为合法栈操作序列：保证任何前缀中 1 的数量不超过 0 的数量
    balance = 0
    for i in range(2 * n):
        if seq[i] == '0':
            balance += 1
        else:
            if balance == 0:
                # 前缀中出栈过多，强制改为入栈
                seq[i] = '0'
                balance += 1
            else:
                balance -= 1

    # 现在 balance >= 0，可能还有多余入栈，需要在后缀中改回若干 1
    # 最终需要恰好 n 个 0, n 个 1
    extra_push = balance  # 多出来的 '0' 数量
    i = 2 * n - 1
    while extra_push > 0 and i >= 0:
        if seq[i] == '0':
            seq[i] = '1'
            extra_push -= 1
        i -= 1

    ent = ''.join(seq)

    # 2. 原始逻辑
    mp = {w[i]: i + 1 for i in range(n)}
    w.sort()
    ptr = 0
    stk = []
    for i in range(2 * n):
        if ent[i] == "0":
            print(mp[w[ptr]], end=" ")
            stk.append(mp[w[ptr]])
            ptr += 1
        else:
            print(stk.pop(), end=" ")
    print()


if __name__ == "__main__":
    # 示例：n = 5
    main(5)