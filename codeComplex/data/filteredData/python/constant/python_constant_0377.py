def main(n):
    # Deterministic data generation based on n
    mecces = n
    burgerKing = n // 2
    both = n // 3
    groupSize = n * 2

    mecces -= both
    burgerKing -= both
    notPassed = groupSize - sum((mecces, burgerKing, both))
    if notPassed > 0 and burgerKing >= 0 and mecces >= 0:
        # print(notPassed)
        pass

    else:
        # print(-1)
        pass
if __name__ == "__main__":
    main(10)