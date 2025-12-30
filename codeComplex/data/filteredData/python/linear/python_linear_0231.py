import random

def main(n):
    # 生成测试数据：长度为 n 的由 'x' 和 'y' 组成的字符串
    a = n
    b = ''.join(random.choice('xy') for _ in range(a))

    s = 0
    for i in range(a - 2):
        if b[i:i+3] == 'xxx':
            s += 1

    print(s)


if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)