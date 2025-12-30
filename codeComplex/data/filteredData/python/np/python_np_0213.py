from itertools import combinations
import random

def main(n: int) -> int:
    # 生成规模为 n 的测试数据
    # p 为题目数量
    p = n

    # 生成题目难度列表 lst，值在 1~100 之间
    lst = [random.randint(1, 100) for _ in range(p)]

    # 生成 minn, maxn, dif，保证有一定合理性
    total_sum = sum(lst)
    avg = total_sum // p if p > 0 else 0

    minn = max(0, avg - 50)
    maxn = avg + 50
    dif = random.randint(0, 30)

    c = 0
    for i in range(2, p + 1):
        for j in combinations(lst, i):
            if (maxn >= sum(j) >= minn) and (max(j) - min(j) >= dif):
                c += 1
    return c

if __name__ == "__main__":
    # 示例：调用 main(10)，可根据需要修改 n
    result = main(10)
    print(result)