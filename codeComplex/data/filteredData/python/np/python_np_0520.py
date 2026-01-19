import io
from collections import deque

def build_input_from_n(n):
    # 将 n 映射为字符串长度和字母种类数量
    # 至少保证 k>=1 且 k 不超过 5，方便位运算
    if n <= 0:
        n = 1
    k = max(1, min(5, n % 5 + 1))
    length = max(k, n)

    # 构造一个包含 'a'.. 对应字母和 '?' 的周期性字符串
    chars = [ord('a') + (i % k) if (i // k) % 2 == 0 else ord('?') for i in range(length)]
    s = bytes(chars)
    return length, k, s

def solver(n, k, s):
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
                effect[j][i] = min(effect[j][i], effect[j][i + 0], inf)

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
    length, k, s = build_input_from_n(n)
    result = solver(length, k, s)
    print(result)

if __name__ == "__main__":
    main(10)