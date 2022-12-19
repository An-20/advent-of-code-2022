with open("input.txt", "r") as file:
    lines = file.read().split("\n")


def g(r, x):
    if not x: return r
    elif len(x) == 1: return r[x[0]]
    else: return g(r[x[0]], x[1:])


def s(r, x, v):
    if len(x) == 1: r[x[0]] = v
    else: s(r[x[0]], x[1:], v)


root = {}
stack = []

for line in lines[1:]:
    if not line: continue
    if line[:4] == "$ cd":
        if ".." in line:
            stack.pop()
        else:
            stack.append(line[5:].strip())
    elif line[:4] == "$ ls":
        pass
    elif line[:3] == "dir":
        stack.append(line[4:].strip())
        s(root, stack, {})
        stack.pop()
    else:
        size, filename = line.split(" ")
        g(root, stack)[filename] = int(size)


candidates = []


def getsize(x):
    if isinstance(x, int):
        return x
    else:
        s = sum(getsize(x[y]) for y in x)
        candidates.append(s)
        return s


space_needed = 30000000 - (70000000 - getsize(root))
candidates = [x for x in candidates if x >= space_needed]
print(sorted(candidates)[0])
