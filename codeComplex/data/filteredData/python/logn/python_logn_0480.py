from bisect import bisect_left as bsl
import random

def main(n):
    # 这里的 n 作为测试规模，用来生成一个“第 k 位数字”的查询
    # 原逻辑：输入 k，找出无限串 "123456789101112..." 的第 k 位数字
    
    # 预处理每个长度的数字贡献
    cur = 9
    count = 1
    tot = 0
    num = []
    cc = []
    for _ in range(11):
        num.append(cur * count)   # 有 cur 个 count 位数，总贡献 cur*count 位
        tot += cur
        cc.append(tot)            # 一共 tot 个数（从 1 开始 到 当前位数上限）
        cur *= 10
        count += 1

    ans = [num[0]]                # ans[i] 表示所有 <= i+1 位数的数字位数总和
    for i in range(1, 11):
        ans.append(ans[-1] + num[i])

    # 用 n 构造测试数据：令 k 为 1 到 n*n 之间的某个值
    # 为了可重复和简单，这里取 k = n*n
    if n <= 0:
        return
    k = n * n

    # 主逻辑：给定 k，求第 k 位数字
    ind = min(bsl(ans, k), 10)
    left = k
    if ind > 0:
        left -= ans[ind - 1]

    # left 是在 (ind+1) 位数区间内的偏移（按位计数）
    nums = left // (ind + 1)
    rem = left % (ind + 1)
    if rem != 0:
        nums += 1
    if ind > 0:
        nums += cc[ind - 1]

    answer = [int(ch) for ch in str(nums)]
    # rem 是该数字中的第 rem 位（从 1 开始）
    print(answer[rem - 1] if rem > 0 else answer[-1])


if __name__ == "__main__":
    # 示例：以 n=10 运行
    main(10)