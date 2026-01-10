def main(n):
    # n 作为输入规模：构造长度为 n 的排列 ml
    N = n
    if N <= 0:
        return

    # 构造一个确定性的排列 ml：简单轮转
    # 例如 N=5 -> [2,3,4,5,1]
    ml = [((i + 1) % N) + 1 for i in range(N)]

    kl = [0 for _ in range(N)]

    k = 0
    for i in range(N):
        if kl[i] == 0:
            kl[i] = 1
            j = ml[i]
            k = k + 1
            while kl[j - 1] == 0:
                kl[j - 1] = 1
                j = ml[j - 1]

    if k % 2 == 0:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    main(10)