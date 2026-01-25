def main(n):
    # 映射规则：
    # 原程序输入为：
    #   n, m
    #   c: 长度为 m 的字符串列表，每个元素是 1..n 的整数
    # 这里我们使用传入的 n 作为原程序的 m（列表长度），
    # 并固定原来的 n 为 10，使规模随 m 线性变化，且保持行为可重复。
    orig_n = 10
    m = n

    # 生成确定性的 c：使 1..orig_n 周期性出现
    c = [(i % orig_n) + 1 for i in range(m)]
    # 转为字符串列表以匹配原程序 c 的形式
    c_str = [str(x) for x in c]

    col = [0] * orig_n
    for i in range(len(c_str)):
        col[int(c_str[i]) - 1] += 1
    print(min(col))


if __name__ == "__main__":
    main(20)