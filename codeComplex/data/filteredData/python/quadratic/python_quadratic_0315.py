import random

def main(n):
    # 生成测试数据：k 在 [1, n] 范围内，数组元素为随机整数
    k = random.randint(1, n)
    li = [random.randint(-1000, 1000) for _ in range(n)]

    ans = []
    for i in range(0, n):
        su = 0
        for j in range(i, n):
            su += li[j]
            if j - i + 1 >= k:
                ans.append(su / (j - i + 1))
    print(max(ans))


if __name__ == "__main__":
    # 示例：可根据需要修改 n 的规模
    main(10)