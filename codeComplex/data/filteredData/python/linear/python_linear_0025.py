import random

def main(n):
    # 生成测试数据：长度为 n 的随机正整数列表（1~100）
    li = [random.randint(1, 100) for _ in range(n)]

    lis = [x % 2 for x in li]
    if lis.count(0) > lis.count(1):
        print(lis.index(1) + 1)
    else:
        print(lis.index(0) + 1)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)