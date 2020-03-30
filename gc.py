import sys


def main(lines):
    max_ident = None
    max_gc = 0.0
    for line in lines:
        ident, *dna_lines = line.strip().split("\n")
        dna = "".join(dna_lines)
        gc = len(list(filter(lambda c: c in "GC", dna))) / len(dna) * 100
        if gc > max_gc:
            max_gc = gc
            max_ident = ident
    print(max_ident)
    print(max_gc)


if __name__ == "__main__":
    main(list(filter(None, sys.stdin.read().split(">"))))
