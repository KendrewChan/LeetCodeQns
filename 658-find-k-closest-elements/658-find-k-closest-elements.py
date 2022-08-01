class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Base case
        if len(arr) == k:
            return arr
        
        # Find closest element via binary search & initialize 2 pointers
        left = self.binarySearch(arr,x)-1
        right = left+1
        
        # While window size is less than k, we expand the window
        while (right-left-1) < k:
             # prevent out of bounds
            if left == -1:
                right += 1
                continue
            if right == len(arr):
                left -= 1
                continue
            
            # Expand window to the side with the closer number
            if abs(arr[left]-x) <= abs(arr[right]-x): 
                # use the equals sign to prioritise leftside. This equates to both 1st && 2nd condition together
                left -= 1
            else:
                right += 1
                
        return arr[left+1:right]
    
    def binarySearch(self, arr, x):
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                left = mid+1
            else:
                right = mid-1
        return left