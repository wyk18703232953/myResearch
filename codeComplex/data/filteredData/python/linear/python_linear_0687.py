import random

def main(n: int):
    # 生成测试数据 b，规则：随机构造一个合法的 a，再反推 b
    # 原逻辑：给定 b，构造 a；这里反向：生成 a，计算 b，使原算法可执行
    if n < 2 or n % 2 != 0:
        raise ValueError("n 必须是大于等于 2 的偶数")

    a = [0] * n
    # 随机生成 a
    for i in range(n):
        a[i] = random.randint(0, 10**6)

    # 根据原程序的推导规则构造 b
    b = [0] * (n - 1)

    l = n // 2 - 1
    r = n // 2

    # b[l] = a[l] + a[r]
    b[l] = a[l] + a[r]

    # 向外依次计算 b[l-1], b[l-2], ...
    i_l = l
    i_r = r
    while i_l > 0:
        # 对于原算法“if b[i_l-1] >= b[i_l]”与“else”的两种情况，
        # 这里固定采用第一种情况反推一个合法的 b[i_l-1]：
        # 原 if 分支：
        #   a[i_l-1] = a[i_l]
        #   a[i_r+1] = b[i_l-1] - a[i_l]
        # => 令 b[i_l-1] = a[i_l-1] + a[i_r+1]
        b[i_l - 1] = a[i_l - 1] + a[i_r + 1]
        i_l -= 1
        i_r += 1

    # 从这里开始执行原始逻辑，验证并输出生成的 a（应与构造时相同）
    a_reconstructed = [0] * n

    l = n // 2 - 1
    r = n // 2

    a_reconstructed[l] = b[l] // 2
    a_reconstructed[r] = b[l] - a_reconstructed[l]

    while l > 0:
        if b[l - 1] >= b[l]:
            a_reconstructed[l - 1] = a_reconstructed[l]
            a_reconstructed[r + 1] = b[l - 1] - a_reconstructed[l]
        else:
            a_reconstructed[r + 1] = a_reconstructed[r]
            a_reconstructed[l - 1] = b[l - 1] - a_reconstructed[r]
        l -= 1
        r += 1

    # 输出 b 和最终求得的 a
    print("n =", n)
    print("b:", *b)
    print("a:", *a_reconstructed)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(6)