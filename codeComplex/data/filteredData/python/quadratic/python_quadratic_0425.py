import random

def main(n: int):
    # 生成长度为 n 的数字串作为测试数据，这里用随机的 0~9
    s = ''.join(str(random.randint(0, 9)) for _ in range(n))

    l = []
    total = 0
    p = 0
    for i in range(0, 450):
        sum1 = 0
        flag = 1
        r = 0
        for k in range(n):
            sum1 = sum1 + int(s[k])
            if sum1 > i:
                flag = 0
            if sum1 == i:
                sum1 = 0
                r = r + 1
        if r >= 2 and sum1 == 0 and flag == 1:
            print("YES")
            p = 1
            break
    if p == 0:
        print("NO")


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)