def main(n: int):
    # 1. 生成规模为 n 的测试数据 A
    # 生成一个简单的递增数组，例如 [1, 2, ..., n]
    # 也可以根据需要改成随机数据等
    A = list(range(1, n + 1))

    # 2. 按原逻辑处理
    A.sort()
    if A[-1] == 1:
        A[-1] = 2
    else:
        A[-1] = 1
        A.sort()

    # 3. 输出结果
    print(*A)


if __name__ == "__main__":
    # 示例调用：可按需要修改 n
    main(5)