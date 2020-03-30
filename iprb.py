import sys
from itertools import product


def main(data):
    groups = list(map(int, data.split()))
    num = sum(groups)

    factors = dict(XX=groups[0], Xx=groups[1], xx=groups[2])

    # Probability that XX is chosen at least once
    non_XX = factors["Xx"] + factors["xx"]
    prob_not_XX = (non_XX / num) * ((non_XX - 1) / (num - 1))
    prob_XX = 1 - prob_not_XX

    # Probability that Xx chosen twice
    prob_Xx_Xx = (factors["Xx"] / num) * ((factors["Xx"] - 1) / (num - 1))

    # Probability that Xx then xx are chosen
    prob_Xx_then_xx = (factors["Xx"] / num) * (factors["xx"] / (num - 1))
    prob_xx_then_Xx = (factors["xx"] / num) * (factors["Xx"] / (num - 1))
    prob_Xx_xx = prob_Xx_then_xx + prob_xx_then_Xx

    # Probability of X being passed
    prob_X = prob_XX + (prob_Xx_Xx * 0.75) + (prob_Xx_xx * 0.5)
    print(prob_X)


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
