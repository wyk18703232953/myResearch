import random

def main(n: int):
    # n 作为 test 的规模：即有 n 组数据
    test = n

    first = []
    for _ in range(test):
        # 根据 n 生成每组测试数据，这里生成长度为 n 的随机整数列表
        list_ = [random.randint(0, 100) for _ in range(n)]
        sum_ = sum(list_)
        first.append(sum_)

    first_sum = first[0]
    count = 0
    for value in first:
        if first_sum < value:
            count += 1

    print(count + 1)


if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改
    main(5)