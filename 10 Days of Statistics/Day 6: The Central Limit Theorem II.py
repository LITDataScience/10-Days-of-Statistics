import math

class CentralLimitTheorem:

    def CLT(nTickets, n, mean, sd):
        newMean = n * mean
        newSd = (n ** 0.5) * sd
        return round(0.5 * (1 + math.erf((nTickets - newMean) / (newSd * math.sqrt(2)))), 4)


if __name__ == '__main__':
    tic, x, mean, sdev = int(input()), int(input()), float(input()), float(input())
    prob = CentralLimitTheorem.CLT(tic, x, mean, sdev)
    print(prob)
