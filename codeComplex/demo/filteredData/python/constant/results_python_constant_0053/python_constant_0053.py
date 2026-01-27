import itertools

def generate_47_arr():
    arr = []
    for digits in range(1, 4):
        arr += itertools.product("47", repeat=digits)
    for i in range(len(arr)):
        arr[i] = int("".join(list(arr[i])))
    arr.append(4444444444)
    return arr

def q121a_v2(num):
    good_num_arr = generate_47_arr()
    for element in good_num_arr:
        if num % element == 0:
            return "YES"
    return "NO"

def main(n):
    num = n
    result = q121a_v2(num)
    # print(result)
    pass
if __name__ == "__main__":
    main(1000000000)