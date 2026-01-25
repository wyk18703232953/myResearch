def main(n):
    # n controls the number of positions (houses); must be at least 2
    if n < 2:
        n = 2

    # Generate a fixed, deterministic input structure:
    # - positions: strictly increasing house indices
    # - is_rider: alternating pattern of rider/citizen with riders at even indices
    num_riders = (n + 1) // 2  # riders at positions 0,2,4,...

    houses = [i * 2 for i in range(n)]
    is_rider_list = [1 if i % 2 == 0 else 0 for i in range(n)]

    current_left_driver = None
    current_citizens = []
    result = []

    for house, is_rider in zip(houses, is_rider_list):
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
        # Edge case: if somehow no riders, all are citizens counted once
        result = [len(current_citizens)]

    print(' '.join(map(str, result)))


if __name__ == "__main__":
    main(10)