with open("input.txt", "r") as file:
    lines = file.read().split("\n")
winners = {"R": "S", "P": "R", "S": "P"}
score = 0
for line in lines:
    if not line: continue
    ga, gb = line.split(" ")
    ga = {"A": "R", "B": "P", "C": "S"}[ga]
    gb = {"X": "R", "Y": "P", "Z": "S"}[gb]
    if winners[gb] == ga:
        score += 6
    elif winners[ga] != gb:
        score += 3
    score += "RPS".index(gb) + 1

print(score)
