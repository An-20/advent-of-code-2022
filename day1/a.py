with open("input.txt", "r") as file:
    lines = file.read().split("\n")
largest = 0
total = 0
for line in lines:
    if line == "":
        if total > largest:
            largest = total
        total = 0
    else:
        total += int(line)

print(largest)
