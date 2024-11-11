class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
    
        rows, cols = len(grid), len(grid[0])
        visit = [[False for _ in range(cols)] for _ in range(rows)]
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W' or visit[r][c]:
                return
            visit[r][c] = True
            
            dfs(r - 1, c)  
            dfs(r + 1, c)  
            dfs(r, c - 1)  
            dfs(r, c + 1)  
        
        island_cout = 0
        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 'L' and not visit[r][c]:
                    dfs(r, c)
                    island_cout += 1 

        return island_cout
                    
        
