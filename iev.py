import sys


PROB_DOM_PHENO = [1.0, 1.0, 1.0, 0.75, 0.5, 0.0]


def main(data):
    pairs = map(int, data.split())
    print(sum(num * prob * 2 for num, prob in zip(pairs, PROB_DOM_PHENO)))


if __name__ == "__main__":
    main(sys.stdin.readline())
