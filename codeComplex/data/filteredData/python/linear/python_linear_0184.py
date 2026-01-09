def get_answer(arr):
    current_sum = 0
    total = sum(arr)
    for index, val in enumerate(arr):
        current_sum += val
        if current_sum >= total / 2:
            return index + 1

def main(n):
    if n <= 0:
        return
    values = [i % 10 + 1 for i in range(1, n + 1)]
    ans = get_answer(values)
    # print(ans)
    pass
if __name__ == "__main__":
    main(10)