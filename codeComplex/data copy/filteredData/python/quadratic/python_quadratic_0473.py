def main(n):
    if n <= 0:
        return

    # 构造一个确定性的 candies 数组，规模为 n
    candies = [(i * 3 + 1) % n + 1 for i in range(n)]

    # 根据原逻辑由 candies 反推 l 和 r，以保持整体算法逻辑不变
    l = []
    for i in range(n):
        guys = 0
        for j in range(i):
            if candies[j] > candies[i]:
                guys += 1
        l.append(guys)

    r = []
    for i in range(n):
        guys = 0
        for j in range(i, n):
            if candies[j] > candies[i]:
                guys += 1
        r.append(guys)

    # 以下为原程序核心逻辑，使用上述确定性生成的 l, r
    candies_rec = []
    for i in range(n):
        candies_rec.append(n - l[i] - r[i])

    left = []
    for i in range(n):
        guys = 0
        for j in range(i):
            if candies_rec[j] > candies_rec[i]:
                guys += 1
        left.append(guys)

    right = []
    for i in range(n):
        guys = 0
        for j in range(i, n):
            if candies_rec[j] > candies_rec[i]:
                guys += 1
        right.append(guys)

    if left == l and right == r:
        # print("YES")
        pass
        candiesstr = ""
        for i in range(n):
            candiesstr += str(candies_rec[i]) + " "
        # print(candiesstr[: len(candiesstr) - 1])
        pass

    else:
        # print("NO")
        pass
if __name__ == "__main__":
    main(5)