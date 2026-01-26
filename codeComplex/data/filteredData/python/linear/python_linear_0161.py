def main(n):
    # n 表示输入规模，这里解释为元素个数
    # 构造一个确定性的序列 E，包含 n 个整数
    # 模式：前 half 个为 i % 5，后半部分为 (i % 5) + 5
    half = n // 2
    E = [i % 5 for i in range(half)] + [(i % 5) + 5 for i in range(n - half)]

    D = {}
    for e in E:
        D[e] = D.get(e, 0) + 1
    result = []
    for e in E:
        result.append(D[e])
    # 输出结果以便保持原程序行为
    for v in result:
        # print(v)
        pass
    return result

if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)