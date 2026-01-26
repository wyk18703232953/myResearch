import math

def main(n):
    # n 表示队列数量 q
    q = max(1, n)
    # 构造长度为 q 的列表 a，完全确定性
    # 例如第 i 个元素为 (i+1)^2 + i
    a = [(i + 1) * (i + 1) + i for i in range(q)]

    earliest_time = 10 ** 9 + 1000
    earliest_queue = 1
    for i in range(q):
        turns = int(max(0, math.ceil((a[i] + 1 - (i + 1)) / q)))
        t = (i + 1) + turns * q
        if t < earliest_time:
            earliest_time = t
            earliest_queue = i + 1

    return earliest_queue

if __name__ == "__main__":
    # 示例调用：可以修改 n 测试不同规模
    result = main(10)
    # print(result)
    pass