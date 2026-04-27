class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ni, nj = 0, 0
        for i in range(len(nums)):
            ni = nums[i]
            nj = target - ni
            if dic.get(nj) != None:
                return [dic.get(nj), i]
            dic[ni] = i
        return None