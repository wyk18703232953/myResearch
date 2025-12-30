import math
import random

def main(n):
    # n 为规模，这里我们用 n 作为 m（即 p 的元素个数）
    # 生成测试数据：
    #   n: 总页数上限（随意设置为 n*k 的量级）
    #   m: 删除位置数量
    #   k: 每次页面跨度
    #
    # 简单策略：
    #   k 取 1~n 的随机值
    #   n_pages 取 n*k 的量级
    #   p 为 1 ~ n_pages 中随机选出的 m 个位置并排序
    if n <= 0:
        print(0)
        return

    m = n
    k = max(1, n // 10)  # 控制每页容量规模
    n_pages = n * k

    # 生成 m 个不同的随机位置
    p = random.sample(range(1, n_pages + 1), m)
    p.sort()

    page_max = k
    action_count = 0
    index = 0

    while index < m:
        while index < m and p[index] <= page_max:
            count = 0
            while index < m and p[index] <= page_max:
                index += 1
                count += 1
            if count > 0:
                action_count += 1
            page_max += count

        if index >= m:
            break

        pc = math.ceil((p[index] - page_max) / k)
        page_max += k * pc

    print(action_count)


if __name__ == "__main__":
    # 示例：规模为 100
    main(100)