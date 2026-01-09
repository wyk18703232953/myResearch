def main(n):
    # Interpret n as candies, and set turns = n as a scalable deterministic choice
    turns = n
    candies = n

    summ = 0
    turn = 0
    # Guard against non-termination: if no solution within reasonable bounds, break
    # Here we limit turns tried to 2 * turns to keep it scalable and deterministic
    max_turn_limit = 2 * turns if turns > 0 else 1
    while candies != summ - (turns - turn) and turn < max_turn_limit:
        turn += 1
        summ += turn
    if turn >= max_turn_limit:
        result = -1  # indicate no valid turn found within limit

    else:
        result = turns - turn

    return result


if __name__ == "__main__":
    # Example deterministic call
    # print(main(10))
    pass