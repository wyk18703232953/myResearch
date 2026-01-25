import re

def main(n):
    # n 表示游戏和音符的总规模，拆成两半
    total_games = n // 2
    total_notes = n - total_games
    if total_games == 0:
        total_games = 1
    if total_notes == 0:
        total_notes = 1

    # 确定性生成 games 和 notes
    games = [(i * 2 + 1) for i in range(total_games)]
    notes = [(i * 3) // 2 for i in range(total_notes)]

    note = 0
    for game in games:
        if notes[note] >= game:
            note += 1
        if note == total_notes:
            break
    print(note)


if __name__ == "__main__":
    main(10)