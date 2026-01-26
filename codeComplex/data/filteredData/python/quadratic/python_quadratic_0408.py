def fn(string, k):
    maximum_match = 0
    for i in range(1, len(string)):
        if string[:i] == string[-i:]:
            maximum_match = i

    answer = list(string)
    extra = list(string[maximum_match:])
    for _ in range(k - 1):
        answer.extend(extra)

    return ''.join(answer)


def main(n):
    if n < 1:
        n = 1
    k = n
    string = ''.join(chr(ord('a') + (i % 26)) for i in range(n))
    result = fn(string, k)
    # print(result)
    pass
if __name__ == "__main__":
    main(5)