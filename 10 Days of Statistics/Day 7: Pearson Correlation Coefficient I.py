import statistics

class PearsonCoefficient:

    def FindMean(x):
        return round(statistics.mean(x), 1)

    def sDev(values, mean):
        data = [(val - mean) ** 2 for val in values]
        return (sum(data) / float(len(data))) ** 0.5

    def PCC(x, y):
        xM = PearsonCoefficient.FindMean(x)
        yM = PearsonCoefficient.FindMean(y)
        xStdev = PearsonCoefficient.sDev(x, xM)
        yStdev = PearsonCoefficient.sDev(y, yM)
        numerator = sum((x[i] - xM) * (y[i] - yM) for i in range(n))
        denominator = n * xStdev * yStdev
        return round((numerator / denominator), 3)

if __name__ == '__main__':
    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))
    print(PearsonCoefficient.PCC(x, y))
