def get_fingering(notes):
    fingering = []
    diff = 0
    next_diff = None
    finger = 0
    for i in range(len(notes) - 1):
        next_diff = notes[i + 1] - notes[i]
        if diff == 0:
            if next_diff > 0:
                finger = 1 + (finger == 1)
            elif next_diff < 0:
                finger = 5 - (finger == 5)

            else:
                finger = 3 + (finger == 3)
        elif diff > 0:
            if finger == 5:
                return None
            if next_diff < 0:
                finger = 5

            else:
                finger += 1

        else:
            if finger == 1:
                return None
            if next_diff > 0:
                finger = 1

            else:
                finger -= 1
        fingering.append(finger)
        diff = next_diff
    return fingering


def main(n):
    # 解释输入规模映射：
    # n 表示音符序列的长度（原程序中为 len(notes)），
    # 其中我们生成一个确定性的整数序列作为音符。
    # 生成方式完全确定：notes[i] = (i * 3) % 7 + i // 2
    if n <= 0:
        return

    notes = [(i * 3) % 7 + i // 2 for i in range(n)]
    notes.append(notes[-1])

    fingering = get_fingering(notes)

    if fingering:
        # print(*fingering)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)