import random

def main(n: int):
    # 生成测试数据：长度为 n 的非负整数数组
    # 这里生成 0 到 n 范围内的随机数，可根据需要调整
    ai = [random.randint(0, n) for _ in range(n)]

    ai.sort()
    num = 0
    num2 = 0
    for i in range(1, n):
        if ai[i - 1] == ai[i]:
            num += 1
            num2 = i

    if num == 0:
        num3 = sum(ai)
        num4 = n * (n - 1) // 2
        ans = (num3 - num4) % 2
        if ans == 1:
            print("sjfnb")
        else:
            print("cslnb")
    elif num == 1:
        if (num2 > 1 and ai[num2 - 2] == ai[num2] - 1) or ai[num2] == 0:
            print("cslnb")
        else:
            num3 = sum(ai)
            num4 = n * (n - 1) // 2
            ans = (num3 - num4) % 2
            if ans == 1:
                print("sjfnb")
            else:
                print("cslnb")
    else:
        print("cslnb")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)