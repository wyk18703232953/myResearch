from functools import lru_cache
import random

mod = 10**9 + 7

def main(n):
    # 生成测试数据：
    # T 为总时间，这里设置为任务时间和的一半左右，保证可行性
    # 每个任务：S[i] = [time_i, color_i]
    random.seed(0)
    S = []
    total_time = 0
    for _ in range(n):
        t = random.randint(1, 10)  # 每个任务所需时间
        c = random.randint(0, 3)   # 每个任务的“颜色”或类型 0~3
        S.append([t, c])
        total_time += t

    # 设定 T（总时间），这里用所有任务时间和的一半向上取整
    T = max(1, total_time // 2)

    @lru_cache(maxsize=None)
    def calc(used, recent, time):
        ans = 0
        for i in range(n):
            if i in used:
                continue
            if time + S[i][0] > T:
                continue
            if S[i][1] == recent:
                continue
            if time + S[i][0] == T:
                ans += 1
            elif time + S[i][0] < T:
                used2 = list(used) + [i]
                used2.sort()
                recent2 = S[i][1]
                time2 = time + S[i][0]
                ans = (ans + calc(tuple(used2), recent2, time2)) % mod
        return ans

    result = calc(tuple(), -1, 0) % mod
    print(result)
    return result

if __name__ == "__main__":
    # 示例：规模 n = 8
    main(8)