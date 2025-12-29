import random

def main(n):
    # 生成测试数据：n个随机整数（可根据需要调整范围）
    # 为了更容易产生长度为2或3的等差序列，使用较小的范围
    arr = [random.randint(1, 50) for _ in range(n)]

    sett = set(arr)
    power = [2 ** i for i in range(32)]

    ans = []

    for d in power:
        for x in arr:
            tmp = [x]
            # 尝试扩展成长度最多为3的等差序列（公差为 d）
            for _ in range(2):
                nxt = tmp[-1] + d
                if nxt in sett:
                    tmp.append(nxt)
                else:
                    break

            if len(tmp) > len(ans):
                ans = tmp[:]

            if len(ans) == 3:
                break
        if len(ans) == 3:
            break

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    # 示例：调用 main(10) 进行测试
    main(10)