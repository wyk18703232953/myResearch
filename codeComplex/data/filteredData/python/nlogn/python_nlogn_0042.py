import random

def main(n):
    # 生成测试数据：长度为 n 的正整数数组
    # 约束：保证可以取 max(arr)，且后续逻辑不会出错
    # 这里简单生成 1~10 之间的随机整数
    if n <= 0:
        return

    arr = [random.randint(1, 10) for _ in range(n)]

    # 原逻辑开始
    mx = max(arr)
    if mx == 1:
        x = 2
    else:
        x = 1

    # 注意：原代码是 arr.remove(mx)，仅删除一个最大值
    arr.remove(mx)
    arr.append(x)
    arr.sort()

    # 输出结果
    print(*arr)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)