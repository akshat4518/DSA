class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k <0:
            return 0
        freq ={}
        for x in nums:
            if x in freq :
                freq[x]=freq[x]+1
            else:
                freq[x] = 1
        count = 0
        for x in freq:
            if k ==0:
                if freq[x]>1:
                    count+=1
            else:
                if x+k in freq:
                    count+=1
        return count
        