import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据：k 为 [1, n] 范围内的正整数
    k = random.randint(1, max(1, n))

    a = 9
    for i in range(1, 12):
        if k <= a * i:
            a = (a // 9) + (k // i) - 1
            if k % i != 0:
                b = str(a + 1)
                c = (k % i) - 1
                print(b[c])
            else:
                b = str(a)
                print(b[-1])
            break
        else:
            k = k - a * i
            a = a * 10


if __name__ == "__main__":
    # 示例：调用 main，规模 n 可以根据需要进行调整
    main(1000)