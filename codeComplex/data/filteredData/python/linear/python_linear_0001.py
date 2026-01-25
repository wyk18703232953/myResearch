import re

def generate_coordinates(n):
    coords = []
    for i in range(1, n + 1):
        if i % 2 == 1:
            # RC 型：R{row}C{col}
            row = i
            col = i * 3 + 5
            coords.append(f"R{row}C{col}")
        else:
            # 字母+行 型：{letters}{row}
            row = i
            letters = ""
            col = i * 3 + 5
            c = col
            while c > 0:
                c -= 1
                letters = chr(65 + (c % 26)) + letters
                c //= 26
            coords.append(f"{letters}{row}")
    return coords

def main(n):
    coordinates_list = generate_coordinates(n)
    for coordinates in coordinates_list:
        match = re.match(r"R(\d+)C(\d+)", coordinates)
        if match:
            rows = int(match.group(1))
            columns = int(match.group(2))
            output = ""
            i = 0
            while columns > 0:
                alpha_index = (columns // (26 ** i) - 1) % 26
                output = chr(65 + alpha_index) + output
                columns -= (alpha_index + 1) * (26 ** i)
                i += 1
            output += str(rows)
            print(output)
        else:
            match = re.match(r"(\D+)(\d+)", coordinates)
            letters = match.group(1)
            rows = match.group(2)
            columns = 0
            for i in range(len(letters), 0, -1):
                columns += (ord(letters[i - 1]) - 64) * (26 ** (len(letters) - i))
            output = f"R{rows}C{columns}"
            print(output)

if __name__ == "__main__":
    main(10)