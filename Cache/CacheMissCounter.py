
# Counts how many times a cache miss would occur if a cache of the given sized were accesses
# with the access history given.
# Assumes cache has a policy of kicking out the element last accessed the longest ago.
def missCount(history, max_cache_size):
    q = []
    misses = 0
    for access in history:
        if q.count(access):
            q.remove(access)
            q.insert(0, access)
        elif len(q) < max_cache_size:
            q.insert(0, access)
            misses += 1
        else:
            q.pop()
            q.insert(0, access)
            misses += 1
    return misses


if __name__ == "__main__":
    print (missCount([1, 2, 3, 2, 3, 2, 4, 5, 2, 3], 3))