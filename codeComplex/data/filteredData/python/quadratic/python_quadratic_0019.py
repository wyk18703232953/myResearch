from collections import defaultdict
import random

mod_v = 1000000007

# Precompute binomial coefficients C(n,k) modulo mod_v up to 1009
temp_arr = [[1]]
for i in range(1, 1010):
    a = [1]
    for k in range(1, i):
        a.append((temp_arr[i - 1][k - 1] + temp_arr[i - 1][k]) % mod_v)
    a.append(1)
    temp_arr.append(a)

# Precompute ans_arr using the same logic as in the original code
ans_arr = [1]
for i in range(1, 1010):
    res = 0
    for j in range(i):
        res += ans_arr[j] * temp_arr[i - 1][j]
        res %= mod_v
    ans_arr.append(res)


def main(n: int) -> None:
    """
    n: problem scale, interpreted as number of columns.
    We generate a random 'lines' count (number of rows) and random 0/1 matrix.
    The rest of the logic is preserved from the original program.
    """
    # You can adjust how lines is chosen based on n; here we cap by 30 for bit-packing safety.
    lines = min(30, max(1, n))

    # Generate random test data: 'lines' rows, each row is a length-n list of 0/1
    new_list = [0 for _ in range(n)]
    for i in range(lines):
        row_bits = [random.randint(0, 1) for _ in range(n)]
        for k in range(n):
            new_list[k] |= row_bits[k] << i

    default_d = defaultdict(int)
    for k in new_list:
        default_d[k] += 1

    answer = 1
    for cnt in default_d.values():
        if cnt < len(ans_arr):
            answer = answer * ans_arr[cnt] % mod_v
        else:
            # Fallback if generated cnt exceeds precomputation; extend if needed.
            # For now, treat it as 0-contribution (same as multiplying by 1).
            answer = answer * 1 % mod_v

    print(answer)


if __name__ == "__main__":
    # Example: run with some default scale
    main(5)