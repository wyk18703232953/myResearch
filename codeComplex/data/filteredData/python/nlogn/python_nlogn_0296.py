import random

def main(n: int):
    # 1. 生成测试数据
    # 原程序中：读入 n 和一个长度为 n 的整数数组，以及一个长度为 2n 的只含 '0' '1' 的字符串 s。
    # 这里我们根据 n 构造：
    #   - 一个长度为 n 的随机整数数组 a
    #   - 一个合法的括号式 0/1 序列 s，其中 0 表示 "push"，1 表示 "pop"，且长度为 2n

    # 生成数组 a
    a = [random.randint(1, 10**9) for _ in range(n)]

    # 生成合法的 0/1 序列 s：
    # 简单方式：先构造 n 个 0 再 n 个 1，即 "000...0111...1"
    # 这保证栈操作合法（不会在空栈上 pop）
    s = "0" * n + "1" * n

    # 2. 按原始逻辑处理
    # l = sorted(zip(lst(), range(n)))
    l = sorted(zip(a, range(n)))
    p = 0
    ans = [0] * (2 * n)
    st = [0] * n
    ln = 0

    for i in range(2 * n):
        ch = s[i]
        if ch == '0':
            st[ln] = p
            ans[i] = l[p][1] + 1
            ln += 1
            p += 1
        else:
            ans[i] = l[st[ln - 1]][1] + 1
            ln -= 1

    # 输出与原程序等价的结果
    print(*ans)


if __name__ == "__main__":
    # 示例：运行 main(5)
    main(5)