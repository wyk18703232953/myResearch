def main(n):
    # 输入结构分析：
    # 原程序：
    # n: 一个整数
    # 第二行: n 个整数
    #
    # 我们将 n 直接映射为数组长度
    # 构造一个确定性的整数数组 a，长度为 n
    # 使用简单算术生成：a[i] = i + 1
    # 这样可规模化、可重复且无随机性
    a = sorted([i + 1 for i in range(n)])
    s = []
    for q in a:
        for q1 in s:
            if q % q1 == 0:
                break
        else:
            s.append(q)
    print(len(s))


if __name__ == "__main__":
    # 示例调用，可根据需要修改 n 观察时间复杂度
    main(10)