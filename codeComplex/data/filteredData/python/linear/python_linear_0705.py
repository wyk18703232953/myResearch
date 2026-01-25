n_global = 0

def generate_input(n):
    # n is the length of the string s
    # generate a deterministic pattern of '-' and '+' based on index
    s = ''.join('-' if i % 2 == 0 else '+' for i in range(n))
    return n, s

def core_logic(n, s):
    cur = 0
    for a in s:
        cur = max(cur, 0)
        if a == '-':
            cur -= 1
        else:
            cur += 1
        cur = max(cur, 0)
    return cur

def main(n):
    global n_global
    n_global = n
    n_input, s = generate_input(n)
    result = core_logic(n_input, s)
    print(result)

if __name__ == "__main__":
    main(10)