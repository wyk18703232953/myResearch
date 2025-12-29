import random

def main(n: int):
    # 生成测试数据：根据规模 n 生成 l, r
    # 这里让 r 的二进制长度约为 n，比特位全部随机，且保证 l <= r
    if n <= 0:
        return 0

    # 生成一个 n 位的随机数 r（最高位保证为 1）
    r = random.getrandbits(n - 1) | (1 << (n - 1))
    # 生成 [0, r] 范围内的随机 l
    l = random.randint(0, r)

    # 以下为原始逻辑改写，无 input()
    p = bin(l)[2:]
    q = bin(r)[2:]

    t = len(q)
    u = len(p)
    p = (t - u) * '0' + p  # 左侧补零到与 q 同长
    ans = []

    # 找到首个与位状态符合规则的位置并构建 ans
    i = 0
    for i in range(len(q)):
        if q[i] == '1' and p[i] == '0':
            ans.append(1)
            break
        elif q[i] == '1' and p[i] == '1':
            ans.append(0)
            continue
        elif q[i] == '0' and p[i] == '1':
            ans.append(1)
            continue
        else:
            ans.append(0)
    # 后续位全部置为 1
    for j in range(i + 1, len(p)):
        ans.append(1)

    total = 0
    ans.reverse()
    for i in range(len(ans)):
        total += (1 << i) * ans[i]

    print(total)
    return total

if __name__ == "__main__":
    # 示例：规模 n = 10
    main(10)