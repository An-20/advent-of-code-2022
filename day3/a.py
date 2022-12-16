with open("input.txt", "r") as file:
    lines = file.read().split("\n")
total = 0
for line in lines:
    if not line: continue
    # find the common one
    common = set(line[:len(line)//2]).intersection(set(line[len(line)//2:])).pop()
    # get priority
    total += ord(common) - (38 if common.upper() == common else 96)

print(total)
