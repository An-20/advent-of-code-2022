with open("input.txt", "r") as file:
    lines = file.read().split("\n")
winners = {"R": "S", "P": "R", "S": "P"}
losers = {b: a for a, b in winners.items()}
score = 0
for line in lines:
    if not line: continue
    ga, gb = line.split(" ")
    ga = {"A": "R", "B": "P", "C": "S"}[ga]
    if gb == "X":
        gb = winners[ga]
    elif gb == "Y":
        gb = ga
        score += 3
    else:
        gb = losers[ga]
        score += 6
    score += "RPS".index(gb) + 1

print(score)
