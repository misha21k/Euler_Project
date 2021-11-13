"""
Maximum path sum

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.
3
7 4
2 4 6
8 5 9 3
that is, 3 + 7 + 4 + 9 = 23
Find the maximum total from top to bottom in triangle.txt ( right click and
'Save Link/Target As...', a 15 K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 2^99 altogether!
If you could check one trillion (10^12) routes every second it would take
over twenty billion years to check them all. There is an efficient algorithm
to solve it. ;o)
"""


def init(filename):
    file = open(filename)
    grid = []
    for line in file:
        row = []
        for node in line.split():
            row.append(int(node))
        if row:
            grid.append(row)
    file.close()

    triangle = {}
    costs = {}
    key = 0
    i = 0
    for row in grid[:-1]:
        for j in range(len(row)):
            triangle[key] = {key+i+1: grid[i+1][j], key+i+2: grid[i+1][j+1]}
            costs[key] = 0
            key += 1
        i += 1

    costs[0] = grid[0][0]
    for j in range(len(grid[-1])):
        triangle[key] = {}
        costs[key] = 0
        key += 1
    return triangle, costs


def find_max_cost(costs):
    max_cost = 0
    for cost in costs.values():
        if cost > max_cost:
            max_cost = cost
    return max_cost


def main():
    triangle, costs = init('triangle.txt')
    for node in range(len(costs)):
        cost = costs[node]
        neighbors = triangle[node]
        for n in neighbors:
            new_cost = cost + neighbors[n]
            if new_cost > costs[n]:
                costs[n] = new_cost
    print(find_max_cost(costs))


main()