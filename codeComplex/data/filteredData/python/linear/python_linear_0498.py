def main(n):
    # n: length of the sequence a
    if n <= 0:
        # print('-1')
        pass
        return

    # Deterministic construction of input sequence:
    # First element fixed, others follow a simple pattern depending on index.
    # This keeps behavior scalable and fully deterministic.
    a_list = [0] * n
    a_list[0] = 5
    for i in range(1, n):
        if i % 3 == 1:
            a_list[i] = a_list[i - 1] + 1
        elif i % 3 == 2:
            a_list[i] = a_list[i - 1] - 2

        else:
            a_list[i] = a_list[i - 1]

    a = iter(a_list)
    prev_type = 3
    prev_res = 2
    curr_a = next(a)
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
    main(10)