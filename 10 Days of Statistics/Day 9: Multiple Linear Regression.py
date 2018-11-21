from sklearn.linear_model import LinearRegression


class MultipleLinReg:

    def linreg(x, y, n):

        for i in range(n):
            vals = list(map(float, input().split()))
            x.append(vals[:-1])
            y.append(vals[-1])

        q = int(input())
        test = []
        for i in range(q):
            vals = list(map(float, input().split()))
            test.append(vals)

        reg = LinearRegression()
        reg.fit(x, y)

        pred = reg.predict(test)
        for i in pred:
            print(i)


if __name__ == '__main__':
    m, n = list(map(int, input().split()))
    x, y = [[] for _ in range(2)]
    MultipleLinReg.linreg(x, y, n)