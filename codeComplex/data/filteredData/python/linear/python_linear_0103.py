def main(n: int):
    import random
    import string

    # 1. 根据规模 n 生成测试数据：
    #    长度在 [1, n] 之间的随机小写字母串 a、b
    len_a = max(1, n // 2)
    len_b = max(1, n - len_a)

    letters = string.ascii_lowercase
    a = ''.join(random.choice(letters) for _ in range(len_a))
    b = ''.join(random.choice(letters) for _ in range(len_b))

    # 2. 按原逻辑计算答案
    p = []
    for i in range(len(a)):
        for j in range(len(b)):
            ok = a[:i + 1] + b[:j + 1]
            p.append(ok)
    ans = min(p)

    # 3. 输出结果（如果需要也可一起打印 a, b）
    print(ans)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)