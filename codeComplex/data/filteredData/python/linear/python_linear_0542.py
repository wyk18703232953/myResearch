import random

def main(n: int):
    # 生成规模为 n 的测试数据，这里示例为范围 [-10, 10]
    # 可根据需要自行调整生成规则
    arr = [random.randint(-10, 10) for _ in range(n)]

    k = min(arr)
    h = max(arr)
    s = 0
    for i in arr:
        if i >= 0:
            s += i
        else:
            s -= i

    if n == 1:
        result = arr[0]
    elif k < 0 and h >= 0:
        result = s
    else:
        if k >= 0:
            result = s - 2 * k
        else:
            result = s + 2 * h

    print(result)

if __name__ == "__main__":
    # 示例：调用 main(5)，可根据需要修改 n
    main(5)