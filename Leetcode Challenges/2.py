class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # We inverted and coverted string
        A = ''.join(map(str, l1[::-1]))
        B = ''.join(map(str, l2[::-1]))

        # We converted to integer the strings
        a = int(A)
        b = int(B)

        # Add of integers
        add = a + b

        # We convert to string and inverted to alocate in add2
        add1 = str(add)
        add2 = add1[::-1]

        # For each element of add2 we convert them to integer and alocate in a list
        return [int(digit) for digit in add2]


sol = Solution()
print(sol.addTwoNumbers([2, 4, 3], [5, 6, 4]))
