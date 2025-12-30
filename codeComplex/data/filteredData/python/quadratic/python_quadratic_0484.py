import random


def main(n: int):
    # 生成一组可能有解的测试数据
    # 思路：先随机生成一个排列 res，再根据 res 反推 left 和 right
    # 对于每个位置 i：
    #   left[i]  = 左侧编号比 res[i] 大的个数
    #   right[i] = 右侧编号比 res[i] 大的个数

    # 生成 1..n 的随机排列作为目标结果
    res_original = list(range(1, n + 1))
    random.shuffle(res_original)

    left = [0] * n
    right = [0] * n

    # 预计算 left 和 right
    for i in range(n):
        cur = res_original[i]
        # 左侧
        cnt_left = 0
        for j in range(i):
            if res_original[j] > cur:
                cnt_left += 1
        left[i] = cnt_left

        # 右侧
        cnt_right = 0
        for j in range(i + 1, n):
            if res_original[j] > cur:
                cnt_right += 1
        right[i] = cnt_right

    # 以下是原逻辑（去掉 input，并使用生成的 left/right）
    res = [0] * n
    val = n

    if all(not left[i] and not right[i] for i in range(n)):
        print("YES")
        print(' '.join(['1'] * n))
        return

    while not all(not left[i] and not right[i] for i in range(n)):
        zeroSet = set()
        for i in range(n):
            if not left[i] and not right[i] and res[i] == 0:
                zeroSet.add(i)
                res[i] = val
        for v in zeroSet:
            for i in range(v + 1, n):
                if i not in zeroSet and res[i] == 0:
                    left[i] -= 1
            for i in range(v):
                if i not in zeroSet and res[i] == 0:
                    right[i] -= 1
        val -= 1
        if not zeroSet:
            print("NO")
            return

    for i in range(n):
        if not res[i]:
            res[i] = str(val)
        else:
            res[i] = str(res[i])
    if any(i == '0' for i in res):
        print("NO")
        return
    print("YES")
    print(' '.join(res))


# 示例：需要时手动调用 main(n)
# main(5)