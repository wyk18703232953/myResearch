def main(n):
    # 映射：n 为测试用例数量
    # 对于第 i 个测试用例：
    #   f_i = i
    #   t_i = i * 2
    # 初始 s 为 n
    s = n
    ans = s
    for i in range(n):
        f = i
        t = i * 2
        if t > (s - f):
            delta = t - (s - f)
            ans += delta
            s += delta
    return ans


if __name__ == "__main__":
    # 示例调用
    # print(main(10))
    pass