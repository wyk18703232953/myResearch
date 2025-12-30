import sys
import heapq
import random

def main(n: int):
    # 1. 生成测试数据
    # 生成权值数组 w，取值范围可自行调节
    w = [random.randint(1, 10**6) for _ in range(n)]

    # 生成长度为 2n 的操作串 s，包含恰好 n 个 '0' 和 n 个 '1'
    # 保证逻辑可运行：前缀中 '0' 的个数始终不少于 '1' 的个数
    zeros_left = n
    ones_left = n
    balance = 0  # = 已放入的个数 - 已取出的个数
    s_chars = []
    for _ in range(2 * n):
        # 如果当前没有可取的元素，必须是 '0'
        if balance == 0:
            s_chars.append('0')
            zeros_left -= 1
            balance += 1
        # 如果剩下的都是某一种，就只能用那种
        elif zeros_left == 0:
            s_chars.append('1')
            ones_left -= 1
            balance -= 1
        elif ones_left == 0:
            s_chars.append('0')
            zeros_left -= 1
            balance += 1
        else:
            # 随机选择，但要保证不会破坏后续可行性
            # 给 '0' 和 '1' 一定概率
            if random.random() < 0.5:
                s_chars.append('0')
                zeros_left -= 1
                balance += 1
            else:
                s_chars.append('1')
                ones_left -= 1
                balance -= 1
    s = ''.join(s_chars)

    # 2. 原逻辑
    idx = []
    for i in range(n):
        idx.append((w[i], i + 1))

    idx.sort()
    heapq.heapify(idx)
    ones = []
    heapq.heapify(ones)
    res = []

    for i in range(2 * n):
        if s[i] == '0':
            l = idx[0]
            heapq.heappop(idx)
            res.append(l[1])
            heapq.heappush(ones, [-l[0], l[1]])
        else:
            l = ones[0]
            heapq.heappop(ones)
            res.append(l[1])

    # 3. 输出结果（可以按需要调整：这里输出 w, s, 以及结果）
    out = []
    out.append("w: " + " ".join(map(str, w)))
    out.append("s: " + s)
    out.append("res: " + " ".join(map(str, res)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    # 示例：可以修改这里的 n 进行测试
    main(5)