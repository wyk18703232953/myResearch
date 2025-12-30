import random

def main(n: int) -> str:
    # 生成测试数据：a 为 1..n 的随机排列
    a = list(range(1, n + 1))
    random.shuffle(a)

    indx = [0] * n
    winners = [''] * n

    # 记录每个值的位置
    for i, ai in enumerate(a):
        indx[ai - 1] = i

    # 从大到小处理每个 ai，确定对应位置的胜负
    for ai in range(n, 0, -1):
        i = indx[ai - 1]
        can_win = False

        # 向右跳
        for j in range(i + ai, n, ai):
            if a[j] > ai and winners[j] == 'B':
                can_win = True
                break

        # 如有需要，再向左跳
        if not can_win:
            for j in range(i - ai, -1, -ai):
                if a[j] > ai and winners[j] == 'B':
                    can_win = True
                    break

        winners[i] = 'A' if can_win else 'B'

    result = ''.join(winners)
    print(result)
    return result


if __name__ == "__main__":
    # 示例：运行时可修改 n 测试
    main(10)