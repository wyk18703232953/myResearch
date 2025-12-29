import random

def main(n):
    # 1. 生成测试数据：随机生成 k，范围可根据需要调整
    # 这里设为 [-n, n]，保证规模相关
    k = random.randint(-n, n)

    dul = 0
    sum1 = 0

    if k == 0:
        for i in range(n - 1, -1, -1):
            sum1 += 1
            dul += sum1
            if dul == i:
                print(i)
                break
    else:
        for i in range(n - 1, -1, -1):
            sum1 += 1
            dul += sum1
            if dul - i == k:
                print(i)
                break

if __name__ == "__main__":
    # 示例：规模 n 自行设定
    main(10)