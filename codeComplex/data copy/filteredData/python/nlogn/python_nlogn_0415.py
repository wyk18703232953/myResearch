from collections import defaultdict

def main(n):
    arr = defaultdict(int)

    # 确定性区间生成：n 个区间，左端点从 1 到 n，右端点为左端点加上一个确定性长度
    # 例如区间为 [i, i + (i % 5)]，保证右端点 >= 左端点
    for i in range(1, n + 1):
        l = i
        r = i + (i % 5)
        arr[l] += 1
        arr[r + 1] -= 1

    brr = [0] * (n + 1)

    keys = sorted(arr.keys())
    current_sum = arr[keys[0]]
    prev_point = keys[0]

    for key in keys[1:]:
        if current_sum <= n:
            brr[current_sum] += key - prev_point
        prev_point = key
        current_sum += arr[key]

    # 与原程序一致，从索引 1 开始输出
    # print(*brr[1:])
    pass
if __name__ == "__main__":
    main(10)