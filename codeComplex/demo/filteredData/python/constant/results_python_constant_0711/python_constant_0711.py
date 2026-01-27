def main(n):
    # 根据 n 生成测试数据：这里构造 v 为 1..n 的某个值
    # 你可以根据需要修改生成规则
    v = n  # 示例：令 v = n

    f = lambda x: x * (x + 1) // 2
    ans = min(n - 1, v) + f(n - min(n - 1, v)) - 1
    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)