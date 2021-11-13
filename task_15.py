"""
Lattice paths

Starting in the top left corner of a 2 x 2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?
"""

n = 20
grid = [[0 for j in range(n + 1)] for i in range(n + 1)]
grid[0][0] = 1  # point has one route

# i x j grid has number of routes in i - 1 x j grid and number of routes in i x j - 1
for i in range(n + 1):
    for j in range(n + 1):
        if i != 0 or j != 0:
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

print(grid[-1][-1])
