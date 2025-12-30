import random

def main(n: int):
    # 生成规模为 n 的测试数据
    # 原代码中第一行 p 未被使用，这里将其设为 n 以保持结构含义
    p = n
    # 生成 n 个随机整数，范围可根据需要调整
    arr = [random.randint(1, 100) for _ in range(p)]

    # 原逻辑
    arr.sort(reverse=True)
    d = 0
    for x in arr:
        d += x
    c = 0
    num = 0
    while c <= d / 2:
        c += arr[num]
        num += 1
    print(num)


if __name__ == "__main__":
    # 示例：调用 main，规模为 10
    main(10)