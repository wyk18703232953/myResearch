def main(n):
    # Interpret n as the total number of moves
    no_of_moves = max(0, n)

    # Deterministically generate the target candy count based on n
    # Example: total candies after collecting 1+2+...+no_of_moves
    no_of_candy = no_of_moves * (no_of_moves + 1) // 2

    total_candy = 1
    now_candy = 1
    now_moves = 1

    if no_of_moves == 0 or (no_of_moves == 1 and no_of_candy == 1):
        result = 0
    else:
        while True:
            now_candy = now_candy + 1
            total_candy += now_candy
            now_moves += 1
            if total_candy - (no_of_moves - now_moves) == no_of_candy:
                break
        result = no_of_moves - now_moves

    print(result)
    return result


if __name__ == "__main__":
    # Example deterministic call
    main(10)