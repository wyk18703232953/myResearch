def main(n):
    # 生成确定性输入数据：
    # 原程序含义：有 n 行，每行若干整数，计算每行和，然后看第 1 行的和在所有行中的排序名次（按从大到小排序）。
    # 这里用固定结构生成数据：第 i 行包含 (i+1) 个整数，为 [i, i+1, ..., i+(i+1)-1]
    S = []
    for i in range(n):
        A = [i + j for j in range(i + 1)]
        S.append(sum(A))

    if not S:
        return  # 规模为 0 时无输出，保持程序确定性

    if S[0] == max(S):
        # print("1")
        pass
        return

    thomas = S[0]
    rank = 1
    S.sort(reverse=True)
    for v in S:
        if v == thomas:
            # print(rank)
            pass
            return

        else:
            rank += 1


if __name__ == "__main__":
    main(10)