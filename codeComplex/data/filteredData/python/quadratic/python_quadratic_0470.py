import random

def main(n: int):
    # 生成满足原算法要求的合法测试数据
    # 构造一个随机的糖果分配，然后反推 L、R
    candies = list(range(1, n + 1))
    random.shuffle(candies)

    # 初始化 L, R
    L = [0] * n
    R = [0] * n

    # 我们从原算法的反向过程生成 L, R
    # 思路：从 nn = 1 到 n，依次选择一个未放糖果的位置作为“本层的 zero_index”
    # 然后根据原算法在那一层的 dec_left / dec_right 计算其它位置的 (l, r)
    assigned = [False] * n
    LR = [(0, 0)] * n  # 占位

    # 为了让数据尽量多样，我们记录每一轮哪些位置“被视为零”
    # 然后反向模拟 dec_left / dec_right 对其它位置的累计影响
    # impacts[i] = (sum_left_shift, sum_right_shift) 到该轮之前的累计
    impacts = [(0, 0)] * n

    for nn in range(1, n + 1):
        # 本轮将要设置为 0 的位置（在原算法中，这一轮它们的 L,R 为 (0,0)）
        idx_zero = random.choice([i for i, used in enumerate(assigned) if not used])
        assigned[idx_zero] = True
        candy_value = candies[idx_zero]

        # 在原算法中，从 nn=n..1 递减；这里我们从 1..n 递增，顺序等价
        # 在这一轮中，从头扫到尾：
        #   遇到 zero_index -> dec_left += 1, dec_right -= 1
        #   其他非零位置的 (l,r) 同时减少 (dec_left, dec_right)
        # 我们现在在构造原始 (l,r)，所以要把“减少之前”的值算出来：
        #   原始 (l,r) = 当前可见 (l,r) + 本轮对该位置的 (dec_left, dec_right) 影响
        # 但我们可以直接记录本轮对每个位置的 (delta_left, delta_right)，
        # 然后将所有轮的影响累加出来，作为最终 L,R。
        delta_left = [0] * n
        delta_right = [0] * n

        dec_left = 0
        dec_right = 1  # 一轮只有一个 zero_index

        for idx in range(n):
            if idx == idx_zero:
                # 这个位置在这一轮是 (0,0)，之后 dec_left/dec_right 更新
                delta_left[idx] += dec_left
                delta_right[idx] += dec_right
                dec_left += 1
                dec_right -= 1
            else:
                # 非 zero_index 位置仅受当前 dec_left/dec_right 影响
                delta_left[idx] += dec_left
                delta_right[idx] += dec_right

        # 累加到总 impacts
        for i in range(n):
            l_sum, r_sum = impacts[i]
            impacts[i] = (l_sum + delta_left[i], r_sum + delta_right[i])

    # 现在 impacts 中就是每个位置在所有轮上的 (dec_left, dec_right) 总影响。
    # 对应到原始数据：原始 L[i] = impacts[i][0]，R[i] = impacts[i][1]
    for i in range(n):
        L[i], R[i] = impacts[i]

    # 至此，我们生成了一组 L, R，它们在原算法中应当是合法的。
    # 下面直接运行原算法逻辑，但不使用 input()，而是用我们刚刚生成的 L, R。

    LR = list(zip(L, R))
    index_to_candies = {}
    candy = n  # 未实际使用，但保留以保持结构

    for nn in range(n, 0, -1):
        if len(index_to_candies) == n:
            break

        zero_index = []
        for idx, (l, r) in enumerate(LR):
            if (l, r) == (0, 0) and idx not in index_to_candies:
                index_to_candies[idx] = nn
                zero_index.append(idx)

        if len(zero_index) == 0:
            print("NO")
            return

        dec_left = 0
        dec_right = len(zero_index)
        zero_index_idx = 0

        for idx, (l, r) in enumerate(LR):
            if zero_index_idx < len(zero_index) and zero_index[zero_index_idx] == idx:
                zero_index_idx += 1
                dec_left += 1
                dec_right -= 1

            if (l, r) != (0, 0):
                LR[idx] = (l - dec_left, r - dec_right)
                if LR[idx][0] < 0 or LR[idx][1] < 0:
                    print("NO")
                    return

    print("YES")
    j = []
    for i in range(n):
        j.append(str(index_to_candies[i]))
    print(" ".join(j))


if __name__ == "__main__":
    # 随机选择一个规模进行测试，或手动设置，如 main(5)
    main(5)