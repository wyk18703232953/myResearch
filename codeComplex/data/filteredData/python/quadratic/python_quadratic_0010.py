from math import sqrt
import random

def main(n):
    # 生成测试数据：固定半径 r，随机生成 n 个横坐标
    r = 1
    # 你可以根据需要调整数据规模和范围
    x = [random.randint(0, 10 * n) for _ in range(n)]

    arr = []
    for i in range(n):
        arr.append(r)
        for j in range(i):
            if abs(x[j] - x[i]) <= (r * 2):
                arr[i] = max(
                    arr[i],
                    arr[j] + sqrt((r * r * 4) - ((x[j] - x[i]) * (x[j] - x[i])))
                )

    arr1 = [str(i) for i in arr]
    print(" ".join(arr1))

# 示例调用（可根据需要修改或在外部调用 main）
if __name__ == "__main__":
    main(5)