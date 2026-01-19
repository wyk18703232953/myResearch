from itertools import combinations

def main(n):
    # Interpret n as the number of elements in arr
    if n < 2:
        print(0)
        return

    num = n
    # Deterministic generation of arr based on n
    # Example: arr = [1, 2, 3, ..., n]
    arr = [i + 1 for i in range(num)]

    # Deterministic thresholds derived from n
    min_dif = n
    max_dif = 3 * n
    easy_hard_dif = 2

    all_combinations = []
    for x in range(2, num + 1):
        combs = combinations(arr, x)
        for abc in combs:
            all_combinations.append(list(abc))

    possible_answers = 0
    for a in all_combinations:
        s = sum(a)
        if min_dif <= s <= max_dif and (max(a) - min(a)) >= easy_hard_dif:
            possible_answers += 1

    print(possible_answers)

if __name__ == "__main__":
    main(10)