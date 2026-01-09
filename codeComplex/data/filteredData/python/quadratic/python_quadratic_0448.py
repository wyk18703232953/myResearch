def main(n):
    # n is the length of the melody
    if n <= 0:
        return

    # Deterministic melody generation based on n
    # Pattern: melody[i] = (i % 7) + (i // 3) to create ups/downs/repeats
    melody = [(i % 7) + (i // 3) for i in range(n)]

    ref = [[-1] * 5 for _ in range(n)]
    can_finish = [[False] * 5 for _ in range(n)]
    can_finish[0] = [True] * 5

    for idx, key in enumerate(melody[:-1]):
        if not any(can_finish[idx]):
            break
        for finger in range(5):
            if melody[idx] < melody[idx + 1] and can_finish[idx][finger]:
                for i in range(finger + 1, 5):
                    can_finish[idx + 1][i] = True
                    ref[idx + 1][i] = finger
                break
            elif melody[idx] > melody[idx + 1] and can_finish[idx][finger] and finger > 0:
                for i in range(finger):
                    can_finish[idx + 1][i] = True
                    ref[idx + 1][i] = finger
            elif melody[idx] == melody[idx + 1] and can_finish[idx][finger]:
                tmp_val, tmp_ref = can_finish[idx + 1][finger], ref[idx + 1][finger]
                can_finish[idx + 1] = [True] * 5
                ref[idx + 1] = [finger] * 5
                can_finish[idx + 1][finger], ref[idx + 1][finger] = tmp_val, tmp_ref

    finger = next((i for i in range(5) if can_finish[n - 1][i]), None)
    if finger is None:
        # print(-1)
        pass

    else:
        seq = [finger]
        for i in range(n - 1, 0, -1):
            finger = ref[i][finger]
            seq.append(finger)
        # print(' '.join(str(x + 1) for x in seq[::-1]))
        pass
if __name__ == "__main__":
    main(10)