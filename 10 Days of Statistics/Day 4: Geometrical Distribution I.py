class GeometricalDistribution:

    def geoDist(N, numerator, denominator):
        """
            Formula of p.d.f: P(x) = q^(N-1)p
            p = Probability of success.
            q = Probability of Failure.
            N = Number of Trials
        """
        pSuccess = numerator / denominator
        pFailure = 1 - pSuccess

        geometrical_distribution = (pFailure ** (N - 1)) * pSuccess
        return geometrical_distribution


if __name__ == '__main__':
    num, den = map(int, input().split())
    N = int(input())
    gd = GeometricalDistribution.geoDist(N, num, den)
    ## rounding off to 3-digits.
    print(round(gd, 3))