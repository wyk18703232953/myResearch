import sys

def main(n):
    if n <= 0:
        # print(0)
        pass
        return

    # 构造确定性的 c 和 a
    # c[i] = i + 1
    c = [i + 1 for i in range(n)]
    # a 构成一个长度为 n 的环：0 -> 1 -> 2 -> ... -> n-1 -> 0
    a = [(i + 1) % n for i in range(n)]

    visited = [-1] * n
    res = 0

    for i in range(n):
        trace = []
        t = i
        mn = 1e9
        while visited[t] == -1:
            visited[t] = i
            trace.append(t)
            t = a[t]

        if visited[t] != i:
            continue

        while len(trace) > 0:
            v = trace.pop()
            mn = min(mn, c[v])
            if t == v:
                break

        res += mn

    # print(res)
    pass
if __name__ == "__main__":
    # 示例调用：可按需修改 n 以做规模实验
    main(10)