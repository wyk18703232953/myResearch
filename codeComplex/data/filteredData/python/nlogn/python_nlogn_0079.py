def main(n):
    # 映射：n -> (number_of_teams, k)
    # 为了可扩展性，将队伍数量设为 n，k 设为 (n // 2) + 1，且 k 不超过 n
    num_teams = max(1, n)
    k = min(num_teams, num_teams // 2 + 1)

    # 确定性生成 teams 列表
    # 原结构：每行两个整数 (score, penalty)
    # 使用简单算术关系生成：
    # score = n - i // 2   (保证部分重复分数)
    # penalty = i % 5      (保证部分重复罚分)
    teams = [(num_teams - i // 2, i % 5) for i in range(num_teams)]

    freqs = {}
    teams.sort(key=lambda x: (-x[0], x[1]))
    for team in teams:
        freqs[team] = freqs.get(team, 0) + 1

    # 模拟原程序行为：输出第 k-1 个队伍的出现次数
    print(freqs[teams[k - 1]])


if __name__ == "__main__":
    main(10)