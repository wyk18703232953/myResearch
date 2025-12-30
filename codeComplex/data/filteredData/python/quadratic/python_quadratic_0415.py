def main(n: int):
    # 生成测试数据：长度为 n 的周期串，例如 "ababab..."
    # 保证有一定的前后缀结构，方便测试 KMP 逻辑
    base = "ab"
    s = "".join(base[i % len(base)] for i in range(n))

    # 这里自定义 k，可按需要调整或根据 n 生成
    # 示例：令 k = 3
    k = 3

    fail = [-1] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        j = fail[i - 1]
        while j != -1 and s[i - 1] != s[j]:
            j = fail[j]
        fail[i] = j + 1

    f1 = fail[-1]
    result = s + s[f1:] * (k - 1)
    print(result)


if __name__ == "__main__":
    # 示例调用：n = 10
    main(10)