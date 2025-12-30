from itertools import groupby
import random

def main(n: int):
    # 1) 生成测试数据：先随机构造一个合法的 answer，然后由它反推 l 和 r
    # 生成一个 1..n 的随机排列作为最终糖果分配
    answer = list(range(1, n + 1))
    random.shuffle(answer)

    # 由 answer 计算 l、r
    l = []
    for i in range(n):
        cnt = 0
        for j in range(i):
            if answer[j] > answer[i]:
                cnt += 1
        l.append(cnt)

    r = []
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if answer[j] > answer[i]:
                cnt += 1
        r.append(cnt)

    # 2) 用原始逻辑（无 input）验证 l, r 是否能还原出相同的 answer
    sums = [(a + b, ind) for (ind, (a, b)) in enumerate(zip(l, r))]
    sums.sort()
    rec_answer = [None] * n
    curr_candies = n
    for key, group in groupby(sums, key=lambda i: i[0]):
        for elem in group:
            rec_answer[elem[1]] = curr_candies
        curr_candies -= 1

    tl = []
    for i in range(n):
        cnt = 0
        for j in range(i):
            if rec_answer[j] > rec_answer[i]:
                cnt += 1
        tl.append(cnt)

    tr = []
    for i in range(n):
        cnt = 0
        for j in range(i + 1, n):
            if rec_answer[j] > rec_answer[i]:
                cnt += 1
        tr.append(cnt)

    if tl != l or tr != r:
        print("NO")
    else:
        print("YES")
        print(' '.join(map(str, rec_answer)))


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)