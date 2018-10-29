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

if __name__ == '__main__':
    N = int(input())
    nums = sorted([int(num) for num in input().split()])
    Q1, Q2, Q3 = MMM.quartiles(N, nums)
    print(Q1)
    print(Q2)
    print(Q3)