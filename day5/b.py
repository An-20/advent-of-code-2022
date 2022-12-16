with open("input.txt", "r") as file:
    lines = file.read().split("\n")
split_idx = lines.index("")
arrangement = lines[:split_idx - 1]
moves = lines[split_idx + 1:]

stacks = []
for x in range(len(arrangement[0]) // 4 + 1): stacks.append([])
for row in reversed(arrangement):
    for x in range(len(row) // 4 + 1):
        if row[4*x+1] != " ":
            stacks[x].append(row[4*x+1])

for move in moves:
    if not move: continue
    mn = int(move.split(" ")[1])
    mo = int(move.split(" ")[3]) - 1
    md = int(move.split(" ")[5]) - 1
    tmp = []
    for x in range(mn):
        tmp.append(stacks[mo].pop())
    for _ in range(mn):
        stacks[md].append(tmp.pop())

print("".join(stack[-1] for stack in stacks))
