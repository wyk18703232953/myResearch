from collections import defaultdict

mod_v = 1000000007

# Precompute Pascal triangle (binomial coefficients mod mod_v)
temp_arr = [[1]]
for i in range(1, 1010):
    a = [1]
    for k in range(1, i):
        a.append((temp_arr[i - 1][k - 1] + temp_arr[i - 1][k]) % mod_v)
    a.append(1)
    temp_arr.append(a)

# Precompute ans_arr based on temp_arr
ans_arr = [1]
for i in range(1, 1010):
    res = 0
    for j in range(i):
        res += ans_arr[j] * temp_arr[i - 1][j]
        res %= mod_v
    ans_arr.append(res)


def generate_input_structure(n):
    # Map n to (n, lines) where lines <= 30 for bit operations
    if n <= 0:
        n = 1
    lines = (n % 30) + 1  # 1..30
    size = n
    return size, lines


def generate_bit_matrix(size, lines):
    # Deterministic generation of a matrix of '0'/'1' characters
    # pattern: bit at position (i,k) is ((i * 131 + k * 17) % 2)
    matrix = []
    for i in range(lines):
        row_bits = []
        for k in range(size):
            bit = (i * 131 + k * 17) % 2
            row_bits.append(str(bit))
        matrix.append(row_bits)
    return matrix


def main(n):
    size, lines = generate_input_structure(n)

    # Simulate original input-based construction of new_list
    new_list = [0 for _ in range(size)]

    matrix = generate_bit_matrix(size, lines)
    for i in range(lines):
        # original code: input1 = list(map(int, input()))
        # here we convert each character to int
        input1 = [int(ch) for ch in matrix[i]]
        for k in range(size):
            new_list[k] |= input1[k] << i

    default_d = defaultdict(int)
    for k in new_list:
        default_d[k] += 1

    answer = 1
    for cnt in default_d.values():
        # ensure we don't exceed precomputed ans_arr size
        idx = cnt if cnt < len(ans_arr) else len(ans_arr) - 1
        answer = answer * ans_arr[idx] % mod_v

    # print(answer)
    pass
    return answer


if __name__ == "__main__":
    # Example deterministic call for time-complexity experiments
    main(1000)