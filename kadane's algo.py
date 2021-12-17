class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        neg = min(arr)
        zero = 0
        for i in range(len(arr)):
            zero += arr[i]
            if zero>neg:
                neg = zero
            if zero<0:
                zero = 0
        return neg