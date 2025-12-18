#!/usr/bin/python3

import sys
import argparse
import json

def main():
    n = int(sys.stdin.readline())
    ticket = sys.stdin.readline().rstrip()
    integers = [int(x) for x in ticket]

    zeros = 0
    while zeros < len(integers) and integers[-1*(zeros+1)] == 0:
        zeros += 1

    if zeros > 0 and zeros >= len(integers):
        integers = []
    elif zeros > 0:
        integers = integers[:-1*zeros]
    #print(integers)
    if not integers:
        print("YES")
        return
    if len(integers) == 1:
        print("NO")
        return

    total = 0
    for i, val in enumerate(integers[:-1]):
        total += val
        splice = integers[i+1:]
        if is_golden(total, splice):
            print("YES")
            return
    print("NO")

def is_golden(total, integers):
    current_total = 0

    for i, val in enumerate(integers):
        current_total += val
        if current_total < total:
            continue
        elif current_total == total:
            #print("Here: %s,%s (%s)" % (total, val, integers[i+1:]))
            splice = integers[i+1:]
            return (not splice) or is_golden(total, splice)
        elif current_total > total:
            return False
    return False

def get_tests():
    tests = [("5\n73452", "YES"),
             ("4\n1248", "NO"),
             ("4\n7435", "NO"),
             ("8\n0020200", "YES"),
             ("99\n999999999999999999999999999999999999999999999918888888888888888888888888888888888888888888888888887", "YES"),
             ("84\n123608423980567916563149282633127550576921328162851174479585123236498689270768303090", "YES"),
             ("2\n00", "YES"),
             ("8\n00020200", "YES"),
             ("5\n11980", "NO"),
             ("3\n100", "NO")]

    for test in tests:
        print(json.dumps({"input": test[0], "output": test[1]}))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--get-tests", action="store_true")
    args = parser.parse_args()

    if args.get_tests:
        get_tests()
    else:
        main()
