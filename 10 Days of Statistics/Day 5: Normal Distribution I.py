import math

class NormalDistribution:
    """
        Formula for Normal Distribution -> cdf(x) = 1/2 * (1+ (erf((x-mean)/(standard Deviation * 2 ** 0.5))))
    """

    def cumulativeProb(x, mean, sd):
        """
            Args:
                erf(): Error Function.abs
                sd: Standard Deviation.
        """
        return round(0.5 * (1 + math.erf((x - mean) / (sd * (2 ** 0.5)))), 3)


if __name__ == '__main__':
    mean, sd = list(map(float, input().split()))
    x = float(input())
    a, b = list(map(float, input().split()))

    ans1 = NormalDistribution.cumulativeProb(x, mean, sd)
    ans2 = NormalDistribution.cumulativeProb(b, mean, sd) - NormalDistribution.cumulativeProb(a, mean, sd)

    print(ans1)
    print(ans2)

