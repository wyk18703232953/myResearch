from operator import itemgetter
import random

def main(n: int) -> int:
    """
    n: 规模（点的数量）
    返回：按照原逻辑计算得到的答案（int）

    自动生成 n 个点，每个点为 [x, t]，并附加和 x+t 用于排序：
    - x 在 [-10**9, 10**9] 范围内
    - t 在 [0, 10**9] 范围内
    """
    points = []
    for _ in range(n):
        # 生成测试数据，可根据需要调整范围
        x = random.randint(-10**9, 10**9)
        t = random.randint(0, 10**9)
        points.append([x, t, x + t])

    # 对应原 process_task
    points.sort(key=itemgetter(2))
    last = 0
    ans = 1 if n > 0 else 0
    for i in range(1, n):
        if points[i][0] - points[i][1] >= points[last][0] + points[last][1]:
            last = i
            ans += 1

    return ans


if __name__ == "__main__":
    # 示例：运行规模为 10 的测试
    n = 10
    print(main(n))