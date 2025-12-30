import random

def main(n):
    # 1. 生成测试数据
    # 约定：
    #   - m 为总限制，随机在 [n, 3n] 区间
    #   - 每首歌是 [a, b]，其中 a, b 在 [1, 10] 区间随机
    m = random.randint(n, 3 * n)

    songs = []
    for _ in range(n):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        songs.append([a, b])

    # 2. 原算法逻辑
    def sumList(lista, inx):
        s = 0
        for i in range(len(lista)):
            s += lista[i][inx]
        return s

    songs_sorted = sorted(songs, key=lambda x: x[1] - x[0])

    suma = sumList(songs_sorted, 0)

    for i in range(n):
        if suma <= m:
            print(i)
            return
        suma -= songs_sorted[i][0] - songs_sorted[i][1]

    if suma <= m:
        print(n)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main，规模 n 自行设定
    main(10)