with open("input.txt", "r") as file:
    line = file.read()
for idx in range(4, len(line)):
    if len(set(line[idx-4:idx])) == 4:
        print(idx)
        break
