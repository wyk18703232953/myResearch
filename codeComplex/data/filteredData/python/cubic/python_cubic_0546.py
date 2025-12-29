import random

def listtostring(string):
    return ''.join(str(ele) for ele in string)

def main(n: int):
    # 1. 生成测试数据：长度为 n 的数字串 a 和 b
    # 生成 a 的数字列表（允许前导 0）
    a = [random.randint(0, 9) for _ in range(n)]
    a.sort()  # 保持与原程序一致：先排序 a

    # 生成 b，确保数值上 >= 排序后的 a
    # 做法：先生成一个至少与 a 等长且数值 >= a 的上界字符串
    # 方法：先构造 b_base >= a，允许适当随机放大
    a_str = listtostring(a)
    a_int = int(a_str)

    # 在 [a_int, a_int + 10^n - 1] 范围内随机取一个 b_int
    # 上界避免溢出太大
    max_add = 10 ** n - 1
    b_int = a_int + random.randint(0, max_add)
    b_str = str(b_int)

    # 若长度不足 n，左侧补 0，使其和原始输入风格统一（列表每位一个字符）
    if len(b_str) < n:
        b_str = b_str.zfill(n)

    b = list(b_str)

    # 2. 原逻辑
    n_len = len(a)

    for i in range(n_len):
        for j in range(n_len):
            t = a.copy()
            t[i], t[j] = t[j], t[i]
            t_val = int(listtostring(t))
            a_val = int(listtostring(a))
            b_val = int(listtostring(b))
            if a_val <= t_val <= b_val:
                a[i], a[j] = a[j], a[i]

    # 3. 输出结果
    print(listtostring(a))

if __name__ == "__main__":
    # 示例：调用 main，规模 n 可按需修改
    main(5)