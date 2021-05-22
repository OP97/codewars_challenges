snail_map = [[1,2,3,4],
             [4,5,6,7],
             [7,8,9,1],
             [1,2,3,4]]

snail_road = []
rowStart, rowEnd = 0, len(snail_map)-1
columnStart, columnEnd = 0, len(snail_map)-1


while rowStart <= rowEnd and columnStart <= columnEnd:
    for i in range(columnStart, columnEnd+1):
        snail_road.append(snail_map[rowStart][i])
    rowStart += 1

    for i in range(rowStart, rowEnd+1):
        snail_road.append(snail_map[i][columnEnd])
    columnEnd -= 1

    for i in range(columnEnd, columnStart-1, -1):
        snail_road.append(snail_map[rowEnd][i])
    rowEnd -= 1

    for i in range(rowEnd, rowStart-1, -1):
        snail_road.append(snail_map[i][columnStart])
    columnStart += 1

print(snail_road)



