import random

def main(n: int):
    # 生成测试数据：1..n 的随机排列
    N = n
    ml = list(range(1, N + 1))
    random.shuffle(ml)

    kl = [0 for _ in range(N)]

    k = 0
    for i in range(N):
        if kl[i] == 0:
            kl[i] = 1
            j = ml[i]
            k += 1
            while kl[j - 1] == 0:
                kl[j - 1] = 1
                j = ml[j - 1]

    if k % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：可以在此处修改规模 n
    main(10)