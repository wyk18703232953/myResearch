from itertools import combinations
import random

MOD = 1000000007


def findsum(comb):
    s = 0
    for song in comb:
        s += song[0]
    return s


def finda(a, b, c):
    if a == 0:
        return 0
    if a == 1 and b == 0 and c == 0:
        return 1
    else:
        return a * findb(a - 1, b, c) + a * findc(a - 1, b, c)


def findb(a, b, c):
    if b == 0:
        return 0
    if b == 1 and a == 0 and c == 0:
        return 1
    else:
        return b * finda(a, b - 1, c) + b * findc(a, b - 1, c)


def findc(a, b, c):
    if c == 0:
        return 0
    if c == 1 and a == 0 and b == 0:
        return 1
    else:
        return c * finda(a, b, c - 1) + c * findb(a, b, c - 1)


def main(n):
    # 生成测试数据
    # 为保证可控，这里设置每首歌时长在 [1, 10]，风格为 1/2/3
    random.seed(0)
    songs = []
    for _ in range(n):
        t = random.randint(1, 10)
        g = random.randint(1, 3)
        songs.append([t, g])

    # 将目标总时间 T 设为所有歌曲时长之和的一半（向下取整），
    # 这样通常会有部分组合能满足。
    total_time = sum(song[0] for song in songs)
    T = total_time // 2 if total_time > 0 else 0

    total_combinations = 0

    for i in range(1, n + 1):
        allcomb = combinations(songs, i)
        for comb in allcomb:
            s = findsum(comb)
            if s == T:
                a = b = c = 0
                for song in comb:
                    if song[1] == 1:
                        a += 1
                    elif song[1] == 2:
                        b += 1
                    else:
                        c += 1
                total_combinations += finda(a, b, c) + findb(a, b, c) + findc(a, b, c)

    total_combinations %= MOD
    print(total_combinations)


if __name__ == "__main__":
    # 示例调用：规模为 5
    main(5)