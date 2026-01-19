import sys
from collections import deque

def build_input(n):
    # 映射规则：
    # n -> 字符串长度
    # k 固定为 3（可根据需要调整，但保持确定性）
    if n < 1:
        n = 1
    k = 3
    # 构造长度为 n 的字符串，循环使用 'a','b','c','?'
    base = [ord('a'), ord('b'), ord('c'), ord('?')]
    s_bytes = bytes(base[i % 4] for i in range(n))
    return n, k, s_bytes

def solve(n, k, s):
    def judge(needed):
        inf = 2147483647
        minstate = [inf] * (1 << k)
        minstate[0] = 0

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
                effect[j][i] = effect[j][i + 4 - 4]

        for state in range(1, 1 << k):
            minimum = minstate[state]
            for j in range(k):
                if (1 << j) & state == 0:
                    continue
                index = minstate[state ^ (1 << j)]
                if index < n:
                    minimum = min(minimum, effect[j][index])
            minstate[state] = minimum

        if minstate[-1] <= n:
            return True
        return False

    front = 0
    rear = n // k + 1

    while front < rear:
        mid = (front + rear) // 2
        flag = judge(mid)
        if flag:
            front = mid + 1
        else:
            rear = mid

    return front - 1

def main(n):
    n_val, k, s_bytes = build_input(n)
    ans = solve(n_val, k, s_bytes)
    print(ans)

if __name__ == "__main__":
    # 示例调用：可以根据需要修改 n 的值做规模实验
    main(1000)