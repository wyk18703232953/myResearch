import random

def main(n: int) -> int:
    """
    将原逻辑封装为 main(n)，并在内部生成测试数据。
    n: 规模参数，用于控制生成的数据大小。
    返回：最终计算得到的 ans。
    """

    # 1. 生成测试数据
    # 约定：m ~ n，k ~ [1, max(1, n//10)]，mi 为递增序列
    m = max(1, n)                         # 保证至少 1 个元素
    k = max(1, n // 10)                   # 分页大小
    # 生成一个递增的正整数序列 mi（模拟原来的已排序位置）
    mi = []
    cur = 1
    for _ in range(m):
        cur += random.randint(1, 3)       # 控制增量，保持单调递增
        mi.append(cur)

    # 2. 原始逻辑
    ans = 0
    items_to_del = 0
    shift = 1
    c_page = None

    for el in mi:
        if c_page is None:
            c_page = (el - shift) // k
            items_to_del = 1
        else:
            page = (el - shift) // k
            if page != c_page:
                shift += items_to_del
                ans += 1
                c_page = (el - shift) // k
                items_to_del = 1
            else:
                items_to_del += 1

    if items_to_del != 0:
        ans += 1

    # 输出结果以保持原程序行为
    print(ans)
    return ans


if __name__ == "__main__":
    # 示例：用 n = 100 运行一次
    main(100)