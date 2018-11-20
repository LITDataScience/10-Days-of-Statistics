import math

class CentralLimitTheorem:

    def CLT(nTickets, sampleSize, mean, sdev):
        marginal_error = zScore * sdev / math.sqrt(sampleSize)
        print(round((mean - marginal_error), 2))
        print(round((mean + marginal_error), 2))


if __name__ == '__main__':
    sampleSize, mean, sdev, distPercentage, zScore = int(input()), int(input()), int(input()), float(input()), float(input())
    prob = CentralLimitTheorem.CLT(zScore, sampleSize, mean, sdev)

