import random

def main(n: int):
    # 生成测试用例数量 t，这里设为 n（可根据需要调整规则）
    t = n

    for _ in range(t):
        # 对于每个测试用例，生成长度为 n 的数组 a
        # 元素范围设为 [0, n]，可根据需要调整
        a = [random.randint(0, n) for _ in range(n)]
        a.sort()
        if a[-2] > n - 2:
            print(n - 2)
        else:
            print(a[-2] - 1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n 的默认值
    main(5)