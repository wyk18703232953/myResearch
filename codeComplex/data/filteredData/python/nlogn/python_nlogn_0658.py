import random

def main(n):
    # 1. 生成测试数据 A（1-based，下标0不用）
    # 这里给每个点一个随机度数，保证至少有一个点度数≥2，避免一开始就输出 NO
    if n <= 0:
        return
    A = [0] * (n + 1)
    for i in range(1, n + 1):
        # 随机度数，范围可自行调整
        A[i] = random.randint(1, max(2, n // 2))
    # 确保至少有一个点的度数 ≥ 2
    if max(A[1:]) <= 1:
        A[1] = 2

    # 2. 原逻辑开始
    vec = []
    for i in range(1, n + 1):
        vec.append([A[i], i])
    vec.sort()
    vec.reverse()

    if vec[0][0] == 1:
        print("NO")
        return

    dia = 0
    path = [vec[0][1]]
    ans = []
    bol, col, idx = 1, 1, 0

    for v in vec[1:]:
        if v[0] != 1:
            ans.append([path[-1], v[1]])
            dia += 1
            A[path[-1]] -= 1
            path.append(v[1])
            A[path[-1]] -= 1
        else:
            if col == 1:
                dia += 1
                col = 0
                A[path[0]] -= 1
                ans.append([path[0], v[1]])
            elif bol == 1:
                dia += 1
                bol = 0
                A[path[-1]] -= 1
                ans.append([path[-1], v[1]])
            else:
                while idx < len(path) and A[path[idx]] == 0:
                    idx += 1
                if idx == len(path):
                    print("NO")
                    return
                A[path[idx]] -= 1
                ans.append([path[idx], v[1]])

    print("YES", dia)
    print(len(ans))
    for u, w in ans:
        print(u, w)


if __name__ == "__main__":
    # 示例：运行规模为 n 的一组测试
    main(10)