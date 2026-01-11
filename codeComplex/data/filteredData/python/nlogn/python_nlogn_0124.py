def main(n):
    # Deterministic data generation based on n
    # Map n to problem parameters:
    # n -> number of filters
    # m -> number of sockets needed (linear in n)
    # k -> initial sockets (periodic function of n)
    if n <= 0:
        return

    # Basic scalable parameters
    num_filters = n
    m = 2 * n + 3
    k = (n % (n + 5)) + 1  # always between 1 and n+5, deterministic

    # Generate filters deterministically: increasing capacities
    # Example: capacities range around 2..5 with simple pattern
    filters = [2 + (i % 4) for i in range(num_filters)]
    filters.sort()

    # Core algorithm logic preserved
    if k < m:
        spots = k
        end = num_filters - 1
        supply_filters_needed = 0
        while spots < m and end >= 0:
            spots += filters[end] - 1
            supply_filters_needed += 1
            end -= 1

        if spots < m:
            result = -1

        else:
            result = supply_filters_needed

    else:
        result = 0

    # Output to avoid optimization removal in experiments
    # print(result)
    pass
if __name__ == "__main__":
    main(10)