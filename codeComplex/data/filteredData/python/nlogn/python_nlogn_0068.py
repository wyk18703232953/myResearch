import random

def main(n):
    # 生成规模为 n 的测试数据，这里生成 1~100 之间的随机整数
    list1 = [random.randint(1, 100) for _ in range(n)]

    sum2 = 0
    sum1 = 0
    count = 0
    list1.sort(reverse=True)

    for i in range(len(list1)):
        sum1 = sum1 + list1[i]

    for i in range(len(list1)):
        if int(sum1 / 2) >= sum2:
            sum2 = sum2 + list1[i]
            count = count + 1

    print(count)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)