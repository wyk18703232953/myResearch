import math

MOD = 10 ** 9 + 7

# Precomputed coefficients for n = 0..16
RES = [0, 1, 0, 3, 0, 15, 0, 133, 0, 2025, 0, 37851, 0, 1030367, 0, 36362925, 0]

def main(n: int):
    # Clamp n into valid range of RES to keep behavior defined for all n >= 0
    if n < 0:
        n = 0
    elif n >= len(RES):
        n = len(RES) - 1
    val = RES[n] * math.factorial(n)
    print(val % MOD)

if __name__ == "__main__":
    # Example deterministic call; adjust n to scale the "input size"
    main(10)