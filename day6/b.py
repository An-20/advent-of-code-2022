with open("input.txt", "r") as file:
    line = file.read()
for idx in range(14, len(line)):
    if len(set(line[idx-14:idx])) == 14:
        print(idx)
        break
