class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        stack = []
        hm = {}
        
        # Traverse from right to left
        for i in range(len(nums2) - 1, -1, -1):
            data = nums2[i]
            
            # Remove smaller elements
            while stack and stack[-1] <= data:
                stack.pop()
            
            # If stack empty → no greater element
            if not stack:
                hm[data] = -1
            else:
                hm[data] = stack[-1]
            
            stack.append(data)
        
        # Build answer
        ans = []
        for val in nums1:
            ans.append(hm[val])
        
        return ans