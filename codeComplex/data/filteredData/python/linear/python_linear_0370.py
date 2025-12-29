import random

def main(n: int):
    # 1. 生成测试数据
    # 假设 c 和 a 中的元素是 1~100 的整数
    # m 的规模与 n 相同，这里可根据需要调整
    m = n

    # 生成递增或随机序列都可以，这里使用随机序列
    c = [random.randint(1, 100) for _ in range(n)]
    a = [random.randint(1, 100) for _ in range(m)]

    # 2. 原逻辑实现
    x = 0
    for i in range(n):
        try:
            if a[0] >= c[i]:
                x += 1
                a.pop(0)
        except IndexError:
            # a 为空时跳出
            pass

    print(x)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)