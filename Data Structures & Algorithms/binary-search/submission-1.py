class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        middle = len(nums)//2
        while(nums[middle]!=target and upper - lower > 1):
            if target < nums[middle]:
                upper = middle
            elif target > nums[middle]:
                lower = middle
            middle = (lower + upper)//2
            print(lower)
            print(upper)
        if target == nums[middle]:
            return middle
        if (nums[lower] == target):
            return lower
        elif (nums[upper] == target):
            return upper
        else:
            return -1