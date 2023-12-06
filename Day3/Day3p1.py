nearby = [
    (0, 1), (0, 0), (0, -1),
    (1, 1), (1, 0), (1, -1),
    (-1, 1), (-1, 0), (-1, -1),
] 

def adjacent(grid, i, j):
    ret = 0
    for near in nearby:
        r, c = near
        if grid[r+i][c+j].isnumeric():
            left = c+j 
            right = left+1
            num = ""
            while ((left >= 0 and grid[r+i][left].isnumeric()) or (right < len(grid[0]) and grid[r+i][right].isnumeric())):
                if (left >= 0 and grid[r+i][left].isnumeric()):
                    num = grid[r+i][left] + num 
                    grid[r+i][left] = '.'
                    left -= 1 
                if (right < len(grid[0]) and grid[r+i][right].isnumeric()):
                    num = num + grid[r+i][right]
                    grid[r+i][right] = '.'
                    right += 1
            if num:
                ret += int(num)
    
    return ret
            


def main():
    
    s = input()
    grid = []
    while s:
        grid.append([x for x in s])
        print(s)
        try:
            s = input()
        except EOFError:
            break
    
    ret = 0 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (not grid[i][j].isnumeric()) and grid[i][j] != '.':
                val = adjacent(grid, i, j)
                # print(val)
                ret += val
    
    return ret 

print(main())