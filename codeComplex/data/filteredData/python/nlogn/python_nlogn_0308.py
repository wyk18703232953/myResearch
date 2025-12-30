import random

def main(n):
    # 1. 生成测试数据：a 为长度为 n 的整数数组，值在 1..10^9
    a = [random.randint(1, 10**9) for _ in range(n)]
    # 2. 生成操作串：长度为 n 的 0/1 串，保证是合法的栈操作序列
    #    思路：共 n 次 push（对应 '0'），n 次 pop（对应 '1'），保持前缀中 push 次数 ≥ pop 次数
    ops = []
    push_left = n
    pop_left = n
    current_stack = 0
    for _ in range(2 * n):
        can_push = push_left > 0
        can_pop = pop_left > 0 and current_stack > 0
        if can_push and can_pop:
            # 随机决定 push 或 pop，保证合法
            if random.randint(0, 1) == 0:
                ops.append('0')
                push_left -= 1
                current_stack += 1
            else:
                ops.append('1')
                pop_left -= 1
                current_stack -= 1
        elif can_push:
            ops.append('0')
            push_left -= 1
            current_stack += 1
        else:
            ops.append('1')
            pop_left -= 1
            current_stack -= 1
    ops = ''.join(ops)

    # 原逻辑开始
    i = iter(sorted(zip(a, range(1, n + 1))))
    s, o = [], []
    for c in ops:
        if c == '0':
            x = next(i)[1]
            o.append(x)
            s.append(x)
        else:
            o.append(s.pop())
    print(*o)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)