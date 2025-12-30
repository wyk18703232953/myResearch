import math
import random

def main(n):
    # 生成规模为 n 的测试数据：a 为长度为 n 的整数列表
    # 这里随机构造到达时间，范围可根据需要调整
    q = n
    a = [random.randint(0, 10**9) for _ in range(q)]

    earliest_time = 10**9 + 1000
    earliest_queue = 1

    for i in range(q):
        cycles = int(max(0, math.ceil((a[i] + 1 - (i + 1)) / q)))
        t = (i + 1) + cycles * q
        if t < earliest_time:
            earliest_time = t
            earliest_queue = i + 1

    print(earliest_queue)


if __name__ == "__main__":
    # 示例：使用 n=10 作为规模运行
    main(10)