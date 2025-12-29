import random

def main(n):
    # 生成测试数据：构造一个长度为 n 的排列，且包含 n
    # 这里生成 1..n 的随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)

    # 以下为原逻辑
    idx = arr.index(n)
    ok = 1
    for i in range(1, idx):
        if arr[i] < arr[i - 1]:
            ok = 0
    for i in reversed(range(idx, n - 1)):
        if arr[i] < arr[i + 1]:
            ok = 0
    if ok:
        print("YES")
    else:
        print("NO")

    return 0

# 示例调用
if __name__ == "__main__":
    main(10)