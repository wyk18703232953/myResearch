import random

def main(n):
    # 生成测试数据：n 个非负整数，范围可自行调整
    x = [random.randint(0, 10**6) for _ in range(n)]
    
    x.sort()
    count, count2 = 0, 0
    ans = 1
    for i in range(n):
        count += x[i] - i
        if i >= 2 and x[i] == x[i - 1] == x[i - 2]:
            ans = 0
        if i >= 2 and x[i] == x[i - 1] == x[i - 2] + 1:
            ans = 0
        if i >= 1 and x[i] == x[i - 1]:
            count2 += 1
    if n >= 3 and x[0] == x[1] == 0:
        ans = 0
    for i in range(n):
        if x[i] > 0:
            break
        if i == n - 1:
            ans = 0

    if ans == 0 or count % 2 == 0 or count2 > 1:
        print("cslnb")
    else:
        print("sjfnb")


if __name__ == "__main__":
    # 示例：运行规模为 5 的测试
    main(5)