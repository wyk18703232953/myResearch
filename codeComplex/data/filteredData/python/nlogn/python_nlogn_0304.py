import random

def main(n):
    # 1. 生成测试数据：lst 为 n 个随机整数
    # 数值范围可自行调整，这里设为 1..10^9
    lst = [random.randint(1, 10**9) for _ in range(n)]

    # 2. 生成长度为 2n 的操作字符串 s
    # 保证恰好有 n 个 '0' 和 n 个 '1'，顺序随机
    ops = ['0'] * n + ['1'] * n
    random.shuffle(ops)
    s = ''.join(ops)

    # 以下为原逻辑（去掉 input 部分）
    for j in range(n):
        lst[j] = [lst[j], j + 1]
    lst.sort()
    stk = []
    i = 0
    out = []
    for j in range(2 * n):
        if s[j] == '0':
            stk.append(lst[i][1])
            out.append(str(lst[i][1]))
            i += 1
        else:
            out.append(str(stk[-1]))
            stk.pop()

    print(' '.join(out))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可根据需要修改 n
    main(5)