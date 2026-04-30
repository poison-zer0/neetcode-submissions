class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}
        for num in nums:
            if num not in frequent_elements:
                frequent_elements[num] = 1
            else:
                frequent_elements[num] += 1

        sorted_elements = sorted(frequent_elements, key = lambda x: frequent_elements[x], reverse=True)
        return sorted_elements[:k]