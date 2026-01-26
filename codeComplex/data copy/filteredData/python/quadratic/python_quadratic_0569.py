import math
from collections import defaultdict

def main(n):
    # 解释：将原来的 n, m 输入结构映射为 (n, m) = (n, n)
    # 这样输入规模由一个参数 n 控制为 n×n 的网格大小
    m = n

    up, down = 1, n
    count = 0
    total = n * m
    outputs = []

    while up <= down:
        left, right = 1, m
        while left <= m and count < total:
            if count < total:
                outputs.append((up, left))
            count += 1
            left += 1
            if count < total:
                outputs.append((down, right))
            count += 1
            right -= 1

        up += 1
        down -= 1

    # 为了保持与原程序“输出所有坐标”的行为一致，
    # 在此将结果真正打印出来
    for x, y in outputs:
        # print(f"{x} {y}")
        pass
if __name__ == "__main__":
    # 示例：以 n=5 运行主函数进行时间复杂度实验
    main(5)