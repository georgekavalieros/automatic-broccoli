import sys
import time

path = []
paths = [[] for i in range(len(path))]
full_path = []


# Find All Paths
def find_paths(table, n):
    global full_path
    for i, row in enumerate(table):
        path.append(row[0])
        array = [row[:] for row in table]
        array = create_subarray(array, i, 0)
        if array:
            find_paths(array, n)
        if not array:
            cpath = [row[:] for row in path]
            if len(cpath) == n:
                full_path = cpath
            else:
                full_path = full_path[:-len(cpath)] + cpath
            paths.append(full_path)
            path.clear()
    return paths


# Remove unnecessary paths
def euler_paths(table, n):
    all_paths = find_paths(table, n)
    euler_paths = []
    for row in all_paths:
        if len(row) == len(set(row)):
            euler_paths.append(row)
    return euler_paths


# Copy array to temp. Remove row i and column j of temp.
def create_subarray(temp, k, l):
    for i, row in enumerate(temp):
        for j, num in enumerate(row):
            if j == l:
                row.remove(num)
    for i, row in enumerate(temp):
        if i == k:
            temp.remove(row)
    return temp


def find_subsets(array, length):
    pool = tuple(array)
    n = len(pool)
    if length > n:
        return
    index = list(range(length))
    yield tuple(pool[i] for i in index)
    while True:
        for i in reversed(range(length)):
            if index[i] != i + n - length:
                break
        else:
            return
        index[i] += 1
        for j in range(i+1, length):
            index[j] = index[j-1] + 1
        yield tuple(pool[i] for i in index)


# Find a subset of paths that create a latin square.
# Create a 2D array of zeros (counter).
# For each path we take we add 1 to counter[l][k].
# If counter[l][k] is 2, we had a collision.
def find_latin_square(table):
    counter = [[0 for i in range(len(table))] for j in range(len(table))]
    flag = 0
    paths = euler_paths(table, len(table))
    subsets = find_subsets(paths, len(table))
    for i, subset in enumerate(subsets):
        if subset[0][0] == subset[1][0] or subset[1][0] == subset[2][0] or subset[2][0] == subset[3][0]:
            continue
        for path in subset:
            for k, path_i in enumerate(path):
                for l, row in enumerate(table):
                    if path[k] == row[k]:
                        counter[l][k] += 1
                        if counter[l][k] > 1:
                            flag = 1
            if flag == 1:
                flag = 0
                counter = [[0 for i in range(len(table))] for j in range(len(table))]
                break

        for x in counter:
            if 0 in x:
                break
            else:
                return subset


def create_orthogonal_latin_square(table):
    latin_square = find_latin_square(table)
    if latin_square:
        orthogonal_latin_square = [["" for i in range(len(table))] for j in range(len(table))]
        for path in latin_square:
            for k, path_i in enumerate(path):
                for l, row in enumerate(table):
                    if path[k] == row[k]:
                        orthogonal_latin_square[l][k] = path[0]
        return orthogonal_latin_square
    else:
        return []


start_time = time.time()
# Main
if len(sys.argv) == 1:
    print('Please enter a filename.')
    sys.exit(-1)

s = sys.argv[1]
if s:
    list1 = []
    for line in open(s, 'r').read().splitlines():
        list1.append(line.split(', '))

    # # Print Euler paths.  --approximately 64seconds for 10x10 matrix
    # paths = euler_paths(list1, len(list1))
    # for x in paths:
    #     print(x)

    # # Print a latin square. --takes too long for 10x10 matrix. Has to match all 808 different paths
    # square = find_latin_square(list1)
    # if square:
    #     for x in square:
    #         print(x)
    # if not square:
    #     print("[]")

    # Runs well up to 6x6 squares.
    # Create graeco-latin square. --takes too long for 10x10 matrix.
    orthogonal_latin_square = create_orthogonal_latin_square(list1)
    graeco_latin_square = []
    if orthogonal_latin_square:
        for i, row in enumerate(orthogonal_latin_square):
                result = list(zip(list1[i], row))
                graeco_latin_square.append(result)

        for x in graeco_latin_square:
            print(x)
    else:
        print([])
else:
    print("File not exists")

print("--- %s seconds ---" % (time.time() - start_time))
