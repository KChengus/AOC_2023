import re

class Solution():
    def __init__(self):
        self.grid = []


    def pipes(self, dx, dy, pipe):
        if pipe == '|':
            # continue stright
            return (0, dy)
        if pipe == '-':
            # continue stright
            return (dx, 0)
        if pipe == 'L':
            # top of L 
            if (dy == 1):
                # go right
                return (1, 0)
            # right of L -> to up
            return (0, -1)
        if pipe == 'J':
            # top of J 
            if (dy == 1):
                # go Left
                return (-1, 0)
            # left of J -> to up
            return (0, -1)
        if pipe == '7':
            # bottom of 7 
            if (dy == -1):
                # go Left
                return (-1, 0)
            # left of 7 -> to down 
            return (0, 1)
        if pipe == 'F':
            # bottom of F 
            if (dy == -1):
                # go right 
                return (1, 0)
            # right of F -> to down 
            return (0, 1)
        return (-1,-1)

    def solve(self):
        cur_x = 0
        cur_y = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'S':
                    cur_x = j
                    cur_y = i
                    break
        startX = cur_x
        startY = cur_y
        adjs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]
        print(self.grid)
        for adj in adjs: 
            dx, dy = adj
            cur_y = startY + dy
            cur_x = startX + dx
            # if not (cur_y < 0 or cur_y >= len(self.grid) or cur_x < 0 or cur_x >= len(self.grid[0])):
            count = 0
            while startX != cur_x or startY != cur_y:
                dx, dy = self.pipes(dx, dy, self.grid[cur_y][cur_x])
                if dx == -1 and dy == -1:
                    break
                cur_x += dx 
                cur_y += dy
                count += 1
            if (dx != -1 or dy != -1):
                break
        return (count + 1) // 2
        



    def handle_input(self):
        s = input()
        while s:
            self.grid.append(s)
            try:
                s = input()
            except EOFError:
                break
    def run(self):
        self.handle_input()
        return self.solve()

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())