def main(n):
    # Generate deterministic input: game list of length n
    # Example: game[i] = i // 2 to allow duplicates and variety
    game = [i // 2 for i in range(n)]

    game.append(-1)
    game.sort()
    bitSum = game[1] % 2
    rep = False
    for i in range(1, n):
        bitSum += game[i + 1] % 2
        if game[i] == game[i + 1]:
            if rep:
                return 'cslnb'
            else:
                if game[i - 1] == game[i] - 1:
                    return 'cslnb'
                rep = True
    Goal = ((n * (n - 1)) / 2) % 2
    if (bitSum + Goal) % 2 == 0:
        return 'cslnb'
    else:
        return 'sjfnb'


if __name__ == "__main__":
    # Example deterministic call
    result = main(10)
    print(result)