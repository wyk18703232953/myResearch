def main(n):
    from collections import deque

    # 为时间复杂度实验构造确定性输入：
    # 映射：n -> 原程序中的 n，且 k 也随 n 确定性变化
    # 约束：k <= 20（因为使用了 1<<k 的状态数组）
    if n <= 0:
        return 0

    # 选择一个与 n 相关但有上界的 k
    k = min(5 + n % 10, 20)
    # 确保 n 至少能被 k 使用到一定规模
    n_effective = max(n, k)

    # 构造长度为 n_effective 的字节串 s，元素为 'a'..('a'+k-1) 和 '?'
    # 完全确定性构造：根据下标 i 和 k 做简单算术
    s_list = []
    for i in range(n_effective):
        if i % (k + 1) == 0:
            s_list.append(ord('?'))
        else:
            s_list.append(ord('a') + (i % k))
    s = bytes(s_list)

    inf = 2147483647

    def judge(needed):
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        effect = [[inf] * (n_effective + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(n_effective - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0
                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                effect[j][i] = min(effect[j][i], effect[j][i], inf * inf)

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n_effective:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        return minstate[-1] <= n_effective

    front = 0
    rear = n_effective // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    result = front - 1
    print(result)
    return result


if __name__ == "__main__":
    main(1000)