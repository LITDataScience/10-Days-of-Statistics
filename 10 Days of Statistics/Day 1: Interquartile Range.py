import statistics


class interquartileRange:

    def median(values: list, start_index: int, stop_index: int) -> float:
        length = stop_index - start_index + 1
        middle_index = start_index + length // 2
        if (length % 2) == 0:
            return (values[middle_index - 1] + values[middle_index]) / 2
        else:
            return values[middle_index]

    def quartiles(values: list) -> tuple:
        values = sorted(values)
        length = len(values)
        q2 = interquartileRange.median(values, 0, length - 1)
        middle_index = length // 2
        if (length % 2) == 0:
            q1 = interquartileRange.median(values, 0, middle_index - 1)
            q3 = interquartileRange.median(values, middle_index, length - 1)
        else:
            q1 = interquartileRange.median(values, 0, middle_index - 1)
            q3 = interquartileRange.median(values, middle_index + 1, length - 1)
        return q1, q2, q3

    def interquatile_range(values: list, frequencies: list) -> float:
        n = len(values)
        s = []
        for i in range(n):
            value = values[i]
            frequency = frequencies[i]
            for j in range(frequency):
                s.append(value)
        s.sort()
        qs = interquartileRange.quartiles(s)
        result = float(qs[2] - qs[0])
        return result


if __name__ == '__main__':
    n = int(input())
    x = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    print(interquartileRange.interquatile_range(x, f))