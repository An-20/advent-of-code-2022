with open("input.txt", "r") as file:
    lines = file.read().split("\n")
trees = []
for line in lines:
    if not line: continue
    row = []
    for char in line:
        row.append(int(char))
    trees.append(row)


def transpose(x):
    new = []
    for _ in x[0]:
        new.append([])
    for y in x:
        for idx in range(len(y)):
            new[idx].append(y[idx])
    return new


def check_visibility(x, r=True):
    visibility = []
    for old_row in x:
        new_row = []
        tallest = -1
        for height in (old_row if r else reversed(old_row)):
            if height > tallest:
                new_row.append(True)
                tallest = height
            else:
                new_row.append(False)
        if not r:
            new_row.reverse()
        visibility.append(new_row)
    return visibility


transposed = transpose(trees)
v_top = transpose(check_visibility(transposed))
v_bottom = transpose(check_visibility(transposed, False))
v_left = check_visibility(trees)
v_right = check_visibility(trees, False)

count = 0
for x in range(len(trees)):
    for y in range(len(trees[0])):
        if v_top[x][y] or v_bottom[x][y] or v_left[x][y] or v_right[x][y]:
            count += 1
            print("X", end="")
        else:
            print("_", end="")
    print("\n")

print(count)
