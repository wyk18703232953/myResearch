import random

def combine(n, k, w=1, out=None, result=None):
    if out is None:
        out = []
    if result is None:
        result = []

    if k == 0:
        result.append(out)
        return result

    for i in range(w, n + 1):
        new_out = out[:]  # copy current combination
        new_out.append(i)
        combine(n, k - 1, i + 1, new_out, result)

    return result


def main(n):
    # 生成测试数据：
    # n: 元素数量
    # l, r: 和的区间
    # x: 最大值与最小值的差值下限
    # c: n 个正整数
    if n < 2:
        print(0)
        return

    # 生成 c 中的元素，范围可自行调整
    c = [random.randint(1, 100) for _ in range(n)]

    # 让 l、r 根据 c 的总体范围生成，保证有一定概率有解
    total_min = min(c) * 2
    total_max = sum(c)
    if total_min > total_max:
        total_min, total_max = total_max, total_min
    l = random.randint(total_min, total_max)
    r = random.randint(l, total_max)

    # x 在当前 c 的跨度内生成
    x = random.randint(0, max(c) - min(c) if max(c) != min(c) else 0)

    if n < 2:
        print(0)
        return

    # 生成所有大小为 n 的组合（原代码的最终结果只保留大小为 n 的组合）
    result = combine(n, n)

    # 将组合里的索引转换成分值
    for i in range(len(result)):
        comb = result[i]
        for j in range(len(comb)):
            comb[j] = c[comb[j] - 1]

    cnt = 0
    for i in range(len(result)):
        sm = sum(result[i])
        if l <= sm <= r and (max(result[i]) - min(result[i]) >= x):
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    # 示例：使用 n=4 运行
    main(4)