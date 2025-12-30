import random

def main(n: int) -> int:
    # 生成测试数据：长度为 2 * n 的数组，每个数字恰好出现两次
    # 保证原算法中的 xs.index(xs[0], 1) 总能在后面找到匹配
    xs = list(range(1, n + 1)) * 2
    random.shuffle(xs)

    res = 0

    # 原逻辑：反复取 xs[0]，在后面找到相同元素位置 j
    # 计算 j - 1 累加后，删除这一对元素
    while xs:
        j = xs.index(xs[0], 1)
        res += j - 1
        xs = xs[1:j] + xs[j + 1:]

    # 这里返回结果，方便测试使用
    return res


if __name__ == "__main__":
    # 示例：运行时默认测试 n=5，可根据需要修改
    print(main(5))