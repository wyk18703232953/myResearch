import random

def main(n):
    # 生成测试数据：n 和 k（1 ≤ k ≤ 10，且 k ≤ n 时更有趣）
    if n <= 0:
        return
    k = random.randint(1, min(10, max(1, n)))
    # 生成 n 个整数，每个在 [0, 2*n] 范围内
    p = [random.randint(0, 2 * n) for _ in range(n)]

    processed = set()
    color = {}
    length = {}
    ans = []

    for i in range(n):
        elt = p[i]
        if elt in processed:
            ans.append(color[elt])
        else:
            processed.add(elt)
            new = 1
            run = True
            for j in range(1, k):
                if elt - j < 0:
                    break
                elif (elt - j) not in processed:
                    processed.add(elt - j)
                    new += 1
                elif length[elt - j] + new <= k:
                    for i2 in range(length[elt - j] + new):
                        color[elt - i2] = color[elt - j]
                    length[elt] = length[elt - j] + new
                    run = False
                    break
                else:
                    break
            if run:
                for j in range(new):
                    color[elt - j] = elt - new + 1
                length[elt] = new

    s = str(color[p[0]])
    for elt in p[1:]:
        s += ' ' + str(color[elt])
    print(s)