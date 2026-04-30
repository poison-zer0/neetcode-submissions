class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_elements = {}
        for num in nums:
            if num not in frequent_elements:
                frequent_elements[num] = 1
            else:
                frequent_elements[num] += 1
        bucket_length = len(nums) + 1
        bucket = [[] for _ in range(bucket_length)]
        for key, value in frequent_elements.items():
            if not bucket[value]:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
        final_bucket = list()
        for bucket_item in reversed(bucket):
            for item in bucket_item:
                final_bucket.append(item)
                if len(final_bucket) == k:
                    return final_bucket
        return final_bucket
        