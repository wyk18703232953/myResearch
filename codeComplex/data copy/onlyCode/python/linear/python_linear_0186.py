n = int(input())

number_sequence = [int(x) for x in input().split(" ")]
number_total = sum(number_sequence)

current_total = 0
current_position = 0

for number in number_sequence:
    current_total = current_total + number
    current_position = current_position + 1
    if(current_total >= number_total/2):
        print(current_position)
        break
