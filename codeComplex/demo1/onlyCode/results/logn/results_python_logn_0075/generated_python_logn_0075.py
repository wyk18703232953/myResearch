def number(pos):
    ans = 0
    for i in range(pos + 1):
        ans += 2 ** i
    return ans


def main(n):
    """
    规模 n 用来生成测试数据：
    这里约定：
    - 生成两个整数 l, r
    - l = n
    - r = 2 * n + 1  （确保一般情况下 l != r，且有一定二进制差异）
    你可以根据需要修改生成逻辑。
    """
    l = n
    r = 2 * n + 1

    if l == r:
        print(0)
    else:
        b_pos = 0
        i = 0
        while l > 0 or r > 0:
            if (l % 2) != (r % 2):
                b_pos = i
            l >>= 1
            r >>= 1
            i += 1
        print(number(b_pos))


# 示例：运行 main(10) 可查看结果
if __name__ == "__main__":
    main(10)