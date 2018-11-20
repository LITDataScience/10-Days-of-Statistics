import math

class CentralLimitTheorem:

    def CLT(maxWeight, n, mean, sd):
        newMean = n * mean
        newSd = (n ** 0.5) * sd
        return round(0.5 * (1 + math.erf((maxWeight - newMean) / (newSd * math.sqrt(2)))), 4)


if __name__ == '__main__':
    wt, x, mean, sdev = int(input()), int(input()), int(input()), int(input())
    prob = CentralLimitTheorem.CLT(wt, x, mean, sdev)
    print(prob)