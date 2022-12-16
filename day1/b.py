with open("input.txt", "r") as file:
    lines = file.read().split("\n")
nums = []
total = 0
for line in lines:
    if line == "":
        nums.append(total)
        total = 0
    else:
        total += int(line)

print(sum(sorted(nums)[-3:]))
