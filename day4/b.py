with open("input.txt", "r") as file:
    lines = file.read().split("\n")
total = 0
for line in lines:
    if not line: continue
    ra, rb = line.split(",")
    a1, a2 = (int(x) for x in ra.split("-"))
    b1, b2 = (int(x) for x in rb.split("-"))
    if (a1 <= b1 <= a2) or (a2 >= b2 >= a1) or (b1 <= a1 <= b2) or (b2 >= a2 >= b1):
        total += 1
print(total)
