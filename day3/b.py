with open("input.txt", "r") as file:
    lines = file.read().split("\n")
total = 0
for x in range(len(lines)//3):
    if not lines[3*x]: continue
    # find the common one
    common = set(lines[3*x]) \
        .intersection(set(lines[3*x+1])) \
        .intersection(set(lines[3*x+2])) \
        .pop()
    # get priority
    total += ord(common) - (38 if common.upper() == common else 96)

print(total)
