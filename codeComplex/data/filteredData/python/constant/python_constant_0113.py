def main(n: int):
    """
    规模 n 用于生成一个整数测试数据：
    - 当 n 为偶数：生成一个负数，其绝对值等于 n 的平方，如 -n*n
    - 当 n 为奇数：生成一个负数，其绝对值为 n*10 + 3（两位末尾便于测试删除操作）
    然后对这个整数执行原逻辑。
    """

    # 1. 生成测试数据 s（字符串形式的整数）
    if n <= 0:
        # 给一个固定的负数测试
        s = "-10"
    else:
        if n % 2 == 0:
            val = -n * n
        else:
            # 确保至少两位数，方便末两位删除逻辑
            val = -(n * 10 + 3)
        s = str(val)

    # 2. 原逻辑开始
    neg = 0
    if int(s) < 0:
        neg = 1

    ans1 = ""
    s_int = int(s)
    s_abs_str = str(abs(s_int))
    ans2 = ""

    for i in range(0, len(s_abs_str)):
        if i == len(s_abs_str) - 2:
            ans1 += s_abs_str[i]
        elif i == len(s_abs_str) - 1:
            ans2 += s_abs_str[i]
        else:
            ans1 += s_abs_str[i]
            ans2 += s_abs_str[i]

    if neg == 0:
        print(s_abs_str)
    else:
        if str(min(int(ans1), int(ans2))) == "0":
            print(0)
        else:
            print("-" + str(min(int(ans1), int(ans2))))


if __name__ == "__main__":
    # 示例调用：规模 n = 10
    main(10)