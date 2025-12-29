import random

def main(n: int):
    # 生成规模为 n 的测试数据：随机整数列表
    # 这里生成范围在 1~100 的整数，你可按需修改
    lst = [random.randint(1, 100) for _ in range(n)]

    evens = []
    odds = []

    for e, x in enumerate(lst):
        if x % 2 == 0:
            evens.append(e + 1)
        else:
            odds.append(e + 1)

    if len(evens) < len(odds):
        print(evens[0])
    else:
        print(odds[0])

if __name__ == "__main__":
    # 示例：运行时指定一个 n
    main(10)