def main(n):
    values = list(range(1, n + 1))
    if n >= 3:
        values[0], values[1] = values[1], values[0]
    wrong = 0
    sorted_values = list(sorted(values))
    for i in range(n):
        if values[i] != sorted_values[i]:
            wrong += 1
    if wrong > 2:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    print(main(5))