import random

def main(n):
    # 1. 生成测试数据
    # 约束：arr 中元素为正整数，m 为任意整数（原代码中未使用）
    m = random.randint(1, max(1, n))  # 虽然没用到，但保留变量以贴近原逻辑
    arr = [random.randint(1, n) for _ in range(n)]

    # 2. 原始逻辑封装
    arr = sorted(arr, reverse=True)
    arr.append(0)
    isum = sum(arr)
    ans = []
    top = arr[0]
    for i in range(n):
        if arr[i] == 1:
            ans.append(1)
            arr[i + 1] = 1
            continue
        if arr[i + 1] > arr[i]:
            arr[i + 1] = arr[i]
        if arr[i] - arr[i + 1] == 0:
            ans.append(1)
            h = 1
        else:
            ans.append(arr[i] - arr[i + 1])
            h = arr[i] - arr[i + 1]

        top = arr[i] - h
        arr[i + 1] = top

    print(isum - sum(ans))


if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)