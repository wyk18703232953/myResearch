import random

def ask(x, arr):
    # 交互函数改为直接访问生成的数据
    return arr[x - 1]

def main(n):
    # 根据 n 生成测试数据：
    # 为了保持与原二分逻辑相容，这里构造一个在长度为 n 的环上，
    # 相隔 t = n//2 的位置值相等的数组，并保证 t 为偶数（否则原程序直接输出 -1）
    t = n // 2
    if t & 1:  # 若 t 为奇数，按照原程序逻辑，无解
        print('! -1')
        return

    # 构造一个长度为 n 的数组 arr，使得 arr[i] == arr[(i + t) % n]
    base_len = t
    base = [random.randint(1, 1000) for _ in range(base_len)]
    arr = base + base[:]  # 长度 2 * t == n，并满足相隔 t 的位置值相等

    l = 1
    r = n
    while l < r:
        mid = (l + r) >> 1
        if ask(mid, arr) >= ask((mid + t - 1) % n + 1, arr):
            r = mid
        else:
            l = mid + 1

    print('! %d' % l)


if __name__ == "__main__":
    # 示例运行，可根据需要修改 n
    main(10)