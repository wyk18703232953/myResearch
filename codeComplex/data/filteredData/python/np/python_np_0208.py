import random

def main(n: int) -> None:
    # 生成测试数据
    # n: 题目中的任务数量
    # 其余参数 l, r, x 以及 tasks 随机生成，可按需要调整范围
    random.seed(0)

    # 随机生成任务难度
    tasks = [random.randint(1, 10**3) for _ in range(n)]

    # 生成参数，使得有一定概率存在合法解
    total = sum(tasks)
    l = random.randint(0, max(0, total // 4))
    r = random.randint(max(l, total // 4), total)
    x = random.randint(0, max(tasks) - min(tasks) if n > 1 else 0)

    # 原逻辑
    mask = 3
    ans = 0

    while mask < (1 << n):
        sum_dif = 0
        min_diff = float("inf")
        max_diff = -float("inf")

        if mask & (mask - 1):
            for i in range(n):
                if mask & (1 << i):
                    sum_dif += tasks[i]
                    min_diff = min(min_diff, tasks[i])
                    max_diff = max(max_diff, tasks[i])
            if (x <= (max_diff - min_diff)) and (l <= sum_dif <= r):
                ans += 1

        mask += 1

    print(ans)

# 示例调用
if __name__ == "__main__":
    main(10)