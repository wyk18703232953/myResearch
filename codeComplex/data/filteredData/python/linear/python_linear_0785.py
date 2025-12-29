import random

def main(n):
    # 生成测试数据：长度为 n 的非负整数数组
    # 这里生成范围为 [0, n] 的随机整数，可按需求自行调整
    a = [random.randint(0, n) for _ in range(n)]

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