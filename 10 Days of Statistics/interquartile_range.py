class MMM:
    def median(nums):
        if len(nums) % 2 == 0:
            return int(sum(nums[len(nums) // 2 - 1:len(nums) // 2 + 1]) / 2)
        else:
            return nums[len(nums) // 2]

    def quartiles(N, nums):
        Q1 = MMM.median(nums[:len(nums) // 2])
        Q2 = MMM.median(nums)
        if N % 2 == 0:
            Q3 = MMM.median(nums[len(nums) // 2:])
        else:
            Q3 = MMM.median(nums[len(nums) // 2 + 1:])
        return Q1, Q2, Q3

    def interquatile_range(values: list, frequencies: list, N) -> float:
        n = len(values)
        s = []
        for i in range(n):
            value = values[i]
            frequency = frequencies[i]
            for j in range(frequency):
                s.append(value)
        s.sort()
        qs = MMM.quartiles(N, s)
        result = float(qs[2] - qs[0])
        return result


if __name__ == '__main__':
    Num = int(input())
    nums = sorted([int(num) for num in input().split()])
    freq = sorted([int(num) for num in input().split()])
    print(MMM.interquatile_range(nums, freq, Num))
