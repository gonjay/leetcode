class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        for i in range(1,rows):
            grid[i][0] = grid[i-1][0] + grid[i][0]
        for j in range(1,cols):
            grid[0][j] = grid[0][j-1] + grid[0][j]
        for i in range(1,rows):
            for j in range(1,cols):
                grid[i][j] = min(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[rows-1][cols-1]

su = Solution()
grid = [[1,2],[5,6],[1,1]]
print su.minPathSum(grid)
