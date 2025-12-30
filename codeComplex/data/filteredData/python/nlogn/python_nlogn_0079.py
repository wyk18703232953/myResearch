import random

def main(n):
    # 随机生成 k，保证 1 <= k <= n
    k = random.randint(1, n)

    # 生成 n 个队伍：(score, penalty)
    # score 范围 [0, 1000]，penalty 范围 [0, 1000]
    teams = []
    for _ in range(n):
        score = random.randint(0, 1000)
        penalty = random.randint(0, 1000)
        teams.append((score, penalty))

    freqs = {}
    teams.sort(key=lambda x: (-x[0], x[1]))
    for team in teams:
        freqs[team] = freqs.get(team, 0) + 1
    print(freqs[teams[k - 1]])

if __name__ == "__main__":
    # 示例：规模为 10
    main(10)