def can_reach_nen_path(grid):
    if not grid or not grid[0]:
        return False
    
    n, m = len(grid), len(grid[0])
    
    # dp[i][j] = maximum energy when reaching cell (i, j)
    dp = [[-1] * m for _ in range(n)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            
            current_energy = dp[i][j]
            
            # Move right
            if j + 1 < m:
                new_energy = current_energy + grid[i][j + 1]
                if new_energy > current_energy:
                    dp[i][j + 1] = max(dp[i][j + 1], new_energy)
            
            # Move down
            if i + 1 < n:
                new_energy = current_energy + grid[i + 1][j]
                if new_energy > current_energy:
                    dp[i + 1][j] = max(dp[i + 1][j], new_energy)
    
    return dp[n - 1][m - 1] != -1


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
    
    print("Grid 1:", can_reach_nen_path(grid1))  # True
    print("Grid 2:", can_reach_nen_path(grid2))  # False
