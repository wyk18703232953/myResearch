from collections import defaultdict
import random

def main(n):
    # 生成测试数据：n 个区间，端点在 [1, n] 内，确保 l <= r
    intervals = []
    for _ in range(n):
        l = random.randint(1, n)
        r = random.randint(1, n)
        if l > r:
            l, r = r, l
        intervals.append((l, r))

    arr = defaultdict(int)
    for l, r in intervals:
        arr[l] += 1
        arr[r + 1] -= 1

    brr = [0] * (n + 1)

    keys = sorted(arr.keys())
    if not keys:
        print(*brr[1:])
        return

    current_sum = arr[keys[0]]
    prev_point = keys[0]

    for key in keys[1:]:
        if 1 <= current_sum <= n:
            brr[current_sum] += key - prev_point
        prev_point = key
        current_sum += arr[key]

    print(*brr[1:])

if __name__ == "__main__":
    # 示例：可修改 n 以改变规模
    main(10)