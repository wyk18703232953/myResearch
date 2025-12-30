import random

def main(n):
    # 根据规模 n 生成测试数据
    # 这里生成 s 为 [1, 10^6] 之间的随机整数（可按需调整规则）
    s = random.randint(1, 10**6)

    count = 0
    for i in range(n):
        count += s // (n - i)
        s -= (s // (n - i)) * (n - i)
    print(count)


if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可按需修改 n
    main(10)