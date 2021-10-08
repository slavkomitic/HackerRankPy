def matrixRotation(matrix, r):
    """

    @https://www.hackerrank.com/challenges/matrix-rotation-algo/problem
    """

    def _print_matrix(m):
        for r in range(rows):
            for c in range(columns):
                print(m[r][c], end=" ")
            print()

    rows = len(matrix)
    columns = len(matrix[0])
    layers = min(rows, columns) // 2

    circle = []
    layers_data = dict()
    m = []
    for i in range(layers):
        circle = []
        circle += matrix[i][i:columns-i]
        circle += [matrix[k][-1-i] for k in range(i+1, rows-1-i)]
        circle += matrix[-1-i][i:columns-i][::-1]
        circle += [matrix[k][i] for k in range(rows-2-i, i, -1)]

        [m.append((i, point)) for pos, point in enumerate(circle)]

        filtered = list(filter(lambda x: x[0] == i, m))
        cycle = r % len(filtered)

        filtered = filtered[cycle:] + filtered[:cycle]
        layers_data[i] = filtered

    mtrx = [["*" for c in range(columns)] for r in range(rows)]

    results = []
    for k, v in layers_data.items():
        x = 0 + k
        [results.append((x, y, v.pop(0)[1])) for y in range(k, columns-k)]
        y = columns - 1 - k
        [results.append((x, y, v.pop(0)[1])) for x in range(1+k, rows-1-k)]
        x = rows - 1 - k
        [results.append((x, y, v.pop(0)[1])) for y in range(columns-1-k, 0+k, -1)]
        y = 0 + k
        [results.append((x, y, v.pop(0)[1])) for x in range(rows-1-k, 0+k, -1)]

    for i, r in enumerate(results):
        mtrx[r[0]][r[1]] = r[2]

    _print_matrix(mtrx)


if __name__ == "__main__":

    m = [[1, 2, 3, 4],
         [7, 8, 9, 10],
         [13, 14, 15, 16],
         [19, 20, 21, 22],
         [25, 26, 27, 28]]

    r = 7

    matrixRotation(m, r)
    print()
    #matrixRotation(m, 5)
    print()
    #matrixRotation(m, 14)
