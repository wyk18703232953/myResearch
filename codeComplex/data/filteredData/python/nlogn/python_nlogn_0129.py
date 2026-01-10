def main(n):
    # Deterministic data generation based on n
    # Interpret n as number of available flash drives
    # m: total required memory, k: initial memory
    # f: capacities of n flash drives
    
    # Example deterministic mapping:
    # m grows roughly as n^2, k grows as n, f[i] around i+1
    m = n * n + n  # total required memory
    k = n          # initial memory
    
    # Generate n flash drive capacities deterministically
    f = [(i % 5 + 1) * (i // 3 + 1) for i in range(1, n + 1)]
    
    f.sort()
    
    fs = 0
    ptr = len(f) - 1
    while ptr >= 0:
        if m <= k:
            print(fs)
            return
        k -= 1
        k += f[ptr]
        fs += 1
        ptr -= 1
    
    if m <= k:
        print(fs)
    else:
        print(-1)


if __name__ == "__main__":
    # Example: run with a chosen scale n
    main(1000)