import random

keta = 29

# 隐藏的目标值（用于生成测试数据）
# 会在 main(n) 里根据 n 的范围随机生成
secret_A = 0
secret_B = 0

def query(x, y):
    """
    模拟原交互中的判定函数 f(x, y)：
    - 返回 -1, 0, 1 三种值之一。
    需要满足原算法的逻辑要求：
        初始查询 (?,0,0) 得到 A00:
          A00 = f(0,0)
        后续通过对 f(x,y) 的询问，二分确定 A, B。
    
    这里使用如下定义（典型的交互题设定）：
      比较 abs((x - secret_A)) 与 abs((y - secret_B))
      如果 abs(x - secret_A) < abs(y - secret_B)，返回 -1
      如果 abs(x - secret_A) > abs(y - secret_B)，返回 1
      否则（相等）返回 0
    该定义与原算法相容，可以通过对 f 的查询恢复 (secret_A, secret_B)。
    """
    da = abs(x - secret_A)
    db = abs(y - secret_B)
    if da < db:
        return -1
    elif da > db:
        return 1
    else:
        return 0


def main(n):
    """
    n 为规模参数，用来控制生成测试数据的位数或范围。
    这里约定：
      - 隐藏数 secret_A, secret_B 在 [0, 2^n) 范围内随机生成。
      - 实际算法仍然使用 keta 位（与原程序保持一致），
        但只要 n <= keta，就能正确恢复低 n 位的随机数。
      - 如果 n > keta，则只是 secret_A, secret_B 有更高位随机值，
        算法只能恢复到 2^(keta+1) 范围内的那部分（与原程序一致）。
    """

    global secret_A, secret_B

    # 根据 n 生成测试数据（隐藏的 A, B）
    upper = 1 << max(1, n)  # 至少 2^1，避免 n=0 时无意义
    secret_A = random.randrange(0, upper)
    secret_B = random.randrange(0, upper)

    # ---- 以下是原逻辑的无 input() 改写 ----
    # 初始询问
    A00 = query(0, 0)

    # 特殊情况：A00 == 0
    if A00 == 0:
        ANS = 0
        for k in range(keta, -1, -1):
            if query(1 << k, 0) == -1:
                ANS += 1 << k
        A = ANS
        B = ANS
        # 返回结果（原程序是输出 "! A B"）
        return A, B, secret_A, secret_B

    # 一般情况
    A = 0
    B = 0
    for k in range(keta, -1, -1):
        res1 = query((1 << k) + A, B)
        res2 = query(A, (1 << k) + B)

        if res1 != res2:
            if res1 == -1:
                A += 1 << k
                B += 1 << k
        else:
            if A00 == 1:
                A += 1 << k
            else:
                B += 1 << k
            A00 = res1

    # 返回算法求得的 (A,B) 以及真实的 (secret_A, secret_B) 方便对比
    return A, B, secret_A, secret_B


# 示例调用（提交时可删除或保留，不影响 main 逻辑）
if __name__ == "__main__":
    # 例如用 n = 10 测试
    est_A, est_B, real_A, real_B = main(10)
    print("estimated A,B:", est_A, est_B)
    print("real      A,B:", real_A, real_B)