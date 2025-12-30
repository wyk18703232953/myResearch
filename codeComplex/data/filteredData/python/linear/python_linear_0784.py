import random

def main(n: int):
    # 1. 生成测试数据：生成 n 个随机非负整数
    # 根据原题意（类似 cf "cslnb/sjfnb" 问题），元素为非负整数即可
    a = [random.randint(0, 10**6) for _ in range(n)]

    # 原逻辑开始
    a = sorted(a)
    duplicates = {}
    d = None
    delta = 0

    for i, el in enumerate(a, 1):
        if el not in duplicates:
            duplicates[el] = 0
        else:
            d = el
            duplicates[el] += 1
        min_value = i - 1
        delta += el - min_value

    if sum(duplicates.values()) > 1 or duplicates.get(0, 0) >= 1 or (d is not None and d - 1 in duplicates):
        print('cslnb')
    elif delta == 0:
        print('cslnb')
    elif delta % 2 == 1:
        print('sjfnb')
    else:
        print('cslnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)