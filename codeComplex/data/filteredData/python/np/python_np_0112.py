import math

def main(n):
    # Generate two deterministic strings a and b based on n
    # a will have n characters, b will have n characters
    # Pattern: positions where i % 2 == 0 -> '+', else '-'
    a = ['+' if i % 2 == 0 else '-' for i in range(n)]
    # For b, shift the pattern by 1 to create a difference but deterministically
    b = ['+' if (i + 1) % 2 == 0 else '-' for i in range(n)]

    p = a.count('+') - b.count('+')
    m = a.count('-') - b.count('-')

    if m < 0 or p < 0:
        print(0)
        return

    l = math.factorial(p + m) / (math.factorial(p) * math.factorial(m))
    print(l * (0.5 ** (p + m)))

if __name__ == "__main__":
    main(10)