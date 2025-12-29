import re

inputs = int(input())
# inputs是一个整数，代表坐标的数量
for x in range(inputs):
    coordinates = input()
    # coordinates是一个字符串，代表一个坐标，格式为R1C1或A1
    match = re.match("R(\d+)C(\d+)", coordinates)
    if match:
        rows = int(match.group(1))
        columns = int(match.group(2))

        output = ""
        i = 0
        while columns > 0:
            alpha_index = (columns // (26 ** i) - 1) % 26
            output = chr(65 + alpha_index) + output
            # print(columns, alpha_index)
            columns -= (alpha_index + 1) * (26 ** i)
            i += 1
        output += str(rows)
        print(output)
    else:
        match = re.match("(\D+)(\d+)", coordinates)
        letters = match.group(1)
        rows = match.group(2)
        columns = 0
        for i in range(len(letters), 0, -1):
            columns += (ord(letters[i - 1]) - 64) * (26 ** (len(letters) - i))
        output = f"R{rows}C{columns}"
        print(output)
