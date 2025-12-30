import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据
    # 这里生成一个包含 n 个非负整数的数组，数值范围可按需调整
    # 为了贴近原逻辑，生成 0 ~ 2n 之间的随机整数
    arr = [random.randint(0, 2 * n) for _ in range(n)]

    # 2. 原始逻辑
    arr1 = [arr[0]]
    m = -1
    for i, v in enumerate(arr):
        if v > m + 1:
            print(i + 1)
            break
        m = max(m, v)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(10) 进行测试
    main(10)