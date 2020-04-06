import sys


def memo(func):
    store = dict()
    def _memo(*params):
        try:
            val = store[params]
        except KeyError:
            val = store[params] = func(*params)
        return val
    
    return _memo


def fibd(months, lifespan):
    @memo
    def _fibd(curr_m, age):
        if curr_m >= months:
            return 1
        next_m = curr_m + 1
        if age >= lifespan:
            return _fibd(next_m, 1)
        elif age == 1:
            return _fibd(next_m, age + 1)
        return _fibd(next_m, age + 1) + _fibd(next_m, 1)
    
    return _fibd(1, 1)



def main(data):
    n, m = map(int, data.split())
    print(fibd(n, m))


if __name__ == "__main__":
    main(sys.stdin.readline().strip())
