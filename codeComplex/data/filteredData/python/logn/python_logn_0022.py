import random

def main(n: int):
    # 生成两个随机正整数，范围根据 n 调整（用于控制数据规模）
    # 这里将随机数上限设置为 2^n - 1，保证二进制位数不超过 n
    if n <= 0:
        return

    max_val = (1 << n) - 1
    a = random.randint(0, max_val)
    b = random.randint(0, max_val)

    # 保持与原逻辑相同
    a, b = min(a, b), max(a, b)
    A = bin(a)[2:]
    B = bin(b)[2:]
    A = "0" * (len(B) - len(A)) + A
    diff = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            diff = len(A) - i
            break

    print((2 ** diff) - 1)


if __name__ == "__main__":
    # 示例：规模 n = 10，可根据需要修改
    main(10)