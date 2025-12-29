import random

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
    # 生成规模为 n 的测试数据：音高为 1~100 的随机序列
    notes = [random.randint(1, 100) for _ in range(n)]
    # 按原程序逻辑，追加最后一个音符
    notes.append(notes[-1])

    fingering = get_fingering(notes)

    if fingering:
        print(*fingering)
    else:
        print(-1)


if __name__ == "__main__":
    # 示例调用：可根据需要修改 n
    main(10)