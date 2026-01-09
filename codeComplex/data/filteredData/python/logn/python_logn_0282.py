import sys, math

m = 1000000007

def pow2(k):
    if k == 0:
        return 1
    z = pow2(k // 2)
    if k % 2 == 1:
        return (2 * z * z) % m

    else:
        return (z * z) % m

def core(x, k):
    if x == 0:
        return 0
    t = pow2(k)
    a = x * t
    b = a - t + 1
    return (a + b) % m

def main(n):
    # 生成确定性的 (x, k) 输入：
    # 规模含义：n 为测试用例数量
    # 对于第 i 个测试用例：x = i, k = i // 2
    results = []
    for i in range(1, n + 1):
        x = i
        k = i // 2
        res = core(x, k)
        results.append(res)
    # 输出所有结果，避免 I/O 成为瓶颈，仅做一次打印
    for r in results:
        # print(r)
        pass
if __name__ == "__main__":
    # 示例调用，n 为规模参数，可根据实验需要修改
    main(10)