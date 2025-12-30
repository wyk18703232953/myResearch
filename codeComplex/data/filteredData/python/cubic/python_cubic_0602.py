import random

def min_sub_array(day, k):
    if not day:
        return [0] * (k + 1)
    n = len(day)
    best = [float('inf')] * (n + 1)
    best[0] = 0
    best[1] = 1
    for size in range(2, n + 1):
        for i in range(n + 1 - size):
            best[size] = min(best[size], day[i + size - 1] - day[i] + 1)
    output = [0] * (k + 1)
    for i in range(k + 1):
        if n - i > 0:
            output[i] = best[n - i]
    return output


def main(n):
    # 生成规模参数：
    # N: 行数（原先多天）
    # M: 每行长度
    # K: 最大“删掉的 1 的数量”规模
    # 这里简单设定：
    N = max(1, n // 3)
    M = max(1, n)
    K = min(5, M)  # 避免 K 过大，可根据需要调整

    # 生成测试数据：N 行，每行长度为 M，由 '0'/'1' 组成
    # 保证至少有一行有 '1'，以覆盖逻辑
    lines = []
    has_one = False
    for _ in range(N):
        line = ''.join(random.choice('01') for _ in range(M))
        if '1' in line:
            has_one = True
        lines.append(line)
    if not has_one:
        # 如果全部为0，则强制在第一行放一个1
        lines[0] = '1' + lines[0][1:] if M > 1 else '1'

    # 模拟原逻辑
    first_line = lines[0]
    day = [i for i, val in enumerate(first_line) if val == '1']
    best = min_sub_array(day, K)

    for idx in range(1, N):
        line = lines[idx]
        day = [i for i, val in enumerate(line) if val == '1']
        new_day_best = min_sub_array(day, K)

        new_best = [float('inf')] * (K + 1)
        for i in range(K + 1):
            for j in range(i + 1):
                new_best[i] = min(new_best[i], new_day_best[j] + best[i - j])
        best = new_best

    # 模拟原代码输出
    print(best[K])


if __name__ == "__main__":
    # 示例：调用 main，n 为规模参数
    main(10)