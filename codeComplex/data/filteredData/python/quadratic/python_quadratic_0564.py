from sys import stdout

def main(n):
    # 根据规模 n 生成测试数据，这里简单设定：
    # N = n, M = n（你也可以根据需求改成其他关系）
    N = n
    M = n

    if M % 2 == 0 and N % 2 == 0:
        for m in range(1, M // 2 + 1):
            for x in range(1, N + 1):
                # stdout.write(str(x) + ' ' + str(m) + '\n')
                # stdout.write(str(N + 1 - x) + ' ' + str(M + 1 - m) + '\n')
                pass
    elif M % 2 == 0 and N % 2 == 1:
        for m in range(1, M // 2 + 1):
            for i in range(1, N + 1):
                # stdout.write(str(i) + ' ' + str(m) + '\n')
                # stdout.write(str(N + 1 - i) + ' ' + str(M + 1 - m) + '\n')
                pass

    else:
        for m in range(1, (M + 1) // 2):
            for x in range(1, N + 1):
                # stdout.write(str(x) + ' ' + str(m) + '\n')
                # stdout.write(str(N + 1 - x) + ' ' + str(M + 1 - m) + '\n')
                pass
        if N % 2 == 0:
            for i in range(1, N // 2 + 1):
                # stdout.write(str(i) + ' ' + str((M + 1) // 2) + '\n')
                # stdout.write(str(N + 1 - i) + ' ' + str((M + 1) // 2) + '\n')
                pass

        else:
            for i in range(1, (N + 1) // 2):
                # stdout.write(str(i) + ' ' + str((M + 1) // 2) + '\n')   
                # stdout.write(str(N + 1 - i) + ' ' + str((M + 1) // 2) + '\n')
                pass
            # stdout.write(str((N + 1) // 2) + ' ' + str((M + 1) // 2) + '\n')  


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)