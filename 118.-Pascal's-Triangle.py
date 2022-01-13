# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        ls = [[1]]
        for i in range(1, n):
            prev = ls[i - 1]
            row = [1]
            for j in range(1, len(prev)):
                sum = prev[j] + prev[j - 1]
                row.append(sum)
            row.append(1)
            ls.append(row)
        return ls
