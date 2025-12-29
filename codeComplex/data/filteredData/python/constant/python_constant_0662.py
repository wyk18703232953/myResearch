import random

def interactive_judge(a, b, hidden_a, hidden_b):
    """
    Simulates the judge:
    returns:
        -1 if (hidden_a ^ a) < (hidden_b ^ b)
         0 if (hidden_a ^ a) == (hidden_b ^ b)
         1 if (hidden_a ^ a) > (hidden_b ^ b)
    """
    va = hidden_a ^ a
    vb = hidden_b ^ b
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        return 0

def main(n):
    """
    n: bit-length (up to 30) used to generate hidden_a and hidden_b (0 <= value < 2^n)
    The function prints recovered a and b, and the hidden ones for verification.
    """
    if n <= 0:
        n = 1
    if n > 30:
        n = 30

    # generate test data
    max_val = (1 << n) - 1
    hidden_a = random.randint(0, max_val)
    hidden_b = random.randint(0, max_val)

    # start of converted logic (replacing the interactive part)
    # initial query
    cond = interactive_judge(0, 0, hidden_a, hidden_b)
    cur_a = 0
    cur_b = 0

    for i in range(29, -1, -1):
        xor = (1 << i)
        query_a = cur_a ^ xor
        query_b = cur_b ^ xor
        val = interactive_judge(query_a, query_b, hidden_a, hidden_b)

        if val != cond:
            if cond == -1 and val == 1:
                # flip b
                cur_b ^= xor
                query_a = cur_a
                query_b = cur_b
                val = interactive_judge(query_a, query_b, hidden_a, hidden_b)
                cond = val
            else:
                # flip a
                cur_a ^= xor
                query_a = cur_a
                query_b = cur_b
                val = interactive_judge(query_a, query_b, hidden_a, hidden_b)
                cond = val
        else:
            cond = val
            query_a = cur_a ^ xor
            query_b = cur_b
            val = interactive_judge(query_a, query_b, hidden_a, hidden_b)
            if val == -1:
                cur_a ^= xor
                cur_b ^= xor
            else:
                pass

    # output result of algorithm and the ground truth for verification
    print("Recovered a, b:", cur_a, cur_b)
    print("Hidden    a, b:", hidden_a, hidden_b)
    return cur_a, cur_b, hidden_a, hidden_b


if __name__ == "__main__":
    # example: use bit-length n = 10
    main(10)