def main(n):
    from sys import stdout

    # 根据 n 确定性生成 N, M
    # 让 N 和 M 都与 n 同阶，以便做规模实验
    if n <= 0:
        return
    N = n
    M = n + (n % 2)  # 若 n 为奇数，M 为偶数；若 n 为偶数，M 为偶数+0 => M 与 n 同阶且多为偶数

    if M % 2 == 0 and N % 2 == 0:
        for m in range(1, M // 2 + 1):
            for x in range(1, N + 1):
                stdout.write(str(x) + " " + str(m) + "\n")
                stdout.write(str(N + 1 - x) + " " + str(M + 1 - m) + "\n")
    elif M % 2 == 0 and N % 2 == 1:
        for m in range(1, M // 2 + 1):
            for i in range(1, N + 1):
                stdout.write(str(i) + " " + str(m) + "\n")
                stdout.write(str(N + 1 - i) + " " + str(M + 1 - m) + "\n")
    else:
        for m in range(1, (M + 1) // 2):
            for x in range(1, N + 1):
                stdout.write(str(x) + " " + str(m) + "\n")
                stdout.write(str(N + 1 - x) + " " + str(M + 1 - m) + "\n")
        if N % 2 == 0:
            for i in range(1, N // 2 + 1):
                stdout.write(str(i) + " " + str((M + 1) // 2) + "\n")
                stdout.write(str(N + 1 - i) + " " + str((M + 1) // 2) + "\n")
        else:
            for i in range(1, (N + 1) // 2):
                stdout.write(str(i) + " " + str((M + 1) // 2) + "\n")
                stdout.write(str(N + 1 - i) + " " + str((M + 1) // 2) + "\n")
            stdout.write(str((N + 1) // 2) + " " + str((M + 1) // 2) + "\n")


if __name__ == "__main__":
    # 示例调用：输入规模 n，可根据需要修改
    main(10)