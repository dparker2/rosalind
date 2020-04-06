import sys
from functools import reduce


MOD = 1000000
PS = dict(
    L=6,
    S=6,
    R=6,
    P=4,
    V=4,
    T=4,
    A=4,
    G=4,
    I=3,
    Stop=3,
    F=2,
    Y=2,
    H=2,
    N=2,
    D=2,
    Q=2,
    K=2,
    E=2,
    C=2,
    M=1,
    W=1,
)


def main(prot):
    mul = lambda acc, x: (acc * x) % MOD
    print(reduce(mul, [PS[p] for p in prot], PS["Stop"]))


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
