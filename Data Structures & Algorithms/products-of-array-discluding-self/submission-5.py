class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force O(n2)
        # res = []
        # for i in range(len(nums)):
        #     prod_sum = 1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             prod_sum = prod_sum*nums[j]
        #     res.append(prod_sum)
        # return res
        # print(res)
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]
        return res
