import sys
import random

def main(n: int):
    # 生成测试数据：这里简单地设 m = n，必要时可按需修改生成规则
    m = n

    # 原逻辑开始
    for i in range(n // 2 + n % 2):
        x1 = i + 1
        x2 = n - i
        if x1 == x2:
            for j in range(m // 2 + m % 2):
                if j + 1 == m - j:
                    sys.stdout.write(str(x1) + " " + str(j + 1) + "\n")
                else:
                    sys.stdout.write(str(x1) + " " + str(j + 1) + "\n")
                    sys.stdout.write(str(x2) + " " + str(m - j) + "\n")
        else:
            if i % 2 == 0:
                for j in range(m):
                    sys.stdout.write(str(x1) + " " + str(j + 1) + "\n")
                    sys.stdout.write(str(x2) + " " + str(m - j) + "\n")
            else:
                for j in range(m):
                    sys.stdout.write(str(x1) + " " + str(m - j) + "\n")
                    sys.stdout.write(str(x2) + " " + str(j + 1) + "\n")


if __name__ == "__main__":
    # 示例：调用 main(5)，实际使用时可按需修改或从其他模块调用 main(n)
    main(5)