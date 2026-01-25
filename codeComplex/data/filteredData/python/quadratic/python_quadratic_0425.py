def main(n):
    # 生成确定性输入：n 位数字串，周期性重复 "1234567890"
    if n <= 0:
        print("NO")
        return

    s = ''.join(str((i % 10)) for i in range(1, n + 1))

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
    # 示例：运行若干不同规模，便于做时间复杂度实验
    for size in (10, 50, 100, 200, 400):
        print(f"n = {size}")
        main(size)