import random

def main(n):
    # 生成测试数据
    # 这里的规则可以按需要调整：
    # l, r 为总和限制；x 为最大值和最小值差值限制
    # a 为难度数组（正整数）
    a = [random.randint(1, 10**3) for _ in range(n)]
    l = random.randint(1, n * 500)
    r = random.randint(l, n * 1000)
    x = random.randint(0, 10**3)

    count = 0
    # 遍历所有非空子集
    for mask in range(1, 1 << n):
        temp = []
        for j in range(n):
            if mask & (1 << j):
                temp.append(a[j])

        if temp:
            s = sum(temp)
            if l <= s <= r and max(temp) - min(temp) >= x:
                count += 1

    print(count)
    return count

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可根据需要调整
    main(5)