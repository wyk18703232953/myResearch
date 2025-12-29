import random

def main(n: int):
    # 生成测试数据
    # 为了有交集，先生成一个基础集合，再拆成两个列表并加一些随机元素
    base_size = max(1, n // 2)
    base = random.sample(range(1, max(3, n * 2)), base_size)

    # 从 base 中随机挑若干元素放入 l1、l2，再各自补充一些不相交的元素
    l1_extra_size = max(0, n - base_size)
    l2_extra_size = max(0, n - base_size)

    l1 = base[:]  # 先放所有 base
    l2 = base[:]

    # 补充不相交的额外元素
    extra_pool_start = max(base) + 1 if base else 1
    extra_pool = list(range(extra_pool_start, extra_pool_start + l1_extra_size + l2_extra_size + 5))
    random.shuffle(extra_pool)

    l1.extend(extra_pool[:l1_extra_size])
    l2.extend(extra_pool[l1_extra_size:l1_extra_size + l2_extra_size])

    m = len(l2)

    # 原始逻辑（保留语义，修正错误判断）
    l3 = []
    for i in range(n):
        for j in range(m):
            if l1[i] == l2[j]:
                # 原代码中 `if l1[i] is not l3` 是错误的对象比较
                # 合理推断为避免重复元素
                if l1[i] not in l3:
                    l3.append(l1[i])

    print(*l3)


if __name__ == "__main__":
    # 示例调用，实际使用时可按需要修改或删除
    main(5)