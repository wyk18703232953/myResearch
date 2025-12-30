import bisect as bi
import random

def main(n):
    # 规模设定：数组 a 长度为 n，查询次数 q 也设为 n
    q = n

    # 根据 n 生成测试数据
    # 元素为 1~10 的正整数，保证前缀和单调递增
    a = [random.randint(1, 10) for _ in range(n)]
    l = [random.randint(1, 10) for _ in range(q)]

    som = sum(a)
    e = 0
    p = []
    for i in a:
        e += i
        p.append(e)

    e = 0
    for i in l:
        e += i
        if e >= som:
            e = 0
        x = bi.bisect(p, e)
        print(n - x)


if __name__ == "__main__":
    # 示例调用：n 可按需修改
    main(10)