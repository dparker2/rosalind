import sys


def main(data):
    dna_1, dna_2 = data
    hamm = sum(1 for b1, b2 in zip(dna_1, dna_2) if b1 != b2)
    print(hamm)


if __name__ == "__main__":
    main(sys.stdin.read().splitlines())
