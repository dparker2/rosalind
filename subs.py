import sys


def main(data):
    dna, motif = data
    positions = [
        str(i + 1) for i in range(len(dna)) if dna[i : i + len(motif)] == motif
    ]
    print(" ".join(positions))


if __name__ == "__main__":
    main(sys.stdin.read().splitlines())
