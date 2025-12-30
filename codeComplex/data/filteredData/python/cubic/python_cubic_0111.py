from collections import defaultdict
import random

def main(n):
    # 根据规模 n 生成测试数据：这里生成 [-10,10] 之间的随机整数
    random.seed(0)
    a = [random.randint(-10, 10) for _ in range(n)]

    rec = defaultdict(list)
    # 枚举所有子数组，并按“子数组和”分类
    for j in range(n):
        s = 0
        for k in range(j, n):
            s += a[k]
            rec[s].append((j, k))

    ans = []
    # 对每种子数组和，选择最多的不相交子数组
    for key in rec.keys():
        tmp = []
        rec[key] = sorted(rec[key], key=lambda x: x[1])
        pre = -1
        for l, r in rec[key]:
            if pre >= l:
                continue
            tmp.append((l + 1, r + 1))
            pre = r
        if len(tmp) > len(ans):
            ans = tmp

    # 输出结果
    print(len(ans))
    for l, r in ans:
        print(l, r)


if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)