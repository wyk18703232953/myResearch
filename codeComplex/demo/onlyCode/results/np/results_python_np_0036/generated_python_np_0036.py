def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main(n):
    commands = "+" * (n // 2) + "-" * (n - n // 2)
    received_list = []
    fixed = min(2, n)
    for i in range(fixed):
        received_list.append(commands[i])
    for i in range(fixed, n):
        received_list.append("?")
    received = "".join(received_list)
    n_len = len(commands)
    positive = 0
    negative = 0
    count = 0
    for i in range(n_len):
        if commands[i] == "+":
            positive += 1
        else:
            negative += 1
        if received[i] == "+":
            positive -= 1
        elif received[i] == "-":
            negative -= 1
        else:
            count += 1
    cases = 2 ** count
    probability = 0.0
    if positive >= 0 and negative >= 0:
        probability = (factorial(count) / (factorial(positive) * factorial(negative))) / cases
    return float("{0:.9f}".format(probability))

if __name__ == "__main__":
    print(main(10))