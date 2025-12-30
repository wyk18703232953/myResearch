import random

def main(n: int):
    # 生成测试数据：长度为 n 的整数数组 a
    # 这里生成 0 到 2n 之间的随机整数，可能含重复
    a = [random.randint(0, 2 * n) for _ in range(n)]

    total = sum(a)
    final = n * (n - 1) // 2
    repeated = []
    count = {}

    for i in a:
        try:
            count[i] += 1
            repeated.append(i)
        except KeyError:
            count[i] = 1

    moves = total - final

    if len(repeated) > 1:
        print('cslnb')
    elif 0 in repeated:
        print('cslnb')
    elif len(repeated) == 1 and repeated[0] - 1 in a:
        print('cslnb')
    else:
        if moves % 2 == 0 or moves <= 0:
            print('cslnb')
        else:
            print('sjfnb')


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)