import random
import time

# Generate some data
data = random.sample(range(1, 100), 16)
print(f"Data: {data}")

# Put the data in a 4x4 grid
grid = []
i = 0
for r in range(4):
    row = []
    for c in range(4):
        row.append(data[i])
        i += 1
    grid.append(row)

# Do some really complex calculations...
print("Working...")
time.sleep(5)

# Display the grid
print("Grid:")
for row in grid:
    print('\t'.join([str(i) for i in row]))
