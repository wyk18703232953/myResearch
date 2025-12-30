import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里生成 1..n 的随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    gap = n // 2
    count = 0

    # Shell 排序的变体
    while gap >= 1:
        for j in range(gap, n):
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    count += 1
                i -= gap
        gap //= 2

    if count % 2 == (3 * n) % 2:
        print("Petr")
    else:
        print("Um_nik")


if __name__ == "__main__":
    # 示例：运行 main，规模自定
    main(10)