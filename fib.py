import sys
from functools import reduce


def reducer(k):
    def _reducer(acc, idx):
        if idx in (0, 1):
            return acc + [1]
        return acc + [(acc[idx - 2] * k) + acc[idx - 1]]

    return _reducer


def main(data):
    n, k = map(int, data.split())
    generations = reduce(reducer(k), range(n), [])
    print(generations[-1])


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
