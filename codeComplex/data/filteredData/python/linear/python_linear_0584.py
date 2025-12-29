import random

mod = 10**9 + 7

def count_ones(m, n, mod):
    return (pow(2, m, mod) - 1) * pow(2, n, mod) % mod

def main(n):
    # 1. 生成规模为 n 的字符串 S（长度为 n，由 '0'、'1' 组成）
    random.seed(0)
    S = ''.join(random.choice('01') for _ in range(n))
    
    # 2. 生成查询个数 q（这里取 q = n，亦可按需调整规则）
    q = n
    
    # 3. 生成 q 个区间 [l, r]，1 <= l <= r <= n
    LR = []
    for _ in range(q):
        l = random.randint(1, n)
        r = random.randint(l, n)
        LR.append((l, r))
    
    # 4. 预处理 LIST（前缀和：到当前位置为止 '1' 的个数）
    LIST = [0]
    for s in S:
        if s == "1":
            LIST.append(LIST[-1] + 1)
        else:
            LIST.append(LIST[-1])
    
    # 5. 处理并输出每个查询的结果
    for l, r in LR:
        ones = LIST[r] - LIST[l - 1]
        zeros = (r - l + 1) - ones
        print(count_ones(ones, zeros, mod))

if __name__ == "__main__":
    # 示例调用：可按需修改 n
    main(10)