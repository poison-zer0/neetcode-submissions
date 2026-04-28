class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False