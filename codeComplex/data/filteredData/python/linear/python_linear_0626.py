def main(n):
    # n controls the number of positions in the line (houses and riders combined)
    # We will generate:
    # - num_riders: about n // 3 riders
    # - positions: 1..n as house positions
    # - is_rider: deterministic pattern, roughly every 3rd position is a rider
    num_positions = max(1, n)
    positions = list(range(1, num_positions + 1))
    is_rider_list = [(1 if (i % 3 == 0) else 0) for i in range(1, num_positions + 1)]
    num_riders = sum(is_rider_list)
    _ = 0  # placeholder for unused second value in the original input

    houses = iter(positions)
    is_rider_iter = iter(is_rider_list)

    current_left_driver = None
    current_citizens = []
    result = []

    for house, is_rider in zip(houses, is_rider_iter):
        if is_rider:
            if current_left_driver is None:
                result.append(len(current_citizens))

            else:
                result.append(0)
                for citizen in current_citizens:
                    if abs(citizen - current_left_driver) <= abs(citizen - house):
                        result[-2] += 1

                    else:
                        result[-1] += 1

            current_citizens = []
            current_left_driver = house

        else:
            current_citizens.append(house)

    if result:
        result[-1] += len(current_citizens)

    else:
        # No riders at all: in the original logic, result would never be created,
        # but to keep a deterministic output, we can output a single number.
        result = [len(current_citizens)]

    # print(' '.join(map(str, result)))
    pass
    return num_riders, result


if __name__ == "__main__":
    # Example deterministic call; adjust n to scale input size
    main(10)