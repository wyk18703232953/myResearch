def solve(n):
    for d in [2, 4]:
        if n % d != 0:
            continue
        temp = int((n // d) ** 0.5)
        temp -= 1
        while temp * temp < n // d:
            temp += 1
        if temp * temp == n // d:
            return "YES"
    return "NO"

def main(n):
    results = []
    for i in range(1, n + 1):
        val = i * 2
        results.append(solve(val))
    return results

if __name__ == "__main__":
    # print(main(10))
    pass