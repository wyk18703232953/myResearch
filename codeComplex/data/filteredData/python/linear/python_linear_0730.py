import random

def main(n):
    # 生成测试数据：随机选择 1 <= k <= n
    k = random.randint(1, n)

    strr = ""
    while len(strr) < n:
        strr += "0" * ((n - k) // 2) + "1"
    strr = strr[:n]
    print(strr)

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)