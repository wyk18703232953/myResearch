def main(n):
    # Deterministically generate two lowercase strings first and last based on n
    # Ensure they are non-empty
    first = ''.join(chr(ord('a') + (i % 26)) for i in range(max(1, n)))
    last = ''.join(chr(ord('z') - (i % 26)) for i in range(max(1, (n % 5) + 1)))

    username = first[0]
    first = first[1:]
    while first != "" and first[0] < last[0]:
        username = username + first[0]
        first = first[1:]
    result = username + last[0]
    # print(result)
    pass
    return result

if __name__ == "__main__":
    main(10)