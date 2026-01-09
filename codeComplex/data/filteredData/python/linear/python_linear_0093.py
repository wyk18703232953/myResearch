def main(n):
    # Deterministically generate a string of length n over a small alphabet
    # Example pattern: repeating 'A', 'B', 'C', 'D'
    chars = ['A', 'B', 'C', 'D']
    pokemons = ''.join(chars[i % 4] for i in range(n))

    last = {}
    start_of_all = 0
    for i in range(n):
        ty = pokemons[i]
        if ty not in last:
            start_of_all = i
        last[ty] = 0

    minlen = 100001
    for i in range(n):
        ty = pokemons[i]
        last[ty] = i
        length = i + 1 - min(last.values())
        if i >= start_of_all and length < minlen:
            minlen = length

    # print(minlen)
    pass
if __name__ == "__main__":
    main(1000)