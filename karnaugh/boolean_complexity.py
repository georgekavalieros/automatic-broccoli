import sys


#
# find the right, left, down and up element value and position.
#
def right(array, i, j):
    try:
        return array[i][j + 1], i,  j + 1
    except IndexError:
        return array[i][0], i, 0


def left(array, i, j):
    if j == 0:
        return array[i][len(array[j])-1], i, len(array[j]) - 1
    else:
        return array[i][j - 1], i, j - 1


def down(array, i, j):
    try:
        return array[i+1][j], i + 1, j
    except IndexError:
        return array[0][j], 0, j


def up(array, i, j):
    if i == 0:
        return array[len(array[i])-1][j], len(array[i])-1, j
    else:
        return array[i-1][j], i - 1, j


# Search up to 1 bottom and 4 right elements.
def find_right_neighbors(array, i, j):
    elements = []
    elements2 = []

    # 1 element
    if array[i][j] == 1:
        elements.append((i, j))

        d = down(array, i, j)
        r = right(array, i, j)

        # right
        if r[0] == 1:
            elements.append((r[1], r[2]))

            # 4 elements in a row
            r2 = right(array, r[1], r[2])
            r3 = right(array, r2[1], r2[2])
            if r2[0] == 1 and r3[0] == 1:
                elements2 = list(elements)
                elements2.append((r2[1], r2[2]))
                elements2.append((r3[1], r3[2]))

            # 2 elements
            if d[0] == 1:
                d1 = right(array, d[1], d[2])

                # 4 elements
                if d1[0] == 1:
                    elements.append((d[1], d[2]))
                    elements.append((d1[1], d1[2]))

                    # 8 elements
                    d2 = right(array, d1[1], d1[2])
                    d3 = right(array, d2[1], d2[2])

                    if r2[0] == 1 and r3[0] == 1 and d2[0] == 1 and d3[0] == 1:
                        elements.append((d2[1], d2[2]))
                        elements.append((d3[1], d3[2]))
                        elements.append((r2[1], r2[2]))
                        elements.append((r3[1], r3[2]))

        return elements, elements2


# Search up to 1 right and 4 bottom elements.
def find_down_neighbors(array, i, j):
    elements = []
    elements2 = []

    # 1 element
    if array[i][j] == 1:
        elements.append( (i, j) )

        r = right( array, i, j )
        d = down( array, i, j )

        # right
        if d[0] == 1:
            elements.append( (d[1], d[2]) )

            # 4 elements in a column
            d2 = down( array, d[1], d[2] )
            d3 = down( array, d2[1], d2[2] )
            if d2[0] == 1 and d3[0] == 1:
                elements2 = list( elements )
                elements2.append( (d2[1], d2[2]) )
                elements2.append( (d3[1], d3[2]) )

            # 2 elements
            if r[0] == 1:
                r1 = down( array, r[1], r[2] )

                # 4 elements
                if r1[0] == 1:
                    elements.append( (r[1], r[2]) )
                    elements.append( (r1[1], r1[2]) )

                    # 8 elements
                    r2 = down( array, r1[1], r1[2] )
                    r3 = down( array, r2[1], r2[2] )

                    if d2[0] == 1 and d3[0] == 1 and r2[0] == 1 and r3[0] == 1:
                        elements.append( (r2[1], r2[2]) )
                        elements.append( (r3[1], r3[2]) )
                        elements.append( (d2[1], d2[2]) )
                        elements.append( (d3[1], d3[2]) )

        return elements, elements2


# Main
if len(sys.argv) == 1:
    print("Expected more arguments.")
    exit(0)

args = list()

for i in range(1, len(sys.argv)):
    args.append(sys.argv[i])

# relate the basic terms(letters) to their representative neighborhoods.
array = {'A': ((0, 2), (1, 2), (2, 2), (3, 2), (0, 3), (1, 3), (2, 3), (3, 3)),
         '~A': ((0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1)),
         'B': ((0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2), (3, 2)),
         '~B': ((0, 0), (1, 0), (2, 0), (3, 0), (0, 3), (1, 3), (2, 3), (3, 3)),
         'C': ((2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)),
         '~C': ((0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3)),
         'D': ((1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)),
         '~D': ((0, 0), (0, 1), (0, 2), (0, 3), (3, 0), (3, 1), (3, 2), (3, 3))}

# Initialize karnaugh map.
karnaugh = [[0 for i in range(4)] for j in range(4)]
for i in args:
    row = int(i)//4
    karnaugh[row][int(i) % 4] = 1

all_sets = []
lstr = []
lstd = []

temp = 1
res = 1
for k in range(4):
    for l in range(4):
        res *= karnaugh[k][l]*temp
        temp = karnaugh[k][l]

if res == 1:
    print(res)
    exit(0)

# find all neighborhoods.
for k in range(4):
    for l in range(4):
        if find_right_neighbors(karnaugh, k, l):
            for neighbors in find_right_neighbors(karnaugh, k, l):
                if not all(x in lstr for x in neighbors):
                    all_sets.append(neighbors)
                    lstr = neighbors

        if find_down_neighbors(karnaugh, k, l):
            for neighbors in find_down_neighbors(karnaugh, k, l):
                if not all(x in lstd for x in neighbors):
                    all_sets.append(neighbors)
                    lstd = neighbors

_8neighborhoods = list()
_4neighborhoods = list()
_2neighborhoods = list()
_1neighborhoods = list()
_all_neighborhoods = list()

# remove duplicates from right and bottom search.
all_sets = map(tuple, [sorted(i) for i in all_sets])
all_sets = list(set(all_sets))
for x in all_sets:
    if len(x) == 8:
        _8neighborhoods.append(x)
    elif len(x) == 4:
        _4neighborhoods.append(x)
    elif len(x) == 2:
        _2neighborhoods.append(x)
    elif len(x) == 1:
        _1neighborhoods.append(x)

#
# remove overlapped neighborhoods
# append the rest to _all_neighborhoods.
#
for x in _8neighborhoods:
    _all_neighborhoods.append(x)

for y in _4neighborhoods:
    count = 0
    if _all_neighborhoods:
        for x in _all_neighborhoods:
            if not all(i in x for i in y):
                count += 1
        if count == len(_all_neighborhoods):
            _all_neighborhoods.append(y)
    else:
        _all_neighborhoods.append(y)

for y in _2neighborhoods:
    count = 0
    if _all_neighborhoods:
        for x in _all_neighborhoods:
            if not all(i in x for i in y):
                count += 1
        if count == len(_all_neighborhoods):
            _all_neighborhoods.append(y)
    else:
        _all_neighborhoods.append(y)

for y in _1neighborhoods:
    count = 0
    if _all_neighborhoods:
        for x in _all_neighborhoods:
            if not all(i in x for i in y):
                count += 1
        if count == len(_all_neighborhoods):
            _all_neighborhoods.append(y)
    else:
        _all_neighborhoods.append(y)


# create and output the final expression.
result = ""
counter = 0
for neighborhood in _all_neighborhoods:
    for key, value in array.items():
        if all(i in value for i in neighborhood):
            result += key
            counter += 1
    result += " \u2228 "
print(result[:-3], " ", counter)
