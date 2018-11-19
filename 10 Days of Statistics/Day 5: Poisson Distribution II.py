import math

class PoissonDistribution2:

    def poissonDistribution2(num):
        (val1, val2) = (num[0], num[1])
        print(round(160 + 40*(val1 + math.pow(val1,2)),3))
        print(round(128 + 40 * (val2 + math.pow(val2, 2)), 3))

if __name__ == '__main__':
    arr = list(map(float, input().split()))
    PoissonDistribution2.poissonDistribution2(arr)