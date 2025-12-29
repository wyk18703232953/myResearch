from sys import stdout
import random


def main(n: int):
    # 根据 n 生成测试数据，这里假设有一个隐藏数组 arr，长度为 n，
    # 并保证在 i 和 i + n//2 位置存在“特殊结构”，与原交互逻辑兼容。
    # 为了演示，生成一个随机数组，并人为设置一个解的位置 pos。
    if n % 2 == 1:
        raise ValueError("n 必须为偶数，且原题要求 n % 4 != 2")

    # 生成随机数组
    arr = [random.randint(0, 1000) for _ in range(n)]

    # 构造一个满足条件的解位置 pos：arr[pos] == arr[pos + n//2]
    # 为简单起见，如果 n % 4 == 2，本来是无解情况，原程序直接输出 -1 退出。
    # 我们保留原有逻辑：这种情况下直接打印 -1 并返回。
    if n % 4 == 2:
        print("! -1")
        return

    # 选择一个解位置 pos（1-based 索引）
    pos = random.randint(1, n // 2)
    arr[pos - 1 + n // 2] = arr[pos - 1]  # 强制满足 arr[pos] == arr[pos + n//2]

    # 定义 query 函数模拟原来的交互“? i”
    def query(idx: int) -> int:
        # idx 是 1-based 索引
        return arr[idx - 1]

    # 以下是将原来的交互逻辑直接改写为调用 query()

    # 原交互：读入 n 后的逻辑已经由 main(n) 接管

    # 对位置 1 和 1 + n//2 进行初始查询
    print("?", 1)
    stdout.flush()
    a = query(1)

    print("?", 1 + n // 2)
    stdout.flush()
    b = query(1 + n // 2)

    # 若一开始即满足条件，则答案为 1
    if a == b:
        print("!", 1)
        return

    l = 1
    r = 1 + n // 2

    while l != r:
        mid = (l + r) // 2

        print("?", mid)
        stdout.flush()
        c = query(mid)

        print("?", mid + n // 2)
        stdout.flush()
        d = query(mid + n // 2)

        if c == d:
            print("!", mid)
            return

        if a < b:
            if c < d:
                l = mid + 1
            else:
                r = mid
        else:
            if c > d:
                l = mid + 1
            else:
                r = mid

    print("!", l)


# 示例：如果需要运行测试，可在此调用 main
# if __name__ == "__main__":
#     main(8)