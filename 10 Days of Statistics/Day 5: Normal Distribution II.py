import math

class NormalDistribution:
    """
        Formula for Normal Distribution -> cdf(x) = 1/2 * (1+ (erf((x-mean)/(standard Deviation * 2 ** 0.5))))
    """

    def cumulativeProb(x, mean, sdev):
        """
            Args:
                erf(): Error Function.abs
                sd: Standard Deviation.
        """
        return round(0.5 * 100 * (1 + math.erf((x - mean) / (sdev * (2 ** 0.5)))), 3)

if __name__ == '__main__':
    mean, sdev = list(map(float, input().split()))
    x, y= float(input()),  float(input())

    ans1 = round(100 - NormalDistribution.cumulativeProb(x, mean, sdev), 2)
    ans2 = round(100 - NormalDistribution.cumulativeProb(y, mean, sdev), 2)
    ans3 = round(NormalDistribution.cumulativeProb(60, 70, 10), 2)

    print(ans1)
    print(ans2)
    print(ans3)
