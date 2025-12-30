import random

def main(n: int):
    # 1. 生成测试数据：根据规模 n 生成 l, r
    # 这里让 r - l 的规模大约为 2^n 量级，保证有意义的区间
    if n <= 0:
        n = 1
    # 生成一个 n 比特以内的随机 l
    l = random.randint(0, max(1, (1 << n) - 1))
    # 生成 r >= l，且不超过 n+1 比特
    r = random.randint(l, l + (1 << n))
    
    # 2. 原逻辑移植（去掉 input）
    if l == r:
        print(0)
        return

    binr, binl = bin(r)[2:], bin(l)[2:]
    binl = '0' * (len(binr) - len(binl)) + binl

    for i in range(len(binl)):
        if binl[i] != binr[i]:
            binl = '1' * len(binl[i:])
            break

    print(int(binl, 2))


# 示例：自行调用 main
if __name__ == "__main__":
    main(10)