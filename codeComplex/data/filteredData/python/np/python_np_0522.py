from collections import deque
import random

def main(n):
    # n: 字符串长度规模；k 固定为 3~5 之间的一个合理值（也可按需调整）
    # 这里选择固定 k=4，若需其他生成规则可自行修改
    k = 4
    # 生成测试数据：随机由 'a'...'a'+k-1 和 '?' 组成的字节串
    alphabet = [ord('a') + i for i in range(k)]
    s_list = []
    for _ in range(n):
        # 0.2 概率生成 '?'，否则生成字母
        if random.random() < 0.2:
            s_list.append(ord('?'))
        else:
            s_list.append(random.choice(alphabet))
    s = bytes(s_list)

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        # effect[j][i]: 若从位置 i 开始用第 j 个字母覆盖一个长度为 needed 的段，
        #               段的右端点(开区间)位置；若不可行则为 inf
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            for i in range(n - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0
                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                if effect[j][i] > inf:
                    effect[j][i] = inf

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        return minstate[-1] <= n

    front = 0
    rear = n // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    # 按原程序逻辑返回结果
    return front - 1


if __name__ == "__main__":
    # 示例：规模为 20 时运行
    result = main(20)
    print(result)