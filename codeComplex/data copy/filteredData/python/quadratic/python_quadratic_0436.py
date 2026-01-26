def solve(n):
    from math import sqrt

    # Deterministically construct l as a list of 0/1 digits of length n
    # Pattern: l[i] = i % 2  -> "0101..." for any n
    l = [i % 2 for i in range(n)]

    divisors = []
    total = sum(l)
    for j in range(2, int(sqrt(total)) + 1):
        if total % j == 0:
            divisors.extend([j, total // j])
    if total == 0:
        # print("YES")
        pass
        return
    if total != 1:
        divisors.append(1)
    for x in divisors:
        search = x
        index = 0
        summ = 0
        while index < n:
            summ += l[index]
            if summ > search:
                break
            elif summ == search:
                summ = 0
            index += 1
        if summ == 0 and index == n:
            # print("YES")
            pass
            return
    # print("NO")
    pass


def main(n):
    solve(n)


if __name__ == "__main__":
    # Example: run with a specific n for experiment
    main(10)