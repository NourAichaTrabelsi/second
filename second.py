def can_reach_nen_path(grid):
    """
    Determines if there exists a path from top-left to bottom-right
    in a grid following Nen Flow rules:
    - Move only right or down
    - Each step must go to a cell with strictly higher energy than the last step
    """
    if not grid or not grid[0]:
        return False
    
    n, m = len(grid), len(grid[0])
    
    # dp[i][j] stores the last cell value along a valid path reaching (i,j)
    dp = [[-1]*m for _ in range(n)]
    dp[0][0] = grid[0][0]
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            
            current_energy = dp[i][j]
            
            # Move right
            if j + 1 < m and grid[i][j+1] > current_energy:
                dp[i][j+1] = max(dp[i][j+1], grid[i][j+1])
            
            # Move down
            if i + 1 < n and grid[i+1][j] > current_energy:
                dp[i+1][j] = max(dp[i+1][j], grid[i+1][j])
    
    # If bottom-right cell was reached with a valid path
    return dp[n-1][m-1] != -1


# ---------------------------
# Testing
# ---------------------------
if __name__ == "__main__":
    
    grid1 = [
        [1, 2, 3],
        [2, 3, 4],
        [3, 4, 5]
    ]
    
    grid2 = [
        [5, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    
    grid3 = [
        [1, 3, 2],
        [2, 4, 5],
        [3, 5, 6]
    ]
    
    print("Grid 1:", can_reach_nen_path(grid1))  # True
    print("Grid 2:", can_reach_nen_path(grid2))  # False
    print("Grid 3:", can_reach_nen_path(grid3))  # True
