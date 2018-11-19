import math

class PoissonDistribution:
    """
        Formula for Poisson's Distribution ->  P(k,mean) = ((mean^k)*(e^(-mean))) / (factorial(k))
    """

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * PoissonDistribution.factorial(n - 1)

    def poissonDistribution(mean, k):
        temp = ((mean ** k) * (math.e ** (-mean))) / PoissonDistribution.factorial(k)
        return temp




if __name__ == '__main__':
    mean, k = input(), input()
    pd = PoissonDistribution.poissonDistribution(mean, k)
    print(round(pd, 3))