import math
import random

MOD = 10**9 + 7

def t_from_s_a_u(s, a, u):
    # time from distance s with acceleration a and initial speed u
    return (-2 * u + math.sqrt(4 * u * u + 8 * s * a)) / (2 * a)

def solve(A, V, L, D, W):
    if V <= W or W * W >= 2 * A * D:  # W irrelevant
        # can we get to speed V before distance L?
        if V * V >= 2 * A * L:
            return math.sqrt(2 * L / A)
        else:
            dist_1 = (V * V) / (2 * A)
            T1 = 2 * dist_1 / V
            dist_2 = L - dist_1
            T2 = dist_2 / V
            return T1 + T2
    else:
        # V > W, and we reach W in distance D
        dist_1 = (W * W) / (2 * A)
        T1 = math.sqrt(2 * dist_1 / A)
        rem_dist = D - dist_1
        dist_A = (V * V - W * W) / (2 * A)

        if 2 * dist_A >= rem_dist:
            # accelerate then decelerate the whole time within rem_dist
            TA = 2 * t_from_s_a_u(rem_dist / 2, A, W)
        else:
            TA1 = 2 * (V - W) / A
            SA1 = (V + W) * (V - W) / A
            SA2 = rem_dist - SA1
            TA2 = SA2 / V
            TA = TA1 + TA2

        T1 += TA

        # now we are at speed W again at position D, then go to end
        if V * V - W * W >= 2 * A * (L - D):
            # accelerate linearly from W to some speed (<= V) over distance L-D
            return T1 + t_from_s_a_u(L - D, A, W)
        else:
            dist_2 = (V * V - W * W) / (2 * A)
            T2 = 2 * dist_2 / (V + W)
            dist_3 = L - D - dist_2
            T3 = dist_3 / V
            return T1 + T2 + T3

def main(n):
    # generate one random test case using n as a scale factor
    # make n at least 1 to avoid degenerate ranges
    n = max(1, int(n))

    # acceleration A in [1, 10*n]
    A = random.randint(1, 10 * n)

    # base speed scale
    base_speed = max(1, n)

    # maximum speed V in [1, 20*base_speed]
    V = random.randint(1, 20 * base_speed)

    # total distance L in [1, 100*n]
    L = random.randint(1, 100 * n)

    # camera position D in [0, L]
    D = random.randint(0, L)

    # speed limit W in [1, 20*base_speed]
    W = random.randint(1, 20 * base_speed)

    ans = solve(A, V, L, D, W)
    # print input used and the resulting time for visibility
    print(A, V)
    print(L, D, W)
    print(ans)

if __name__ == "__main__":
    # example: run with n = 10
    main(10)