from operator import itemgetter
import random

def main(n):
    # 生成测试数据：随机生成 m 个区间
    # 这里设定 m 与 n 同阶，可按需修改生成策略
    m = max(1, n)  # 至少 1 个区间
    intervals = []
    for _ in range(m):
        l = random.randint(0, n - 1)
        r = random.randint(l, n - 1)
        intervals.append((l, r))

    # 排序区间（与原程序一致）
    a = sorted(intervals, key=itemgetter(0, 1))

    ans = [-1] * n
    for l, r in a:
        if ans[l] == -1:
            flag = 1
            for i in range(l, r + 1):
                if flag:
                    ans[i] = 1
                else:
                    ans[i] = 0
                flag ^= 1
        else:
            flag = 1
            x = ans[l]
            for i in range(l, r + 1):
                if flag:
                    ans[i] = x
                else:
                    ans[i] = x ^ 1
                flag ^= 1

    for i in range(n):
        if ans[i] == -1:
            ans[i] = 0

    ans_str = ''.join(map(str, ans))
    print(ans_str)
    return ans_str

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可自行调整
    main(10)