import json
import sys


def hash_numbers(data):
    value = ";".join([str(d) for d in sorted(data)])
    return hash(value)


def put_value(data, cache, result):
    # sorted bo max z [1,2,3,4] jest taki sam jak dla [4,3,2,1]
    cache[hash_numbers(sorted(data))] = result


def m(data, cache):
    if len(data) == 3:
        return sum(data)
    sums = []
    size = len(data)
    hashed = hash_numbers(data)
    if hashed in cache:
        return cache[hashed]
    for i, d in enumerate(data):
        if i != 0 and i != size - 1:
            new = data[:]
            new.pop(i)
            result = m(new, cache)
            sums.append(result + d + data[i - 1] + data[i + 1])
            put_value(new, cache, result)
    return max(sums)


def main():
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = 'dane2.json'

    cache = {}

    with open(filename) as f:
        data = json.load(f)

    best = m(data, cache)
    print(best)


if __name__ == '__main__':
    main()
