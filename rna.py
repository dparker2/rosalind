import sys


def main(dna):
    rna = dna.replace("T", "U")
    print(rna)


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
