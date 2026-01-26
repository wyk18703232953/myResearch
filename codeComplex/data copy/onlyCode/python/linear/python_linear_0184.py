
def get_answer(arr):
    current_sum = 0
    total = sum(arr)
    for index, val in enumerate(arr):
        current_sum += val
        if current_sum >= total / 2:
            return index + 1

nonsense = input()
input_values = input()
values = [int(v) for v in input_values.split()]

print(get_answer(values))
