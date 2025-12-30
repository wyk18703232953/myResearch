import random

def main(n):
    # 生成测试数据：n 个整数，范围 -999999 到 999999，排除 0
    a = []
    for _ in range(n):
        x = random.randint(-999999, 999999)
        if x == 0:
            x = 1
        a.append(x)

    c = 0
    po = [0] * 1000000
    ne = [0] * 1000000

    for i in range(n):
        if a[i] < 0 and ne[-a[i]] != 1:
            c += 1
            ne[-a[i]] = 1
        elif a[i] > 0 and po[a[i]] != 1:
            c += 1
            po[a[i]] = 1

    print(c)

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)