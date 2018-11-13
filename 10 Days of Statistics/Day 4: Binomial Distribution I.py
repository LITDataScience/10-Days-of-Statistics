import math
import operator as op
from functools import reduce

"""
    formula: b(n,r,p) = n!/((n-r)! * r!).p^r.q^(n-r)
"""
class BD:
    def findNcR(n, r):
        """
            Calculating: n!/((n-r)! * r!)
        """
        r = min(r, n - r)
        if r == 0:
            return 1
        numerator = reduce(op.mul, range(n, n - r, -1))
        denominator = reduce(op.mul, range(1, r + 1))
        return numerator // denominator

    def binomialDist(total, desired, Psuccess):
        """
            Calculating : b(n,r,p)
        """
        failure = 1 - Psuccess
        return BD.findNcR(total, desired) * math.pow(Psuccess, desired) * math.pow(failure, total - desired)


if __name__ == '__main__':
    exp = list(map(float, input().split()))
    boyProb = exp[0] / (exp[0] + exp[1])
    print(round(sum([BD.binomialDist(6, px, boyProb) for px in range(3, 7)]), 3))