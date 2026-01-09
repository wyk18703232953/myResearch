import sys

def transform_string(s):
    from collections import Counter
    d = Counter(s)
    if '1' in d:
        news = ""
        for ch in s:
            if ch != '1':
                news += ch
        ind = len(news)
        for i in range(len(news)):
            if news[i] == '2':
                ind = i
                break
        ans = news[0:ind] + '1' * d['1'] + news[ind:]
        return ans

    else:
        return s

def generate_input_string(n):
    if n <= 0:
        return ""
    chunks = []
    for i in range(n):
        r = i % 3
        if r == 0:
            chunks.append('1')
        elif r == 1:
            chunks.append('2')

        else:
            chunks.append('3')
    return "".join(chunks)

def main(n):
    s = generate_input_string(n)
    result = transform_string(s)
    sys.stdout.write(result + "\n")

if __name__ == "__main__":
    main(1000)