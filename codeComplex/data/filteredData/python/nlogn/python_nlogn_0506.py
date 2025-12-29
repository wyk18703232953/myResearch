import random

def sumList(lista, inx):
    s = 0
    for i in range(len(lista)):
        s += lista[i][inx]
    return s

def main(n):
    # 根据 n 生成测试数据
    # 生成 n 首歌，每首歌为 [a, b]，a >= b >= 0
    # 同时生成 m，略大于所有 a 之和，以保证有可能满足条件
    songs = []
    for _ in range(n):
        a = random.randint(1, 100)
        b = random.randint(0, a)  # 保证 b <= a
        songs.append([a, b])

    total_a = sumList(songs, 0)
    # 将 m 设置为 [0, total_a] 的某个随机值，测试不同情况
    m = random.randint(0, max(total_a, 1))

    # 原始逻辑开始
    songs = sorted(songs, key=lambda x: x[1] - x[0])

    suma = sumList(songs, 0)

    for i in range(n):
        if suma <= m:
            print(i)
            return
        suma -= songs[i][0] - songs[i][1]

    if suma <= m:
        print(n)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)