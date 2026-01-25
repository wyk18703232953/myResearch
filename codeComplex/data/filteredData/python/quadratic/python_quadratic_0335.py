from collections import deque

def main(n):
    # 将 n 映射为原程序中的 (n_nodes, d, k)
    # 确定性构造：随 n 线性变化
    if n < 3:
        n_nodes = n
        d = 1
        k = 1
    else:
        n_nodes = n
        d = max(1, min(n_nodes - 1, n_nodes // 3))
        k = max(1, min(n_nodes, 3 + (n_nodes // 5)))

    n, d, k = n_nodes, d, k

    if n == 1:
        print('NO')
        return
    if n == 2:
        if d > 1:
            print('NO')
        else:
            print('YES')
            print(1, 2)
        return
    if (not 2 <= d <= n - 1) or k == 1:
        print('NO')
        return

    ans = []
    for i in range(d):
        ans.append((i + 1, i + 2))
    now = d + 2
    for i in range(d - 1):
        q = deque([(i + 2, min(i, d - i - 2))])
        first = True
        while q and len(ans) < n - 1:
            node, depth = q.popleft()
            end = now + k - 1
            if first:
                end -= 1
            for j in range(now, end):
                ans.append((node, j))
                if len(ans) == n - 1:
                    break
                if depth > 0:
                    q.append((j, depth - 1))
            now = end
            first = False

    if len(ans) == n - 1:
        print('YES')
        for i, j in ans:
            print(i, j)
    else:
        print('NO')


if __name__ == "__main__":
    # 示例调用，可根据需要调整 n 的大小做规模实验
    main(10)