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

    def binomialDist2(p, q, n):
        """
            Calculating : b(n,r,p)
        """
        firstSum=0
        for i in range(0,3):
            ncr=BD.findNcR(n,i)
            temp=(p**i) * (q** (n-i))
            firstSum+=ncr*temp

        print(round(firstSum,3))

        secondSum=0
        for i in range(2,11):
            ncr=BD.findNcR(n,i)
            temp=(p**i) * (q** (n-i))
            secondSum+=ncr*temp

        print(round(secondSum,3))


if __name__ == '__main__':
    p,n = map(int, input().split())
    p /= 100
    q = 1-p
    BD.binomialDist2(p, q, n)