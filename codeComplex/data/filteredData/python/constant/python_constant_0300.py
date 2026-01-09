from math import *


def main(n):
    """
    n: 控制测试数据规模（这里简单用来生成 k, n, s, p 四个参数）
    原题逻辑：
    输入 k, n, s, p
    输出需要购买的笔记本本数：
        每个笔记本有 p 页
        每个学生一次需要 n 页
        每次发放以 s 页为一份
        共有 k 个学生
    """
    # 根据规模 n 构造测试数据（可按需修改生成规则）
    # 为避免除零和太小数据，这里做一个简单安全构造：
    k = max(1, n)           # 学生数量
    pages_needed = max(1, n)  # 每个学生需要的页数
    s = max(1, n // 3 or 1)   # 每次发放的页数
    p = max(1, n // 5 or 1)   # 每本笔记本的页数

    # 原公式：
    # t = k * ceil(n / s)
    # ans = ceil(t / p)
    t = k * (pages_needed // s + (pages_needed % s != 0))
    ans = t // p + (t % p != 0)

    # print(ans)
    pass
if __name__ == "__main__":
    # 示例：以 10 作为规模调用
    main(10)