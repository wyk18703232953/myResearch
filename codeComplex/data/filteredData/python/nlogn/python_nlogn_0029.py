import random

def main(n: int):
    # 1. 生成规模为 n 的测试数据（整数序列）
    #    这里设定元素范围为 [-10^9, 10^9]
    sequence = [random.randint(-10**9, 10**9) for _ in range(n)]

    # 2. 原逻辑：找到 second order statistics
    firstOrderStatistics = min(sequence)
    if sequence.count(firstOrderStatistics) == len(sequence):
        print("NO")
    else:
        sequence = sorted(sequence)
        secondOrderStatistics = sequence[0]
        for i in sequence:
            if i > secondOrderStatistics:
                secondOrderStatistics = i
                break
        print(secondOrderStatistics)


if __name__ == "__main__":
    # 示例：调用 main，指定规模 n
    main(10)