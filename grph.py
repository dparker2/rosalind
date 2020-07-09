import sys
from itertools import combinations


def main(fasta_sections):
    tips = dict()
    for section in fasta_sections:
        ident, dna = section.split("\n", 1)
        dna = dna.replace("\n", "")
        tips[ident] = (dna[:3], dna[-3:])

    for (id1, tips1), (id2, tips2) in combinations(tips.items(), 2):
        if tips1[1] == tips2[0]:
            print(f"{id1} {id2}")
        if tips2[1] == tips1[0]:
            print(f"{id2} {id1}")


if __name__ == "__main__":
    main(sys.stdin.read().strip(">").split(">"))
