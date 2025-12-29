import random

def main(n):
    # 根据规模 n 生成测试数据：长度为 n 的整数数组
    # 这里生成范围在 [-n, n] 的随机整数，可按需要调整
    a = [random.randint(-n, n) for _ in range(n)]

    s = set(a)
    s.discard(0)
    print(len(s))

if __name__ == "__main__":
    # 示例：调用 main(10)，实际使用时可根据需要修改 n
    main(10)