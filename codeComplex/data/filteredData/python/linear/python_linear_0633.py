def main(n):
    # Interpret n as the number of test cases
    t = n

    # Deterministically generate test cases from n
    # For test case i (1-based):
    #   n_i = i + 1  (so it starts from 2)
    #   k_i = (i * 3) % 50 + 1  (values between 1 and 50)
    results = []
    for i in range(1, t + 1):
        ni = i + 1
        ki = (i * 3) % 50 + 1

        if ni == 1:
            ans = 'YES 0' if ki == 1 else 'NO'
        elif ni == 2:
            if ki <= 2:
                ans = 'YES 1'
            elif ki == 3 or ki > 5:
                ans = 'NO'

            else:
                ans = 'YES 0'
        elif ni <= 32 and ki > (4 ** ni - 1) // 3:
            ans = 'NO'

        else:
            c, x = 0, ni
            p2 = 2
            while x > 0:
                if c + p2 - 1 > ki:
                    break
                c += p2 - 1
                x -= 1
                p2 *= 2
            ans = 'YES %d' % (x,)

        results.append(ans)

    # For experimental use, we return the list of answers
    return results


if __name__ == "__main__":
    # Example deterministic run
    res = main(10)
    for line in res:
        # print(line)
        pass