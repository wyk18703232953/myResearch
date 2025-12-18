"""
$ pylint calderonsin.py
Global evaluation
-----------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

"""
def maxlen():
    string = input()
    maxi = 0;
    for x in range(len(string)):
        substring = ""
        for y in string[x:]:
            substring +=y;
            if string[x:].rfind(substring) != string[x:].find(substring):
                maxi = max(maxi, len(substring))
                continue
    print(maxi)

maxlen()
# $ python3 calderonsin.py build
# remember the output
