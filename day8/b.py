with open("input.txt", "r") as file:
    lines = file.read().split("\n")
trees = []
for line in lines:
    if not line: continue
    row = []
    for char in line:
        row.append(int(char))
    trees.append(row)


max_score = 0
for row_idx in range(len(trees)):
    for tree_idx in range(len(trees[0])):
        if row_idx == 0 or row_idx == len(trees) - 1:
            continue
        if tree_idx == 0 or tree_idx == len(trees[0]) - 1:
            continue

        score = 1
        height = trees[row_idx][tree_idx]
        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            distance = 0
            new_row = row_idx
            new_tree = tree_idx
            while True:
                new_row += move[0]
                new_tree += move[1]
                if (
                        not (0 <= new_row < len(trees)) or
                        not (0 <= new_tree < len(trees[0]))
                ):
                    score *= distance
                    break
                distance += 1
                if trees[new_row][new_tree] >= height:
                    score *= distance
                    break
        if score > max_score:
            max_score = score
