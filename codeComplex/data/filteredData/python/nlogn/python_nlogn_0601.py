import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 生成 m 个栈高度，m 可以与 n 相同或根据 n 设置，这里设为 m = n
    m = n
    # 生成每个栈的高度：1 到 n 之间的随机整数
    stacks = [random.randint(1, n) for _ in range(m)]

    # 2. 按原逻辑进行计算
    stacks.sort()

    ans = 0
    cur_stack = 0
    cur_h = 0

    while cur_stack < n:
        ans += 1
        if stacks[cur_stack] >= cur_h + 1:
            cur_h += 1
        cur_stack += 1
    ans += stacks[-1] - cur_h

    print(sum(stacks) - ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)