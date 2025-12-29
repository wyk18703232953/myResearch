import random

def main(n: int):
    # 1. 生成测试数据：长度为 n 的整数数组 a
    #   这里生成 1 到 100 之间的随机整数，可按需修改规则
    a = [random.randint(1, 100) for _ in range(n)]

    # 2. 原始逻辑
    s = sum(a)
    new = 0
    i = 0

    # 注意避免 n=0 的情况导致索引越界
    while i < n and 2 * (new + a[i]) < s:
        new += a[i]
        i += 1

    # 输出结果
    print(i + 1 if n > 0 else 0)


if __name__ == "__main__":
    # 示例：运行规模为 10
    main(10)