from collections import defaultdict

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroindex = -1
        zeroless = [num for num in nums if num != 0]
        if len(nums) - len(zeroless) > 1:
            return [0] * len(nums)
        elif len(nums) - len(zeroless) == 1:
            zeroindex = nums.index(0)

        products = []
        for index, value in enumerate(zeroless):
            if index == 0:
                products.append(value)
            else:
                products.append(products[index - 1] * value)

        results = []
        if zeroindex != -1:
            results = [0] * len(nums)
            results[zeroindex] = products[-1]
            return results

        for index, value in enumerate(products):
            if index == 0:
                results.append(int((products[-1] / products[index])))
            else:
                results.append(int((products[-1] / products[index]) * products[index - 1]))

        return results