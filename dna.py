import sys
from collections import Counter


def main(data):
    counted = Counter(data)
    print(f"{counted['A']} {counted['C']} {counted['G']} {counted['T']}")


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
