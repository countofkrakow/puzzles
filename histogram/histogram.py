# takes an array with nonnegative ints representing columns in a histogram
# returns the volume of water that will get caught in the histogram if water were poured over it vertically

def solveHistogram(hist):
    n = len(hist)
    maxFromLeft = []
    maxFromLeft.append(hist[0])
    maxFromRight = []
    maxFromRight.append(hist[n - 1])

    for column in range(1, n):
        maxFromLeft.append(max(maxFromLeft[column-1], hist[column]))

    for column in reversed(range(n-1)):
        maxFromRight.insert(0, (max(maxFromRight[0], hist[column])))

    sum = 0

    for i in range(n):
        sum += (min(maxFromLeft[i], maxFromRight[i]) - hist[i])

    return sum


if __name__ == "__main__":
    print (solveHistogram([2, 1, 4, 5, 1, 3, 3])) # expected 3
    print (solveHistogram([2, 0, 1, 0, 3, 7, 4, 3, 6])) # expected 10
