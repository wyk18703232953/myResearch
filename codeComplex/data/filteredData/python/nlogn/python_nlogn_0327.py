import random

def main(n: int):
    # 生成一个 0..n-1 的随机排列 p
    p = list(range(n))
    random.shuffle(p)

    visited = [False] * n
    loops = []

    for x in range(n):
        if not visited[x]:
            visited[x] = True
            start = x
            l = [x]
            cur = p[x]
            while cur != start:
                visited[cur] = True
                l.append(cur)
                cur = p[cur]
            loops.append(len(l) - 1)

    tot = sum(loops)

    if n % 2 == 1:
        if tot % 2 == 1:
            print('Petr')
        else:
            print('Um_nik')
    else:
        if tot % 2 == 0:
            print('Petr')
        else:
            print('Um_nik')


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)