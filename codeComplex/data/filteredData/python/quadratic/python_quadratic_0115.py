import random

def main(n: int) -> int:
    # 生成测试数据：m 次操作，每次随机选择 1..n 之间的一个位置
    # 这里设定 m = n * n，可按需要调整规模
    m = n * n
    tL0 = [random.randint(1, n) for _ in range(m)]

    tL = [0] * n
    score = 0

    for i in range(m):
        tL[tL0[i] - 1] += 1
        if 0 not in tL:
            score += 1
            for j in range(n):
                tL[j] -= 1

    return score

if __name__ == "__main__":
    # 示例：运行规模为 5，并打印结果
    print(main(5))