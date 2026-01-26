def size_of_group(i):
    return long(9 * 10**(i - 1)) * i

def find_group(k, i = 1):
    diff = long(k - (size_of_group(i)))
    if diff <= 0:
        return k, i
    return find_group(diff, i + 1)

def get_number(k, g):
    return str(long(10**(g - 1)) + k / g)[k % g]

def get_sequence_number(num):
    """https://codeforces.com/problemset/problem/1177/B"""
    k_prim, g_prim = find_group(num)
    return get_number(k_prim - 1, g_prim)

# run program
if __name__ == "__main__":
    print(get_sequence_number(long(input())))