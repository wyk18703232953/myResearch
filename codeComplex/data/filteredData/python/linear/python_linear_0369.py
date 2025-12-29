import random

def main(n):
    # 1. 生成测试数据规模
    # total_games 和 total_notes 都与 n 相关，避免为 0
    total_games = max(1, n)
    total_notes = max(1, n)

    # 2. 生成测试数据
    # 游戏时长和笔记值设为 1 到 2n 范围内的随机整数
    games = [random.randint(1, 2 * n) for _ in range(total_games)]
    notes = [random.randint(1, 2 * n) for _ in range(total_notes)]

    # 3. 原逻辑
    note = 0
    for game in games:
        if notes[note] >= game:
            note += 1
        if note == total_notes:
            break

    # 4. 输出结果
    print(note)


if __name__ == "__main__":
    # 示例：n=10，可按需修改
    main(10)