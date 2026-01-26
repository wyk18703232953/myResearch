def size_of_group(i):
    return long(9 * 10**(i - 1)) * i

def find_group_data(k, i = 1):
    diff = long(k - (size_of_group(i)))
    if diff <= 0:
        return k, i
    return find_group_data(diff, i + 1)

def get_sequence_number(num):
    """https://codeforces.com/problemset/problem/1177/B"""
    k, g = find_group_data(num)
    return str(long(10**(g - 1)) + (k - 1) / g)[(k - 1) % g]

# run program
if __name__ == "__main__":
    print(get_sequence_number(long(input())))