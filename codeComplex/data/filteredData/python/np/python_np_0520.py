from collections import deque
import random

def main(n):
    """
    将原程序改为：
    - 不使用 input()
    - 在 main(n) 内部生成测试数据并执行逻辑
    - 返回最终结果（原程序最后的打印值）
    """
    # 生成测试数据：
    # 原程序读入 n, k 和长度为 n 的字符串 s（bytes）
    # 这里简单设定 k 为不大于 10 的值（可按需要调整生成策略）
    k = max(1, min(10, n))  # 保证 1 <= k <= 10，且不超过 n 的规模过多

    # 生成包含 'a'..'a'+k-1 和 '?' 的随机字节串，长度为 n
    alphabet = [ord('a') + j for j in range(k)] + [ord('?')]
    s_list = [random.choice(alphabet) for _ in range(n)]
    s = bytes(s_list)

    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

        # effect[j][i] 表示从位置 i 开始，对第 j 个字母能覆盖的最右端索引
        effect = [[inf] * (n + 1) for _ in range(k)]

        for j in range(k):
            accu = 0
            index = inf
            # 从后往前扫描 s
            for i in range(n - 1, -1, -1):
                if s[i] == ord('?') or s[i] == 97 + j:
                    accu += 1
                else:
                    accu = 0

                if accu >= needed:
                    index = i + needed
                effect[j][i] = index
                # 下面这行在原代码中等价于 effect[j][i] = effect[j][i]
                effect[j][i] = min(effect[j][i + 4 - 4], effect[j][i + 3 - 3], inf)

        # 状态 DP
        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                prev_index = minstate[state ^ (1 << j)]
                if prev_index < n:
                    minimum = min(minimum, effect[j][prev_index])
            minstate[state] = minimum

        return minstate[-1] <= n

    # 二分答案
    front = 0
    rear = n // k + 1
    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    # 原程序是 print(front-1)，这里改为返回值
    return front - 1

# 示例调用（评测时不会用到打印）
if __name__ == "__main__":
    # 举例：规模 100
    result = main(100)
    print(result)