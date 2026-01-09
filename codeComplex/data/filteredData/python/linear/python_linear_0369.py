def main(n):
    # 映射规则：
    # total_games = n
    # total_notes = max(1, n // 2)
    total_games = n
    total_notes = max(1, n // 2)

    # 确定性生成 games 和 notes
    # games: 严格递增序列，便于控制匹配过程
    games = [i + 1 for i in range(total_games)]

    # notes: 交替产生小值和较大值，控制匹配节奏
    # 保证非随机且可重复
    notes = [(i * 2 + 1) for i in range(total_notes)]

    note = 0
    for game in games:
        if notes[note] >= game:
            note += 1
        if note == total_notes:
            break
    # print(note)
    pass
if __name__ == "__main__":
    main(10)