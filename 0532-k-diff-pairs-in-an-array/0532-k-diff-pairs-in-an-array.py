class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        if k == 0: return sum(1 for v in freq.values() if v > 1)
        return sum(1 for num in freq if num + k in freq)
        