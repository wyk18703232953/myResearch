import random

def main(n):
    # 生成测试数据
    # arr1 长度为 n，arr2 长度为 n 或稍有变化
    m = n
    # 为避免重复元素造成 index 的不确定行为，这里生成不重复的随机整数
    arr1 = random.sample(range(1, 10 * n + 1), n)
    # arr2 从 arr1 中选一部分再加上一些不在 arr1 中的元素
    common_part = random.sample(arr1, random.randint(0, n))
    extra_part = random.sample(
        [x for x in range(1, 10 * n + 1) if x not in arr1],
        random.randint(0, n)
    )
    arr2 = common_part + extra_part
    random.shuffle(arr2)

    # 原逻辑：输出 arr2 中同时在 arr1 中出现的元素，
    # 并按其在 arr1 中的顺序排序
    result = sorted([x for x in arr2 if x in arr1], key=lambda k: arr1.index(k))
    print(*result)

if __name__ == "__main__":
    # 示例：调用 main(5)
    main(5)