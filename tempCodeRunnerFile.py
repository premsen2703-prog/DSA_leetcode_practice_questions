def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        j, k = i + 1, n - 1
        while j < k:
            if j > i + 1 and nums[j] == nums[j - 1]:
                j += 1
                continue
            if k < n - 1 and nums[k] == nums[k + 1]:
                k -= 1
                continue

            total = nums[i] + nums[j] + nums[k]
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

    return result

print(threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]