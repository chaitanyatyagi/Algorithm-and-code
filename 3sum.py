class Solution:
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()

        for index,number in enumerate(nums):
            
            if index and number == nums[index-1]:
                continue
            i,j = index+1,n-1
            while i<j:
                res = [number,nums[i],nums[j]]
                curr = sum(res)
                if curr>0:
                    j -= 1
                elif curr<0:
                    i += 1
                else:
                    ans.append(res)
                    i += 1
                    while nums[i] == nums[i-1] and i<j:
                        i += 1
        return ans