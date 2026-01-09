from collections import defaultdict

def main(n):
    # 映射：n -> 数组长度，k 固定为 20（可根据需要调整规模）
    k = 20
    comp = (1 << k) - 1

    # 确定性生成数组：长度为 n，元素为 i ^ (i // 2)
    arr = [(i ^ (i // 2)) & comp for i in range(1, n + 1)]

    xors = defaultdict(int)
    xors[0] = 1
    ans = n * (n + 1) // 2
    xor = 0

    for a in arr:
        xor ^= a
        if xors[xor] > xors[comp ^ xor]:
            xor ^= comp
        ans -= xors[xor]
        xors[xor] += 1

    # print(ans)
    pass
if __name__ == "__main__":
    main(10)