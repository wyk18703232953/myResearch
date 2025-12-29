import math
import random

def main(n):
    # 生成测试数据：
    # 随机生成 d，再生成长度为 n 的数组 p
    # 可以根据需要调整数据规模和范围
    d = random.randint(1, 10)
    p = [random.randint(0, 100) for _ in range(n)]

    # 原逻辑开始
    q = []
    for i in range(len(p) - 1):
        q.append(abs(p[i + 1] - p[i]))
    count = 0
    for k in q:
        if k == 2 * d:
            count += 1
        elif k >= 2 * d:
            count += 2

    result = count + 2

    # 输出或返回结果，这里返回以便在其他程序中复用
    return {
        "d": d,
        "p": p,
        "result": result
    }

# 示例：直接运行本文件时进行一次调用
if __name__ == "__main__":
    n = 10  # 示例规模，可自行修改
    output = main(n)
    print("d:", output["d"])
    print("p:", output["p"])
    print("result:", output["result"])