import math

def calc(v0, v, a, x):
    t = (v - v0) / a
    x0 = v0 * t + 0.5 * a * t * t
    if x0 >= x:
        return (x, (math.sqrt(v0 * v0 + 2 * a * x) - v0) / a)
    return (x0, t)

def go(v0, v, a, x):
    x0, t = calc(v0, v, a, x)
    return t + (x - x0) / v

def generate_inputs(n):
    # Deterministically generate (a, v, l, d, w) from n
    # Ensure positive values and reasonable relations
    a = (n % 5) + 1          # 1..5
    v = (n % 20) + 5         # 5..24
    l = max(10, n * 2)       # at least 10
    d = max(1, n)            # 1.., and will be <= l
    if d > l:
        d = l
    w = (n % (v + 1))        # 0..v
    return a, v, l, d, w

def main(n):
    a, v, l, d, w = generate_inputs(n)
    if w > v:
        w = v
    x, t = calc(0, w, a, d)
    if x == d:
        result = go(0, v, a, l)

    else:
        result = t + go(w, v, a, (d - x) * 0.5) * 2 + go(w, v, a, l - d)
    return result

if __name__ == "__main__":
    # Example deterministic call; change n to scale input size
    # print(main(10))
    pass