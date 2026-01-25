import sys
import math

mod = 1000000007

def nospace(l):
    ans = ''.join(str(i) for i in l)
    return ans

def generate_input_array(n):
    if n <= 0:
        return []
    # Deterministic construction: mix of small and medium values with repeats
    # Ensure array length is exactly n and all elements > 0
    a = [(i % 10) + 1 for i in range(1, n + 1)]
    return a

def core_algorithm(a):
    a.sort()
    n = len(a)
    i = 0
    ans = 0
    while i < len(a):
        if a[i]:
            ans += 1
            j = i + 1
            while j < n:
                if a[j] % a[i] == 0:
                    a[j] = 0
                j += 1
        i += 1
    return ans

def main(n):
    a = generate_input_array(n)
    result = core_algorithm(a)
    print(result)

if __name__ == "__main__":
    main(10)