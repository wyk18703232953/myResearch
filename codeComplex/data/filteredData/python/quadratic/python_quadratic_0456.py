from operator import itemgetter
import random


def main(n: int):
    # 生成测试数据：长度为 n 的正整数数组 ai，元素范围可按需调整
    random.seed(0)
    ai = [random.randint(1, max(2, n)) for _ in range(n)]

    ai2 = [[ai[i], i] for i in range(n)]
    answer = [0] * n

    ai2.sort(key=itemgetter(0))
    answer[ai2[0][1]] = 1
    answer[ai2[-1][1]] = 0

    for i in range(n - 2, 0, -1):
        value, idx = ai2[i][0], ai2[i][1]
        num = idx % value
        for j in range(num, n, value):
            if ai[j] > value and answer[j] == 0:
                answer[idx] = 1
                break

    for i in range(n):
        if answer[i] == 1:
            print("A", end="")
        else:
            print("B", end="")


if __name__ == "__main__":
    # 示例：可根据需要修改 n 进行测试
    main(10)