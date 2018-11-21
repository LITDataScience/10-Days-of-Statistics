class SPCC:

    def spearmanscoeff(x, y, n):

        # calculating the range of x and y.
        rx = [sorted(x).index(_) + 1 for _ in x]
        ry = [sorted(y).index(_) + 1 for _ in y]

        # finding di^2 and coefficient.
        di = [(x - y) ** 2 for (x, y) in zip(rx, ry)]
        coeff = 1 - (6 * sum(di)) / (n ** 3 - n)
        return coeff



if __name__ == '__main__':
    n = int(input())
    x, y = [list(map(float, input().split())) for _ in range(2)]
    print(round(SPCC.spearmanscoeff(x, y, n), 3))
