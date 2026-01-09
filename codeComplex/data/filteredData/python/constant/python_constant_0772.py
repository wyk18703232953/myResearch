def main(n):
    t = n
    for _ in range(t):
        size = max(2, n)  # 保证至少两个元素
        g = [i % (n + 3) + 1 for i in range(size)]
        m1 = max(g)
        g_remove = g.copy()
        g_remove.remove(m1)
        m2 = max(g_remove)
        dl = len(g_remove) - 1
        # print(min(dl, m2 - 1))
        pass
if __name__ == "__main__":
    main(10)