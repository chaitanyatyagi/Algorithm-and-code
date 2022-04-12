class Solution:
    def majorityElement(self, A, N):
        count = 1
        curr = A[0]
        for i in range(1,len(A)):
            if A[i] == curr:
                count += 1
            else:
                count -= 1
                if count == 0:
                    count = 1
                    curr = A[i]
        return curr