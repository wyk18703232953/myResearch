import random

def main(n):
    # 生成测试数据
    # 当 n == 1 时，原程序按字符串处理，这里用整数转字符串代替
    if n == 1:
        a = str(random.randint(-10**9, 10**9))
        print(a)
        return

    # n > 1 时，生成长度为 n 的整数数组
    a = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 以下为原逻辑
    b = [abs(i) for i in a]
    if min(a) * max(a) > 0:
        print(sum(b) - 2 * min(b))
    else:
        print(sum(b))


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可按需修改 n
    main(5)