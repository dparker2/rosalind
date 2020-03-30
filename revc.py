import sys


def main(dna):
    mapping = dict(A="T", T="A", C="G", G="C")
    rev_comp = "".join(mapping[char] for char in dna[::-1])
    print(rev_comp)


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
