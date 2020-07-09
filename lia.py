import sys
from math import factorial


PROB_Aa_Bb = 0.25
PROB_not_Aa_Bb = 1 - PROB_Aa_Bb


def binomial_coefficient(successes, trials):
    return factorial(trials) / (factorial(successes) * factorial(trials - successes))


def main(k_n):
    k, n = map(int, k_n.split())
    size = 2 ** k

    print(
        sum(
            [
                binomial_coefficient(i, size)
                * (PROB_Aa_Bb ** i)
                * (PROB_not_Aa_Bb ** (size - i))
                for i in range(n, size + 1)
            ]
        )
    )


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
