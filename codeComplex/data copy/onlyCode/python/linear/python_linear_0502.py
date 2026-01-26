
def get_fingering(notes):
    fingering = []
    diff = 0
    next_diff = None
    finger = 0
    for i in range(len(notes) - 1):
        next_diff = notes[i+1] - notes[i]
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


_ = input()
notes = [int(x) for x in input().split()]
notes.append(notes[-1])

fingering = get_fingering(notes)

if fingering:
    print(*fingering)
else:
    print(-1)

