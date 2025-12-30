import random

MOD = int(1e9 + 7)

def main(n: int):
    """
    参数
    ----
    n : int
        歌曲数量（规模）。本题原始写法用了位掩码 DP，因此 n 不宜太大（例如 <= 18）。
    """
    # 生成测试数据：
    # 每首歌: [时间, 类型], 类型为 0,1,2（原代码中读入后做了 -1）
    # 时间设为 [1, 5] 之间的随机整数
    songs = []
    for _ in range(n):
        duration = random.randint(1, 5)
        genre = random.randint(0, 2)
        songs.append([duration, genre])

    # 设目标总时间 t 为所有时长和的一半向下取整（保证规模相关）
    total_duration = sum(s[0] for s in songs)
    t = total_duration // 2

    # 以下是原始 main() 的逻辑（去掉输入，直接使用生成的 songs 和 t）
    result = 0

    # dp[mask][genre]: 以 mask 表示选择的歌曲集合，且最后一首歌类型为 genre 的排列数
    dp = [[0, 0, 0] for _ in range(1 << n)]

    for ind, it in enumerate(songs):
        dp[1 << ind][it[1]] = 1

    for mask in range(1, 1 << n):
        for genre in range(3):
            # 尝试接一首不同类型的歌
            for nsng, sng in enumerate(songs):
                if sng[1] != genre and ((mask >> nsng) & 1) == 0:
                    dp[mask | (1 << nsng)][sng[1]] += dp[mask][genre]
                    dp[mask | (1 << nsng)][sng[1]] %= MOD

            # 计算当前 mask 的总时长
            sm = 0
            # 注意：原代码中用 reversed(bin(mask)[2:]) + enumerate，
            # 其索引与歌曲顺序不严谨，这里保留逻辑一致性（从右到左数位置）
            for ind, bit in enumerate(reversed(bin(mask)[2:])):
                if bit == '1':
                    sm += songs[ind][0]

            if sm == t:
                result += dp[mask][genre]
                result %= MOD

    print(result)


if __name__ == "__main__":
    # 示例：运行规模 n = 10
    main(10)