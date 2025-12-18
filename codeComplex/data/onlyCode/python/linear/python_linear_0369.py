import re
def main():

    total_games, total_notes = map(int, input().split())
    games = [int(i) for i in input().split()]
    notes = [int(i) for i in input().split()]
    note = 0
    for game in games:
        if notes[note] >= game:
            note += 1
        if note == total_notes:
            break
    print(note)



main()