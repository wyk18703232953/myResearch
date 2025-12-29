import random

def main(n):
    # 根据规模 n 生成测试数据，这里假设为 [-10^n, 10^n] 范围内的一个随机整数
    if n <= 0:
        test_value = 0
    else:
        low = -10 ** n
        high = 10 ** n
        test_value = random.randint(low, high)

    x = test_value

    if x > 0:
        print(x)
    else:
        l = list(str(x))

        last = l[0:len(l) - 1]
        second = l[0:len(l) - 2]
        second += l[-1]

        lR = "".join(last)
        sR = "".join(second)

        print(max(eval(lR), eval(sR)))


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(3)