from operator import itemgetter

def main(n):
    # 生成确定性输入数据：长度为 n 的整数数组 ai
    # 使用简单算术构造，保证可重复、无随机性
    ai = [(i * 2 + 3) % (n + 5) + 1 for i in range(n)]

    ai2 = [[ai[i], i] for i in range(n)]
    answer = [0] * n
    ai2.sort(key=itemgetter(0))
    if n > 0:
        answer[ai2[0][1]] = 1
        answer[ai2[-1][1]] = 0
    for i in range(n - 2, 0, -1):
        if ai2[i][0] == 0:
            continue
        num = ai2[i][1] % ai2[i][0]
        for j in range(num, n, ai2[i][0]):
            if ai[j] > ai2[i][0] and answer[j] == 0:
                answer[ai2[i][1]] = 1
                break
    for i in range(n):
        if answer[i] == 1:
            # print("A", end="")
            pass

        else:
            # print("B", end="")
            pass
    # print()
    pass
if __name__ == "__main__":
    # 示例调用，可根据需要修改 n
    main(10)