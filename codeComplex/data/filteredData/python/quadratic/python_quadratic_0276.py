def main(n):
    # 设定 m 与 n 同规模，便于时间复杂度实验
    m = n

    # 确定性生成 l1, l2
    # l1: 0, 1, 2, ..., n-1
    l1 = [i for i in range(n)]
    # l2: i*2 % n，带重复和打散
    l2 = [(i * 2) % n for i in range(m)]

    l3 = []
    for i in range(n):
        for j in range(m):
            if l1[i] == l2[j]:
                # 保留原逻辑核心意图：避免重复加入
                if l1[i] not in l3:
                    l3.append(l1[i])
    # 输出与原程序一致
    if l3:
        print(*l3)
    else:
        print()

if __name__ == "__main__":
    main(10)