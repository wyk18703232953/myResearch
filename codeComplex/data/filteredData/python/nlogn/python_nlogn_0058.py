import random

def main(n: int):
    # 根据 n 生成测试数据，这里生成 n 个 [1, 100] 的随机整数
    lst = [random.randint(1, 100) for _ in range(n)]

    # 原始逻辑
    lst.sort()
    lst.reverse()
    m = 0
    for i in range(n):
        if sum(lst[:i]) > sum(lst[i:]):
            break
        else:
            m += 1

    print(m)


if __name__ == "__main__":
    # 示例：以 n = 10 运行
    main(10)