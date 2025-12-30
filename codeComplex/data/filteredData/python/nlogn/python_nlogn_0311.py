import random

def main(n: int):
    # 生成一个随机排列 p，元素为 0..n-1
    p = list(range(n))
    random.shuffle(p)

    vis = [False] * n
    odd = 0
    for x in range(n):
        if vis[x]:
            continue
        odd ^= 1
        while not vis[x]:
            odd ^= 1
            vis[x] = True
            x = p[x]

    print('Petr' if (n + odd) % 2 == 0 else 'Um_nik')


if __name__ == "__main__":
    # 示例：n = 10
    main(10)