# 1029A

n, k = [int(num) for num in input().split(' ')]
string = input()


def fn(string, k):
    maximum_match = 0
    for i in range(1, len(string)):
        if string[:i] == string[-i:]:
            maximum_match = i

    answer = list(string)
    extra = list(string[maximum_match:])
    for i in range(k-1):
        answer.extend(extra)

    return ''.join(answer)


print(fn(string, k))
