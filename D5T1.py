def draw(coordinates, new_line):
    x1 = new_line[0][0]
    x2 = new_line[1][0]
    y1 = new_line[0][1]
    y2 = new_line[1][1]
    if x1 == x2: #same line
        for j in range(min(y1, y2), max(y1, y2) +1):
            coordinates[x1][j] = coordinates[x1][j] + 1
    elif y1 == y2: #same column
        for k in range(min(x1, x2), max(x1, x2) +1):
            coordinates[k][y1] = coordinates[k][y1] + 1
    else:
        if x1 > x2:
            if y1 > y2:
                for i in range(x2, x1+1):
                    if y2 == y1 + 1:
                        break
                    coordinates[i][y2] = coordinates[i][y2] + 1
                    y2 = y2 + 1
            else:
                for i in range(x2, x1+1):
                    if y2 == y1 - 1:
                        break
                    coordinates[i][y2] = coordinates[i][y2] + 1
                    y2 = y2 - 1
        else:
            if y1 > y2:
                for i in range(x1, x2+1):
                    if y1 == y2 - 1:
                        break
                    coordinates[i][y1] = coordinates[i][y1] + 1
                    y1 = y1 - 1
            else:
                for i in range(x1, x2+1):
                    if y1 == y2 + 1:
                        break
                    coordinates[i][y1] = coordinates[i][y1] + 1
                    y1 = y1 + 1
    return coordinates


def main():
    with open("inputD5T1.txt", "r") as f:
        lines = f.readlines()
    #lets create the numbers properly
    onlyNumbers = [row.split("\n")[0] for row in lines]
    start_ends = [row.split("->") for row in onlyNumbers]
    helper = [group.split(",") for case in start_ends for group in case]
    helper2 = [list(map(int, row)) for row in helper]
    line_coordinates = [helper2[n:n + 2] for n in range(0, len(helper2), 2)]

    #create the coordinate map
    coordinates = []
    for i in range(0,999):
        row = [0] * 999
        coordinates.append(row)

    for j, line in enumerate(line_coordinates):
        coordinates = draw(coordinates, line)

    #print(coordinates)
    flat_coordinates = list(item for sublist in coordinates for item in sublist)

    c = 0
    for i, co in enumerate(flat_coordinates):
        if co > 1:
            c = c + 1
    print(c)





if __name__ == "__main__":
    main()