import math
import random

def t_from_s_a_u(s, a, u):
    return (-2 * u + math.sqrt(4 * u * u + 8 * s * a)) / (2 * a)

def solve_single(A, V, L, D, W):
    if V <= W or W ** 2 >= 2 * A * D:  # W irrelevant
        # can we get to speed V before distance L?
        if V ** 2 >= 2 * A * L:
            return math.sqrt(2 * L / A)
        else:
            dist_1 = (V ** 2) / (2 * A)
            T1 = 2 * dist_1 / V
            dist_2 = L - dist_1
            T2 = dist_2 / V
            return T1 + T2
    else:
        # V > W, and we reach W in time
        dist_1 = (W ** 2) / (2 * A)
        T1 = math.sqrt(2 * dist_1 / A)
        rem_dist = D - dist_1
        dist_A = (V ** 2 - W ** 2) / (2 * A)
        if 2 * dist_A >= rem_dist:
            # accelerate then decelerate the whole time
            TA = 2 * t_from_s_a_u(rem_dist / 2, A, W)
        else:
            TA1 = 2 * (V - W) / A
            SA1 = (V + W) * (V - W) / A
            SA2 = rem_dist - SA1
            TA2 = SA2 / V
            TA = TA1 + TA2
        T1 += TA
        # now we are at speed W again, so we accelerate to V and then cruise
        if V ** 2 - W ** 2 >= 2 * A * (L - D):
            return T1 + t_from_s_a_u(L - D, A, W)
        else:
            dist_2 = (V ** 2 - W ** 2) / (2 * A)
            T2 = 2 * dist_2 / (V + W)
            dist_3 = L - D - dist_2
            T3 = dist_3 / V
            return T1 + T2 + T3

def main(n):
    """
    生成 n 组随机测试数据并输出对应的结果。
    规模 n 表示测试用例数量。
    """
    random.seed(0)
    results = []
    for _ in range(n):
        # 生成测试数据：
        # A: [1, 10], V: [1, 50], L: [1, 1000], D: [0, L], W: [0, V]
        A = random.randint(1, 10)
        V = random.randint(1, 50)
        L = random.randint(1, 1000)
        D = random.randint(0, L)
        W = random.randint(0, V)
        ans = solve_single(A, V, L, D, W)
        results.append((A, V, L, D, W, ans))

    # 输出格式：每行一个测试用例及其答案
    for A, V, L, D, W, ans in results:
        print(f"A={A} V={V} L={L} D={D} W={W} -> time={ans}")

if __name__ == "__main__":
    # 示例：生成 5 组测试
    main(5)