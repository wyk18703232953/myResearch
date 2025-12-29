import random

def main(n):
    # 生成规模为 2n 的测试数据（原程序中实际使用的 n 是输入的一半）
    # 这里生成 2n 个 0~100 之间的随机整数
    a = [random.randint(0, 100) for _ in range(2 * n)]

    # 以下是原逻辑，将原始的 n=int(input())//2 替换为使用参数 n
    b = [0] * n
    a.reverse()
    for i in a:
        b.append(i)
    mem = b[-1]
    c = 0
    for i in range(n - 1):
        if b[-2 - i] - c > mem:
            c = b[-2 - i] - mem
        b[-2 - i] -= c
        b[1 + i] += c
        mem = b[-2 - i]
    for i in b:
        print(i, end=' ')

# 示例调用
if __name__ == "__main__":
    main(5)