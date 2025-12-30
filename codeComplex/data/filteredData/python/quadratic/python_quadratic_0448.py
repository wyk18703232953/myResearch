import random

def main(n):
    # 生成测试数据：长度为 n 的随机音高序列，取值范围 1~10
    melody = [random.randint(1, 10) for _ in range(n)]

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
        print(-1)
    else:
        seq = [finger]
        for i in range(n - 1, 0, -1):
            finger = ref[i][finger]
            seq.append(finger)
        print(' '.join(str(x + 1) for x in seq[::-1]))


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    main(10)