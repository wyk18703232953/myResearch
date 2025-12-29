import random

def main(n: int) -> None:
    # 生成测试数据：长度为 n 的整数序列，可自行调整生成规则
    # 这里生成 1~(n//2+1) 之间的随机整数，允许重复
    l = [random.randint(1, max(1, n // 2 + 1)) for _ in range(n)]

    i = 0
    ans = 0
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            i = i + 1
            continue

        j = i + 1
        ind = -1
        while j < len(l):
            if l[j] == l[i]:
                ind = j
                break
            j = j + 1

        while ind > i + 1:
            l[ind], l[ind - 1] = l[ind - 1], l[ind]
            ans += 1
            ind -= 1

        i += 1

    print(ans)