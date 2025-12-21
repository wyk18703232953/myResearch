def main(n):
    chores = [0, 0, n - 1]
    complexity = list(range(1, n + 1))
    complexity.sort()
    return complexity[chores[2]] - complexity[chores[2] - 1]

if __name__ == "__main__":
    print(main(10))