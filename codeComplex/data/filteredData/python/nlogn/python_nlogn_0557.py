from collections import deque

def bfs():
    global visited, dp, l, b, s, ans
    while len(b) > 0 and len(s) > 0:
        aux = 0
        for i in l[s[0]]:
            if not visited[i]:
                visited[i] = True
                dp[i] = 1
                aux += 1
        for _ in range(aux):
            if not b:
                ans = "No"
                return
            x = b.popleft()
            if dp[x] == 1:
                s.append(x)
                dp[x] = -1
            else:
                ans = "No"
                return
        s.popleft()

def main(n):
    global visited, dp, l, b, s, ans
    if n < 1:
        return
    visited = [False for _ in range(n + 2)]
    dp = [-1 for _ in range(n + 2)]
    l = [[] for _ in range(n + 2)]

    # 构造一棵确定性的树：1-2-3-...-n（链式）
    for i in range(1, n):
        a = i
        c = i + 1
        l[a].append(c)
        l[c].append(a)

    # 构造确定性的 BFS 序列：1,2,3,...,n
    seq = [i for i in range(1, n + 1)]
    b = deque(seq)
    b.popleft()  # 与原程序一致：去掉第一个元素

    s = deque([1])
    ans = "Yes"
    visited[1] = True
    bfs()
    print(ans)

if __name__ == "__main__":
    main(10)