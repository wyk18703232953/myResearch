def check(a, b):
    if a[1] == b[1] and 1 <= abs(int(b[0]) - int(a[0])) <= 2:
        return True
    return False

def core_logic(arr):
    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
    mineq = 3 - max(d.values())
    arr.sort(key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])
    if check(arr[0], arr[1]) or check(arr[1], arr[2]):
        mineq = min(mineq, 1)
    if (
        arr[0][1] == arr[1][1] == arr[2][1]
        and int(arr[2][0]) - int(arr[1][0]) == 1
        and int(arr[1][0]) - int(arr[0][0]) == 1
    ):
        mineq = 0
    return mineq

def generate_input(n):
    # Deterministically generate 3 strings shaped like the original input tiles.
    # Each string is "valueSUIT", where:
    # - value is between 1 and max(3, n) (as decimal string, without padding)
    # - SUIT is chosen deterministically from 'a', 'b', 'c' by index
    # This keeps structure similar to the original, while scaling with n.
    max_val = max(3, n)
    suits = ['a', 'b', 'c']
    arr = []
    for i in range(3):
        val = (i * n + 1) % max_val
        if val == 0:
            val = max_val
        s = suits[i % 3]
        arr.append(str(val) + s)
    return arr

def main(n):
    arr = generate_input(n)
    result = core_logic(arr)
    print(result)

if __name__ == "__main__":
    main(10)