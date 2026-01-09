def main(n):
    # Generate deterministic input of size n:
    # Original program expects:
    #   n: length of sequence
    #   a: list of n integers
    # We map parameter n to this n, and build a sequence a of length n.
    # Example deterministic pattern: a[i] = (i % 7) - 3
    if n <= 0:
        # print('-1')
        pass
        return

    a_list = [(i % 7) - 3 for i in range(n)]
    a = iter(a_list)

    prev_type = 3
    prev_res = 2
    try:
        curr_a = next(a)
    except StopIteration:
        # print('-1')
        pass
        return

    res = []
    for _ in range(1):
        for next_a in a:
            if next_a > curr_a:
                if prev_type == 1 or prev_res == 1:
                    prev_res += 1
                    if prev_res == 5:
                        break

                else:
                    prev_res = 1
                prev_type = 1
            elif next_a < curr_a:
                if prev_type == 2 or prev_res == 5:
                    prev_res -= 1
                    if prev_res == 1:
                        break

                else:
                    prev_res = 5
                prev_type = 2

            else:
                if prev_type == 1:
                    prev_res += 1
                elif prev_type == 2:
                    prev_res -= 1
                elif prev_res != 2:
                    prev_res = 2

                else:
                    prev_res = 3
                prev_type = 3
            res.append(prev_res)
            curr_a = next_a

        else:
            if prev_type == 1:
                res.append(prev_res + 1)
            elif prev_type == 2:
                res.append(prev_res - 1)
            elif prev_res != 1:
                res.append(1)

            else:
                res.append(2)
            # print(*res)
            pass
            break

    else:
        # print('-1')
        pass
if __name__ == "__main__":
    # Example deterministic call for complexity experiments
    main(10)