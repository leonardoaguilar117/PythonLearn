class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        numInv = num[::-1]
        if num == numInv:
            return True
        else:
            return False


sol = Solution()
print(sol.isPalindrome(10))
