def main(n):
    # Generate deterministic test data based on n
    # n is the number of stones
    stones = [i // 2 for i in range(n)]
    stones = sorted(stones)

    if n == 0:
        return "cslnb"

    if n == 1:
        if stones[0] % 2 == 0:
            result = 'cslnb'

        else:
            result = 'sjfnb'
        # print(result)
        pass
        return result

    else:
        chilly = -1
        chill = 2
        prev = stones[0]

        for x in stones[1:]:
            if x == prev:
                chill -= 1
                chilly = x

            else:
                streak = 1
                prev = x

        s = sum(stones)

        if n % 4 == 0 or n % 4 == 1:
            s += 1

        if chill <= 0 or stones.count(0) > 1:
            result = 'cslnb'
        elif chill == 1 and chilly - 1 in stones:
            result = 'cslnb'
        elif s % 2 == 1:
            result = 'cslnb'

        else:
            result = 'sjfnb'

        # print(result)
        pass
        return result


if __name__ == "__main__":
    main(10)