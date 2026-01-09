def main(n):
    # 生成测试数据：k 在 [1, 2^n - 1] 范围内
    # 这里选取一个示例规则：k = 2^(n-1) - 1，当 n=1 时特殊处理
    if n <= 0:
        return
    if n == 1:
        k = 1

    else:
        k = (1 << (n - 1)) - 1

    pre, post = [], []
    k -= 1
    v = 1
    for i in range(n - 2, -1, -1):
        if k & (1 << i):
            post.append(v)

        else:
            pre.append(v)
        v += 1

    # 输出与原程序相同的格式
    # print(*pre, n, *reversed(post))
    pass
if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值
    main(5)