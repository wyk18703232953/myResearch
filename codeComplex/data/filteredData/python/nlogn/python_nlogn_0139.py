from collections import defaultdict
import random

def main(n: int):
    # 生成测试数据：
    # n 为数组长度
    # k 在 [1, n+1] 范围内取一个值
    # 数组元素在 [1, 10*n] 内随机生成
    if n <= 0:
        return

    k = random.randint(1, max(2, n + 1))
    l = [random.randint(1, 10 * n) for _ in range(n)]

    # 原始逻辑
    if k == 1:
        ans = n
    else:
        l.sort()
        ndict = defaultdict(list)
        for x in l:
            i = x
            while i % k == 0:
                i = i // k
            ndict[i].append(x)
        ans = 0
        for group in ndict.values():
            count = 0
            while count < len(group):
                if count == len(group) - 1:
                    ans += 1
                    break
                if group[count] * k != group[count + 1]:
                    ans += 1
                    count += 1
                else:
                    ans += 1
                    count += 2

    print(ans)


if __name__ == "__main__":
    # 示例：规模为 10
    main(10)