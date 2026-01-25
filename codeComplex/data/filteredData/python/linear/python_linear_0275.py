n, m, a, b = 0, 0, 0, 0

def generate_inputs(n):
    if n < 4:
        k = 4
    else:
        k = n
    global n_val, m_val, a_val, b_val
    n_val = k
    m_val = max(1, k // 2)
    a_val = k % 7 + 1
    b_val = (k // 3) % 10 + 1

def core_logic(n, m, a, b):
    z = (n % m) * b
    x = ((n // m + 1) * m - n) * a
    y = min(z, x)
    return y if y > 0 else 0

def main(n):
    generate_inputs(n)
    return core_logic(n_val, m_val, a_val, b_val)

if __name__ == "__main__":
    result = main(10)
    print(result)