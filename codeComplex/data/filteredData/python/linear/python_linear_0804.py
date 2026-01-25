import math

def main(n):
    # 映射规则：
    # n: 操作数列表 p 的长度
    # 固定 n, m, k 的关系，使规模主要由 len(p) 控制
    # n_param: 原程序中的 n
    n_param = n
    m = n_param * 2 if n_param > 0 else 0
    k = max(1, n_param // 3)  # k 至少为 1

    # 确定性构造 p 列表，长度为 m，元素单调递增
    # p[i] = (i + 1) * 2 确保有序且正数
    p = [(i + 1) * 2 for i in range(m)]

    i = 0
    ct = 0
    ops = 0
    while i < len(p):
        nm = p[i] - ct
        if nm % k == 0:
            mnm = nm
        else:
            mnm = (nm // k) * k + k
        si = i
        while i < len(p) and p[i] - ct <= mnm:
            i += 1
        ct += i - si
        ops += 1
        if i >= len(p):
            break
    print(ops)


if __name__ == "__main__":
    # 示例：用若干不同规模运行
    for scale in [1, 5, 10, 100]:
        print(f"n={scale} -> ", end="")
        main(scale)