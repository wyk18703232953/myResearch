import math
import random

def main(n):
    # 生成测试数据：
    # sone: 长度 n，由'+'和'-'组成
    # stwo: 长度 n，由'+', '-', '?'组成
    choices_sone = ['+', '-']
    choices_stwo = ['+', '-', '?']
    sone = [random.choice(choices_sone) for _ in range(n)]
    stwo = [random.choice(choices_stwo) for _ in range(n)]

    # 原逻辑开始
    sum1 = 0
    sum2 = 0
    m = 0  # 在原代码中只加不使用，保持以防逻辑依赖（其实无用）

    for i in range(len(sone)):
        if sone[i] == '+':
            sum1 = sum1 + 1
            m = m + 1
        else:
            sum1 = sum1 - 1

    k = 0
    for i in range(len(stwo)):
        if stwo[i] == '+':
            sum2 = sum2 + 1
        elif stwo[i] == '-':
            sum2 = sum2 - 1
        elif stwo[i] == '?':
            k = k + 1

    if (k - (abs(sum1 - sum2))) < 0:
        result = float(0)
    elif (k - (abs(sum1 - sum2))) == 0:
        if k == 0:
            result = float(1)
        else:
            result = float(pow(0.5, k))
    else:
        n_val = k - (abs(sum1 - sum2))
        n_val = abs(sum1 - sum2) + n_val / 2
        if abs(sum1 - sum2) == 0:
            result = float(
                (math.factorial(k) / (math.factorial(k // 2) * math.factorial(k // 2)))
                * pow(0.5, k)
            )
        else:
            result = float(
                (math.factorial(k) / (math.factorial(k - int(n_val)) * math.factorial(int(n_val))))
                * pow(0.5, k)
            )

    print(result)


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)