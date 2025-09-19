class Solution:
    def twoSum(self, nums, target):
        seen = {}  
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        
        raise ValueError("No two sum solution")

if __name__ == "__main__":
    param_1 = [2, 7, 11, 15]
    param_2 = 9
    ret = Solution().twoSum(param_1, param_2)
    print(ret)   # prints: [0, 1]


        