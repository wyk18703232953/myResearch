import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组，元素取值范围 [1, 100]
    arr = [random.randint(1, 100) for _ in range(n)]

    # 原逻辑开始
    arr.sort()
    if arr[-1] == 1:
        arr[-1] = 2
    else:
        arr[-1] = 1
    arr.sort()
    print(*arr)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)