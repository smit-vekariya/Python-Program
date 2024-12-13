unsort = [2, 4, 6, 1, 34, 45, 22, 2, 1]
print("Unsorted:", unsort)

loop = 0  # Counter for the number of iterations to find the minimum

for j in range(len(unsort) - 1, 0, -1):
    swap = False
    for i in range(j):
        loop += 1
        if unsort[i + 1] < unsort[i]:
            unsort[i + 1], unsort[i] = unsort[i], unsort[i + 1]
            swap = True
    if not swap:
        break

print("Sorted:", unsort)
print("Number of loops:", loop)
