import random

def main(n):
    # 生成测试数据：arr 为 1..n 的随机排列
    arr = list(range(1, n + 1))
    random.shuffle(arr)
    # 生成测试数据：brr 为 1..n 的随机排列
    brr = list(range(1, n + 1))
    random.shuffle(brr)

    numb = [0 for _ in range(n + 1)]
    for i in range(len(arr)):
        numb[arr[i]] = i + 1

    ind = 0
    out = []
    for c in brr:
        total = 0
        num = numb[c]
        if num > ind:
            total = num - ind
            ind = num
        out.append(str(total))

    print(" ".join(out))

if __name__ == "__main__":
    # 示例：调用 main(10)
    main(10)