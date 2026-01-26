def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

commands = input().strip()
received = input().strip()
n = len(commands)
positive = 0
negative = 0
count = 0
for i in range(n):
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
cases = 2**count
probability = 0.0
if positive >= 0 and negative >= 0:
    probability = (factorial(count)/(factorial(positive)*factorial(negative)))/cases

print("{0:.9f}".format(probability))