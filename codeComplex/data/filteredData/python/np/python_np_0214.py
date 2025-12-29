from itertools import combinations
import random

def main(n: int):
    # 生成测试数据：
    # p 为元素个数，取 n
    p = n

    # 生成一个有 p 个元素的整数数组 lst，元素范围可按需调整
    lst = [random.randint(0, 100) for _ in range(p)]

    # 根据 lst 的大致范围设置 minn, maxn, dif，供测试使用
    total_sum = sum(lst)
    minn = total_sum // 4        # 任意示例下界
    maxn = (total_sum * 3) // 4  # 任意示例上界
    dif = max(1, (max(lst) - min(lst)) // 3)  # 任意示例差值条件

    # 原逻辑计算
    ans = sum(
        sum(
            (maxn >= sum(j) >= minn) and ((max(j) - min(j)) >= dif)
            for j in combinations(lst, i)
        )
        for i in range(2, p + 1)
    )

    print(ans)


if __name__ == "__main__":
    # 示例调用：n 为规模
    main(10)