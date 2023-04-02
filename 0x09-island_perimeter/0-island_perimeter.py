def island_perimeter(grid):
    perimeter = 0
    
    # loop through the rows and columns of the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            
            # check if the current cell is land
            if grid[row][col] == 1:
                
                # add 4 to the perimeter for each land cell
                perimeter += 4
                
                # check if the cell to the left is also land
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2
                
                # check if the cell above is also land
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 2
                    
    return perimeter
