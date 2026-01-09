import re

def main(n):
    results = []
    for x in range(n):
        if x % 2 == 0:
            # Generate "RxCy" format
            rows = x + 1
            columns = x * 37 + 1
            coordinates = f"R{rows}C{columns}"

        else:
            # Generate "A1" style format
            rows = x + 1
            columns = x * 37 + 1
            # Convert column number to letters
            col = columns
            letters = ""
            i = 0
            while col > 0:
                alpha_index = (col // (26 ** i) - 1) % 26
                letters = chr(65 + alpha_index) + letters
                col -= (alpha_index + 1) * (26 ** i)
                i += 1
            coordinates = f"{letters}{rows}"

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
            results.append(output)

        else:
            match = re.match(r"(\D+)(\d+)", coordinates)
            letters = match.group(1)
            rows = match.group(2)
            columns = 0
            for i in range(len(letters), 0, -1):
                columns += (ord(letters[i - 1]) - 64) * (26 ** (len(letters) - i))
            output = f"R{rows}C{columns}"
            results.append(output)
    return results

if __name__ == "__main__":
    # Example scale; adjust n for experiments
    out = main(10)
    for line in out:
        # print(line)
        pass