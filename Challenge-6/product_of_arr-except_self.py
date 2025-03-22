import array
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        - return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
        - You must write an algorithm that runs in O(n) time and without using the division operation.
        """
        length=len(nums)
        left_products=array.array('i',[1]*length)
        right_products=array.array('i',[1]*length)

        for idx in range (1,length):
            left_products[idx]=left_products[idx-1]*nums[idx-1]

        for idx in range (length-2,-1,-1):
            print(idx)
            right_products[idx]=right_products[idx+1]*nums[idx+1]

        ans=[]
        for idx in range(0,length):
            product=left_products[idx]*right_products[idx]
            ans.append(product)
        return ans